# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:44:43 2023

@author: vincentkuo
"""

"""
This code sample shows Custom Extraction Model operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""
#'''
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://aiformrecognize.cognitiveservices.azure.com/"
endpoint = "https://vincentformtest.cognitiveservices.azure.com/"
key = "6cf5e8c70ebb42b0b0cd1d0a6edd8753"
key = "953e98b2fc6b46f1bbc8b9b0eac2bd6d"

model_id = "aiInvoiceZh1"
#model_id = "aiInvoiceZh2"
model_id = "aiInvoiceZh3"
model_id = "aiInvoiceZh4"
model_id = "aiInvoiceZhEn"
model_id = "aiInvoiceZh5"
model_id = "aiInvoiceZh6" # 版本二
#model_id = "aiInvoiceZh7" # 版本三
model_id = "aiInvoiceZh8" # alphanumeric
model_id = "aiInvoiceZh9" # chineseTest : 2306
model_id = "prebuilt-read" # 
#model_id = "prebuilt-layout" # 
#model_id = "prebuilt-document" # 
model_id = "prebuilt-invoice" # 
model_id = "vincentTestFinal" # 
#model_id = "prebuilt-receipt" # receipt
#model_id = "prebuilt-businessCard" # 
#model_id = "prebuilt-idDocument" # 
#model_id = "prebuilt-tax.us.w2" # 
#model_id = "aiInvoiceEn1"
#formUrl = "https://vincentstored.blob.core.windows.net/?sv=2022-11-02&ss=bfqt&srt=c&sp=rwdlacupiytfx&se=2023-05-02T13:56:50Z&st=2023-05-02T05:56:50Z&spr=https&sig=xtTWBR%2B9TQVToLgs213oN7ellqdhzJLC5rfqtUzA1ac%3D"
formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247348-DE1-20230300053_%E8%81%AF%E5%BC%B7%E5%9C%8B%E9%9A%9B.pdf"
formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247348-DE1-20230300053_聯強國際.pdf"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247351-DE1-20230300056_聯強國際.pdf"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247352-DE1-20230300057_聯強國際.pdf"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247359-DE1-20230300059_聯強國際.pdf"
formUrl = "https://aizh1.blob.core.windows.net/invoice-zh-test/LJ57247360-DE1-20230300060_聯強國際.pdf"
formUrl = "https://vincentstored.blob.core.windows.net/vincentform/LJ57247288-DE1-20230300017_聯強國際.pdf"
#formUrl = "file:///C:/Users/vincentkuo/Downloads/%E7%99%BC%E7%A5%A8/%E6%B8%AC%E8%A9%A6%E7%99%BC%E7%A5%A8/%E5%8F%B0%E5%B9%A3/LJ57247288-DE1-20230300017_聯強國際.pdf"
#formUrl = "http://demo.net5s.com/USER/Userfile/FILE/ff170616135351117163.pdf"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-en-test/F2_3003096663.PDF"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-en-test/F2_3003096664.PDF"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-en-test/F2_3003096665.PDF"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-en-test/F2_3003096666.PDF"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-en-test/F2_3003096667.PDF"
#formUrl = "https://aizh1.blob.core.windows.net/invoice-zh/LJ57247288-DE1-20230300017_聯強國際.pdf"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
#poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
with open("C:/Users/vincentkuo/Downloads/發票/測試發票/台幣/LJ57247288-DE1-20230300017_聯強國際.PDF", "rb") as f:
    poller = document_analysis_client.begin_analyze_document(model_id, document=f)
result = poller.result()
#temp2 = result.pages[0].lines
temp2 = result.pages[0]
temp3 = result.key_value_pairs

for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))
    for name, field in document.fields.items():
        field_value = field.value if field.value else field.content
        print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))
        print(name)


# iterate over tables, lines, and selection marks on each page
for page in result.pages:
    print("\nLines found on page {}".format(page.page_number))
#    print(len(page.lines))
#    print(page.lines)
#    for line in page.lines:
#        print(line)
#        print("...Line '{}'".format(line.content))
    for line in range(len(page.lines)):
        print("...Line '{}'".format(page.lines[line].content))
#        print(page.lines[line].polygon[0].x)
#        print(page.lines[line].polygon[2].x)
#        print(page.lines[line].polygon[0].y)
#        print(page.lines[line].polygon[2].y)
#        if(line==40): print(page.lines[line])
#    for word in page.words:
#        print(
#            "...Word '{}' has a confidence of {}".format(
#                word.content, word.confidence
#            )
#        )
    for selection_mark in page.selection_marks:
        print(
            "...Selection mark is '{}' and has a confidence of {}".format(
                selection_mark.state, selection_mark.confidence
            )
        )

# iterate over tables, paragraphs, and selection marks on each page
#for page in result.paragraphs:
#    print(len(page.lines))
#    print(page.content)
#    for line in page.lines:
#        print(line)
#        print("...Line '{}'".format(line.content))
#    for line in range(len(page.lines)):
#        print("...Line '{}'".format(page.lines[line].content))
#        print(page.lines[line].polygon[0].x)
#        print(page.lines[line].polygon[2].x)
#        print(page.lines[line].polygon[0].y)
#        print(page.lines[line].polygon[2].y)

# iterate over tables, key_value_pairs on each page
for page in result.key_value_pairs:
#    print(len(page.lines))
    if page.value==None: 
        value=""
    else:
        value=page.value.content
    print(page.key.content,"----",value)
#    for line in page.lines:
#        print(line)
#        print("...Line '{}'".format(line.content))
#    for line in range(len(page.lines)):
#        print("...Line '{}'".format(page.lines[line].content))
#        print(page.lines[line].polygon[0].x)
#        print(page.lines[line].polygon[2].x)
#        print(page.lines[line].polygon[0].y)
#        print(page.lines[line].polygon[2].y)

for i, table in enumerate(result.tables):
    print("\nTable {} can be found on page:".format(i + 1))
    for region in table.bounding_regions:
        print("...{}".format(i + 1, region.page_number))
    for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.row_index, cell.column_index, cell.content
            )
        )
print("-----------------------------------")
#print(result.content)
########### Python 3.x #############
#import http.client
#import time
#
#headers = {
#    # Request headers
##    'Host': 'vincentformtest.cognitiveservices.azure.com',
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '953e98b2fc6b46f1bbc8b9b0eac2bd6d',
#}
#'''
##GET
#'''
##headers = {
##    # Request headers
##    'Ocp-Apim-Subscription-Key': '953e98b2fc6b46f1bbc8b9b0eac2bd6d',
##}
#body = "{'urlSource': 'https://vincentstored.blob.core.windows.net/vincentform/LJ57247288-DE1-20230300017_%E8%81%AF%E5%BC%B7%E5%9C%8B%E9%9A%9B.pdf'}"
#
#global conn, response, res, resText
#try: #https://vincentformtest.cognitiveservices.azure.com/  eastasia.api.cognitive.microsoft.com
#    conn = http.client.HTTPSConnection('vincentformtest.cognitiveservices.azure.com')
#    conn.request("POST", "/formrecognizer/documentModels/prebuilt-invoice:analyze?api-version=2022-08-31", body , headers)
##    print(conn)
#    response = conn.getresponse()
#    data = response.getheaders()
##    print(data)
#    requestId = response.getheader('apim-request-id')
#    conn.close()
#    '''
#    #GET
#    '''
#    time.sleep(5)
#    conn = http.client.HTTPSConnection('vincentformtest.cognitiveservices.azure.com')
#    headers = { 'Ocp-Apim-Subscription-Key': '953e98b2fc6b46f1bbc8b9b0eac2bd6d' }
#    conn.request("GET", "/formrecognizer/documentModels/prebuilt-invoice/analyzeResults/"+requestId+"?api-version=2022-08-31", headers=headers)
#    
#    res = conn.getresponse()
#    resText = res.read().decode("utf-8")
#    print(resText[:500])
#    
#    
#except Exception as e:
#    print(e)

####################################
