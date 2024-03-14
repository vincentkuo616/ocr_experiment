# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:06:36 2021

@author: vincentkuo
"""


from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
from pdf2image import convert_from_path
import fitz

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
    
    pytesseract.pytesseract.tesseract_cmd = r'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
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
    # img = cv.imread('D://舊電腦文件//下載//Sample//invoice-triple//E4_400.png')
    #C:\Users\vincentkuo\Downloads\發票\測試發票\台幣\J57247288-DE1-20230300017_聯強國際
    # img = Image.open('D://舊電腦文件//下載//Sample//invoice-triple//E4.jpg')
    
    def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
        # 打開PDF文件
        pdf = fitz.open(pdfPath)
        for pg in range (0, 1):
            page = pdf[pg]
            # 設置縮放和旋轉系數
#            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            # 開始寫圖像
            #pm.writePNG(imgPath+str(pg)+".png")
#            print(pm)
#            pm.set_pixel(2974,4209,[255,255,255])
            pm.set_dpi(400,400)
            pm.save(imgPath)
        pdf.close()
#    pdf_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247288-DE1-20230300017_聯強國際.pdf'
    #LJ57247288-DE1-20230300017 LJ57247311-DE1-20230300031 LJ57247318-DE1-20230300036 LJ57247319-DE1-20230300037 LJ57247324-DE1-20230300040
    #LJ57247348-DE1-20230300053 LJ57247351-DE1-20230300056 LJ57247352-DE1-20230300057 LJ57247359-DE1-20230300059 LJ57247360-DE1-20230300060_3x3
    #F2_3003096658 F2_3003096659 F2_3003096660 F2_3003096661 F2_3003096662
    #F2_3003096663 F2_3003096664 F2_3003096665 F2_3003096666 F2_3003096667
#    pdf_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_聯強國際.pdf'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247288-DE1-20230300017_widthTest1.jpg'
    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247288-DE1-20230300017_聯強國際.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247288-DE1-20230300017_聯強國際.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_2.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2x2.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2x3.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2x0-8.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2x0-5.jpg'
#    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247360-DE1-20230300060_sizeTest2x0-46.jpg'
    pdf_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/外幣/F2_3003096667.pdf'
    img_path = 'C:/Users/vincentkuo/Downloads/發票/測試發票/外幣/F2_3003096667.jpg'
#    pdf_image(pdf_path,img_path,2.8,2.8,0)
#    pdf_image(pdf_path,img_path,5,5,0)
#    pdf_pages = convert_from_path(PDF_file, 500, poppler_path=path_to_poppler_exe)
    img = Image.open(img_path)
    img = cv.imdecode(np.fromfile(img_path,dtype=np.uint8), -1)
#    img = cv.resize(img, None, fx=0.46, fy=0.46, interpolation=cv.INTER_LINEAR)
#    status = cv.imwrite('C:/Users/vincentkuo/Downloads/LJ57247360-DE1-20230300060_sizeTest.jpg',img)
#    print(status)
    # imgSave.save('C://Users//vincentkuo//Downloads//Sample//invoice-triple//E4_400.png', dpi=(400,400))
    
    # 模糊化 (Blur)
    # 注意 Kernel size必須是奇數(odd)，kernel size越大越模糊
    # 模糊化也有許多不同的方法可以進行，讓 kernel依據需求進行運算。
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#    cv.imshow('Blur', blur)
    
    # 輪廓化(edge cascade)
    # 小技巧，可以先將圖片模糊化，再進行輪廓化，可以抓到比較少雜訊。
    canny = cv.Canny(img, 125, 175)
#    cv.imshow('Canny Cats', canny)
    
    # 注意膨脹、侵蝕用的照片是已經輪廓化處理過。雜訊會較少。
    # 膨脹 dilating
    dilated = cv.dilate(canny, (7,7), iterations=3)
#    cv.imshow('Dilated', dilated)
    
    # 侵蝕 eroding
    eroded = cv.erode(dilated, (3,3), iterations=1)
#    cv.imshow('Eroded', eroded)
    
    # 二值化 threshold
    ret, binary = cv.threshold(img, 240, 255, cv.THRESH_BINARY)
#    cv.imshow('Eroded', eroded)
    
#    cv.imshow('img', img)
#    cv.waitKey(0)
#    cv.destroyAllWindows()
    global text, text_chi, test_fix, test_fix2, test_eroded, test_blur, test_canny, test_dilated
    global test_fixE, test_fix2E, test_erodedE, test_blurE, test_cannyE, test_dilatedE
    global zh1, zh2, zh3, zh4, zh5, zh6, zh7, zhtest, zhtest2
    global en1, en2, en3, en4, en5, en6, en7
    global height, width, x1, x2, y1, y2
    global size1, size2, size3, size4, size5, size6, size7, size8, size9
    # text = pytesseract.image_to_string(img, lang='eng') #讀英文
    # #text_chi = pytesseract.image_to_string(img, lang='chi_sim') #簡體中文
    # text_chi = pytesseract.image_to_string(img, lang='chi_tra') #繁體中文
#    test_fix = pytesseract.image_to_string(img, lang='chi_tra+eng') #繁體中文
    text = img
#    print(img.shape)
    height, width, _ = img.shape
#    img = img[340:420, 400:700] ## y , x
    """
    中文模板，特定位置OCR辨識
    """
    test_fix2 = pytesseract.image_to_string(img, lang='chi_tra+eng') #繁體中文
#    zh1 = pytesseract.image_to_string(img[3600:3680, 2460:2780], lang='chi_tra+eng') #繁體中文
#    zh2 = pytesseract.image_to_string(img[100:230, 1200:1780], lang='chi_tra+eng') #繁體中文 blur
#    zh3 = pytesseract.image_to_string(img[340:420, 400:700], lang='eng') #繁體中文
#    zh4 = pytesseract.image_to_string(img[240:310+1, 1300:1670+1], lang='eng') #繁體中文 blur
#    zh5 = pytesseract.image_to_string(img[840:910, 2340:2820], lang='eng') #繁體中文
#    zh6 = pytesseract.image_to_string(img[940:1010, 2430:2840], lang='eng') #繁體中文
#    zh7 = pytesseract.image_to_string(img[3800:3865, 1760:2145], lang='eng') #繁體中文
#    zhtest = pytesseract.image_to_string(img[3450:3560, 102:430], lang='chi_tra+eng') #繁體中文
#    y1 = np.floor(3600*height/4210)
#    y2 = np.ceil(3680*height/4210)
#    x1 = np.floor(2460*height/2975)
#    x2 = np.ceil(2780*height/2975)
#    zh1 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='chi_tra+eng') #繁體中文
#    y1 = np.floor(100*height/4210)
#    y2 = np.ceil(230*height/4210)
#    x1 = np.floor(1200*height/2975)
#    x2 = np.ceil(1780*height/2975)
#    zh2 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='chi_tra+eng') #繁體中文 blur
#    y1 = np.floor(340*height/4210)
#    y2 = np.ceil(420*height/4210)
#    x1 = np.floor(400*height/2975)
#    x2 = np.ceil(700*height/2975)
#    zh3 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='eng') #繁體中文
#    y1 = np.floor(240*height/4210)
#    y2 = np.ceil(310*height/4210)
#    x1 = np.floor(1300*height/2975)
#    x2 = np.ceil(1670*height/2975)
#    zh4 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='eng') #繁體中文 blur
#    y1 = np.floor(840*height/4210)
#    y2 = np.ceil(910*height/4210)
#    x1 = np.floor(2340*height/2975)
#    x2 = np.ceil(2820*height/2975)
#    zh5 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='eng') #繁體中文
#    y1 = np.floor(940*height/4210)
#    y2 = np.ceil(1010*height/4210)
#    x1 = np.floor(2430*height/2975)
#    x2 = np.ceil(2840*height/2975)
#    zh6 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='eng') #繁體中文
#    y1 = np.floor(3800*height/4210)
#    y2 = np.ceil(3865*height/4210)
#    x1 = np.floor(1760*height/2975)
#    x2 = np.ceil(2145*height/2975)
#    zh7 = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='eng') #繁體中文
#    y1 = np.floor(3450*height/4210)
#    y2 = np.ceil(3560*height/4210)
#    x1 = np.floor(102*height/2975)
#    x2 = np.ceil(430*height/2975)
#    zhtest = pytesseract.image_to_string(img[y1:y2, x1:x2], lang='chi_tra+eng') #繁體中文
    zh1 = pytesseract.image_to_string(img[3600*height//4210:3680*height//4210+1, 2460*width//2975:2780*width//2975+1], lang='chi_tra+eng') #繁體中文
#    zh2 = pytesseract.image_to_string(img[740:1060 ,75:130], lang='chi_tra+eng') #繁體中文 blur
    zh2 = pytesseract.image_to_string(img[100*height//4210:230*height//4210+1, 1200*width//2975:1780*width//2975+1], lang='chi_tra+eng') #繁體中文 blur
    zh3 = pytesseract.image_to_string(img[340*height//4210:420*height//4210+1, 400*width//2975:700*width//2975+1], lang='eng') #繁體中文
    zh4 = pytesseract.image_to_string(img[240*height//4210:310*height//4210+1, 1300*width//2975:1670*width//2975+1], lang='eng') #繁體中文 blur
    zh5 = pytesseract.image_to_string(img[840*height//4210:910*height//4210+1, 2340*width//2975:2820*width//2975+1], lang='eng') #繁體中文
#    zh6 = pytesseract.image_to_string(img[940*height//4210:1010*height//4210+1, 2440*width//2975:2840*width//2975+1], lang='eng') #繁體中文 
    zh6 = pytesseract.image_to_string(img[940*height//4210:1010*height//4210+1, 2430*width//2975:2840*width//2975+1], lang='eng') #繁體中文
    zh7 = pytesseract.image_to_string(img[3800*height//4210:3865*height//4210+1, 1760*width//2975:2145*width//2975+1], lang='eng') #繁體中文
#    zhtest = pytesseract.image_to_string(img[3450*height//4210:3560*height//4210+1, 102*width//2975:430*width//2975+1], lang='chi_tra+eng') #繁體中文  
#    zhtest = pytesseract.image_to_string(img[3450*height//4210:3560*height//4210+1, 1760*width//2975:2145*width//2975+1], lang='eng') #繁體中文  
#    img = img[100*height//4210:230*height//4210+1, 1200*width//2975:1780*width//2975+1]
#    img = img[240:310, 1300:1670]
#    cv.imshow('img', img) #1748 1779 809 988
#    cv.waitKey(0)
#    cv.destroyAllWindows()
    """
    英文模板，特定位置OCR辨識
    """
    en1 = pytesseract.image_to_string(img[133:260, 40:725], lang='eng') #英文
    en2 = pytesseract.image_to_string(img[120:220, 1925:2350], lang='eng') #英文
    en3 = pytesseract.image_to_string(img[730:790, 520:860], lang='eng') #英文
    en4 = pytesseract.image_to_string(img[730:790, 1010:1260], lang='eng') #英文
    en5 = pytesseract.image_to_string(img[444:500, 1270:1630], lang='eng') #英文
    en6 = pytesseract.image_to_string(img[730:790, 1830:2300], lang='eng') #英文
    en7 = pytesseract.image_to_string(img[860:920, 520:860], lang='eng') #英文
    """
    圖片調整測試區塊
    """
#    temp = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)
#    size1 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_LINEAR)
#    size2 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_LINEAR)
#    size3 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.4, fy=0.4, interpolation=cv.INTER_LINEAR)
#    size4 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
#    size5 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_LINEAR)
#    size6 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.7, fy=0.7, interpolation=cv.INTER_LINEAR)
#    size7 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.8, fy=0.8, interpolation=cv.INTER_LINEAR)
#    size8 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    temp = cv.resize(img, None, fx=0.9, fy=0.9, interpolation=cv.INTER_LINEAR)
#    size9 = pytesseract.image_to_string(temp, lang='chi_tra+eng') #繁體中文
#    test_fix2 = pytesseract.image_to_string(Image.fromarray(img), lang='chi_tra+eng') #繁體中文
#    test_eroded = pytesseract.image_to_string(Image.fromarray(eroded), lang='chi_tra+eng') #繁體中文
#    test_blur = pytesseract.image_to_string(Image.fromarray(blur), lang='chi_tra+eng') #繁體中文
#    test_canny = pytesseract.image_to_string(Image.fromarray(canny), lang='chi_tra+eng') #繁體中文
#    test_dilated = pytesseract.image_to_string(Image.fromarray(dilated), lang='chi_tra+eng') #繁體中文
#    test_fix2E = pytesseract.image_to_string(Image.fromarray(img), lang='eng') #英文
#    test_erodedE = pytesseract.image_to_string(Image.fromarray(eroded), lang='eng') #英文
#    test_blurE = pytesseract.image_to_string(Image.fromarray(blur), lang='eng') #英文
#    test_cannyE = pytesseract.image_to_string(Image.fromarray(canny), lang='eng') #英文
#    test_dilatedE = pytesseract.image_to_string(Image.fromarray(dilated), lang='eng') #英文
    img = Image.open(img_path)
#    img = img.crop((1300,240,1671,311))
#    newsize = (img.width*16//35, img.height*16//35) [240:310, 1300:1670]
#    img = img.resize(newsize)
#    img.show()
#    img.save('C:/Users/vincentkuo/Downloads/LJ57247288-DE1-20230300017_widthTest2.jpg',dpi=(400,400))
    test_fix = pytesseract.image_to_string(img, lang='chi_tra+eng') #繁體中文
#    test_fixE = pytesseract.image_to_string(img, lang='eng') #英文
#    text_chi = pytesseract.image_to_string(eroded, lang='chi_tra+eng') #繁體中文
    
    # 只選擇數字
#    cong = r'--oem 3 --psm 6 outputbase digits'
#    boxes = pytesseract.image_to_data(img,config=cong)
#    for x,b in enumerate(boxes.splitlines()):
#        if x!=0:
#            b = b.split()
#            print(b)
#            if len(b) == 12:
#                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#                cv.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#                cv.putText(img,b[11],(x,y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

if __name__ == '__main__':
    main()