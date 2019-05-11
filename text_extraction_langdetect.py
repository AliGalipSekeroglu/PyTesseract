
# ****************************** 1-TEXT EXTRACTION FROM PDF,DOC,XLSX,PNG,JPG FILES ******************************

import textract
from langdetect import detect
text1 = textract.process('sample2.docx', method='pdfminer') #DOC to Text
print(text1)

text2 = textract.process('sample.pdf',method='tesseract',language='eng') #PDF to Text
print(text2)

text3=textract.process('test2.xlsx',method='tesseract',language='eng') #XLS to Text
print(text3)

text4=textract.process('eurotext.tif',method='tesseract',language='heb') #PNG to Text
print(text4)
text5=textract.process('novel.jpg',method='tesseract',language='eng') #JPG to Text
print(text5)

# ****************************** 5-LANGUAGE DETECTION FOR THE GIVEN FILES ******************************

#Text donusumunu yaptiktan sonra bosluk kisimlarindan ayirip bir diziye attim,dizinin ilk 5 elemanini langdetect kutuphanesini kullanarak hangi dil oldugunu buldum.
#I created an empty list to put all these words into that,then I gave first 30 words to "detect" function to see the detected language.

dizi=[]
i=0
for i in text5.split():
	dizi.append(i)

string_dizi = str(dizi[0:30])

language_detection=detect(string_dizi)
print("Detected language is: ",language_detection)




"""
#PDF to Text

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename="sample.pdf",resolution=300)
pdfImg=pdf.convert("jpeg")

imgBlobs=[]

for img in pdfImg.sequence:
	page=wi(image= img)
	imgBlobs.append(page.make_blob('jpeg'))

extracted_text= []

for imgBlob in imgBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text= pytesseract.image_to_string(im,lang="eng")
	extracted_text.append(text)

for i in extracted_text:
	print(i)

"""


"""
#PNG to Text,JPEG to Text,TIF to Text

import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = "/home/aligalip/hazir"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread("photoimage.tif") #stoplogo.png,novel.jpg

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result

print ('--- Start recognize text from image ---')
print (get_string(src_path + "2.png"))
print ("------ Done -------")

"""

"""
# https://pypi.org/project/pytesseract/ web sitesindeki Quick Start kismindaki kodlari kullandim.

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#Simple image to string
print(pytesseract.image_to_string(Image.open('stop.gif')))

#print(pytesseract.image_to_string(Image.open('stop.gif'), lang='eng'))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('stop.gif')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('test.png')))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('novel.jpg')))

# In order to bypass the internal image conversions, just use relative or absolute image path
# NOTE: If you don't use supported images, tesseract will return error
print(pytesseract.image_to_string('test.png'))

# get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')

# get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')
"""