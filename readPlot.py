# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:06:36 2021

@author: vincentkuo
"""


from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

text,text_chi,test_fix,='','',''

def main():
    print('########### BEGIN ###########')
    
    # 移動圖片位置 (Translation)
    def translate(img, x, y):
        transMat = np.float32([[1,0,x],[0,1,y]])
        dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img, transMat, dimensions)
    # -x → 往左移動 ; x → 往右移動
    # -y → 往上移動 ; y → 往下移動
    # translated = translate(img, -100, 100)
    # cv.imshow('Translated', translated)
    
    # 旋轉圖片
    def rotate(img, angle, rotPoint=None):
        (height,width) = img.shape[:2]
        if rotPoint is None:
         rotPoint = (width//2,height//2)
         
         rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
         dimensions = (width,height)
        return cv.warpAffine(img, rotMat, dimensions)
    # 輸入角度作為參數
    # rotated = rotate(img, -45)
    # cv.imshow(‘Rotated’, rotated)
    
    
    # pytesseract.pytesseract.tesseract_cmd = r'C://Users//vincentkuo//AppData//Local//Programs//Tesseract-OCR//tesseract.exe'
    #指定tesseract.exe執行檔位置
    # img = Image.open('C://Users//vincentkuo//Downloads//(憑證)Y211109 軟研.jpg') #圖片檔案位置
    # #img = Image.open('C://Users//vincentkuo//Downloads//(憑證)Y211125 軟研.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//(憑證)Y211221 軟研.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//(憑證)Y211227 軟研.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//(憑證)Y211227 軟研 (2).jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-triple//s1.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-e//s2.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s3.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s4.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s5.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s5_2.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s6.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s7.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s8.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s9.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-cashier//s10.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-cashier//s10_2.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s11.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//s12.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-ecalculator//s13.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-cashier//s14.jpg') #圖片檔案位置
    # img = Image.open('C://Users//vincentkuo//Downloads//Sample//invoice-e//F1_2.jpg') #圖片檔案位置
    img = cv.imread('D://舊電腦文件//下載//Sample//invoice-triple//E4_400.png')
    
    imgSave = Image.open('D://舊電腦文件//下載//Sample//invoice-triple//E4.jpg')
    # imgSave.save('C://Users//vincentkuo//Downloads//Sample//invoice-triple//E4_400.png', dpi=(400,400))
    
    # 模糊化 (Blur)
    # 注意 Kernel size必須是奇數(odd)，kernel size越大越模糊
    # 模糊化也有許多不同的方法可以進行，讓 kernel依據需求進行運算。
    # blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    # cv.imshow('Blur', blur)
    
    # 輪廓化(edge cascade)
    # 小技巧，可以先將圖片模糊化，再進行輪廓化，可以抓到比較少雜訊。
    canny = cv.Canny(img, 125, 175)
    cv.imshow('Canny Cats', canny)
    
    # 注意膨脹、侵蝕用的照片是已經輪廓化處理過。雜訊會較少。
    # 膨脹 dilating
    dilated = cv.dilate(canny, (7,7), iterations=3)
    cv.imshow('Dilated', dilated)
    
    # 侵蝕 eroding
    eroded = cv.erode(dilated, (3,3), iterations=1)
    cv.imshow('Eroded', eroded)
    
    cv.waitKey(0)
    global text, text_chi, test_fix
    # text = pytesseract.image_to_string(img, lang='eng') #讀英文
    # #text_chi = pytesseract.image_to_string(img, lang='chi_sim') #簡體中文
    # text_chi = pytesseract.image_to_string(img, lang='chi_tra') #繁體中文
    test_fix = pytesseract.image_to_string(img, lang='chi_tra+eng') #繁體中文
    text_chi = pytesseract.image_to_string(eroded, lang='chi_tra+eng') #繁體中文
    
    # 只選擇數字
    cong = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_data(img,config=cong)
    for x,b in enumerate(boxes.splitlines()):
        if x!=0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
                cv.putText(img,b[11],(x,y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

if __name__ == '__main__':
    main()