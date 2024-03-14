# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:53:04 2023

@author: vincentkuo
"""

import os
from datetime import datetime
import base64
import pandas as pd

path = "C:\\Users\\vincentkuo\\Downloads\\Test"


currentDate = datetime.now().year*10000+datetime.now().month*100+datetime.now().day # YYYYMMDD
#print(currentDate)

allFileList = os.listdir(path)

''' 檢查是否對應名稱資料夾存在、且有檔案
'''
executeDocumentFlag = False
executeDocuments = []
executeFiles = []
for file in allFileList:
    if(os.path.isdir(os.path.join(path, file)) and file==str(currentDate)):
        print(file, "Change to this folder")
        allList = os.walk(os.path.join(path, file))
        for root, dirs, files in allList:
#            print("path:", root)
#            print("directory:", dirs)
#            print("file:", files)
            if(len(files)>0):
                executeDocumentFlag = True
                executeDocuments.append(root)
                executeFiles.append(files)
    else:
        print(file, "Do not Excute")

if executeDocumentFlag:
    for index in range(len(executeDocuments)):
        filesNameList = executeFiles[index]
        for file in filesNameList:
            filePath = executeDocuments[index]+"\\"+file
            if(file[-3:].lower()=='pdf'):
                print("PDF!!")
                with open(filePath, "rb") as f:
                    print(f.read()[:10])
            elif(file[-3:].lower()=='lsx' or file[-3:].lower()=='xls'):
                print("Excel!!")
                data = pd.read_excel(filePath)
                print(data.head(5))
            elif(file[-3:].lower()=='txt'):
                print("Txt!!")
            elif(file[-3:].lower()=='csv'):
                print("CSV!!")
            else:
                print(file[-3:]," Pass!!")
#            with open(filePath, "rb") as f:
##                print(f.read())
#                encoded_bytes = base64.b64encode(f.read())
#                print(encoded_bytes)
#                encoded_string = encoded_bytes.decode("utf-8")
#allList = os.walk(path)
#for root, dirs, files in allList:
#    print("path:", root)
#    print("directory:", dirs)
#    print("file:", files)