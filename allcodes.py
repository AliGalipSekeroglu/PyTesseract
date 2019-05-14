import textract
from langdetect import detect
import hashlib
import sys
import shutil
import os
import zipfile
from PyPDF2 import PdfFileReader
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset


# ****************************** 1-TEXT EXTRACTION FROM PDF,DOC,XLSX,PNG,JPG FILES ******************************

def ExtractTextFromFile(aFile,methodS,Lang):
  print '\ntrying extract from file...\n'
  extracted=textract.process(aFile, method=methodS,language=Lang)
  print extracted
  return extracted

# ****************************** 5-LANGUAGE DETECTION FOR THE GIVEN FILES ******************************

#Text donusumunu yaptiktan sonra bosluk kisimlarindan ayirip bir diziye attim,dizinin ilk 5 elemanini langdetect kutuphanesini kullanarak hangi dil oldugunu buldum.

def DetectLanguage(String):
  print '\ntry to detect language...\n'
  dizi=[]
  i=0
  for i in String.split():
	  dizi.append(i)

  string_dizi = str(dizi[0:30])

  language_detection=detect(string_dizi)
  print("Detected language is: ",language_detection)

# ******************************2.1 IMAGE EXTRACTION FROM PDF FILES ******************************
def ExtractImagePdf(aFile):
  print '\nextracting image from pdf...\n'
  pdf = file(aFile, "rb").read()

  startmark = "\xff\xd8"
  startfix = 0
  endmark = "\xff\xd9"
  endfix = 2
  i = 0

  njpg = 0
  while True:
    istream = pdf.find("stream", i)
    if istream < 0:
      break
    istart = pdf.find(startmark, istream, istream+20)
    if istart < 0:
      i = istream+20
      continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
      raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend-20)
    if iend < 0:
      raise Exception("Didn't find end of JPG!")
    
    istart += startfix
    iend += endfix
    print "JPG %d from %d to %d" % (njpg, istart, iend)
    jpg = pdf[istart:iend]
    jpgfile = file("jpg%d.jpg" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()
    
    njpg += 1
    i = iend

# ******************************2.2 IMAGE EXTRACTION FROM DOCX and XLSX FILES ******************************


def zipDoc(aFile,dirPath):
    dotNDX = aFile.index(".") # position of the .
    shortFN = aFile[:dotNDX] # name of the file before .
    zipName = dirPath + shortFN + ".zip" # name and path of the file only .zip
    shutil.copy2(dirPath + aFile, zipName) # copies all data from original into .zip format
    useZIP = zipfile.ZipFile(zipName) # the usable zip file
    return useZIP # returns the zipped file 

def hasPicExtension(aFile): # if a file ends in a typical picture file extension, returns true
    picEndings = [".jpeg",".jpg",".png",".bmp",".JPEG"".JPG",".BMP",".PNG","WMF"] # list of photo extensions
    if aFile.endswith(tuple(picEndings)): # turn the list into a tuple, because .endswith accepts that
        return True     
    else: # if it doesn't end in a picture extension
        return False

def delDOCXEvidence(somePath): # removes the .docx file structures generated
    ##################################################################
    # Working Linux code:
    os.rmdir(somePath + "/word/media") # removes directory
    os.rmdir(somePath + "/word") # removes more directory
    ##################################################################

    ##################################################################
    # Untested windows code:
    # os.rmdir(somePath + "\\\\word\\\\media") # removes directory
    # os.rmdir(somePath + "\\\\word") #removes more directory
    ##################################################################

def delXLSXEvidence(somePath): # removes the .xlsx file structures generated
    ##################################################################
    # Working Linux code:
    os.rmdir(somePath + "/xl/media") # removes directory
    os.rmdir(somePath + "/xl") # removes more directory
    ##################################################################

    ##################################################################
    # Untested windows code:
    # os.rmdir(somePath + "\\\\xl\\\\media") # removes directory
    # os.rmdir(somePath + "\\\\xl") #removes more directory
    ##################################################################

def extractPicsFromDir(dirPath=""):
    print '\nextracting images from dir..\n'
# when given a directory path, will extract all images from all .docx and .xlsx file types
    if os.path.isdir(dirPath): # if the given path is a directory
        for dirFile in os.listdir(dirPath): # loops through all files in the directory
            dirFileName = dirFile # strips out the file name
            if dirFileName.endswith(".docx"):
                useZIP = zipDoc(dirFile,dirPath) # turns it into a zip
                picNum = 1 # number of pictures in file
                for zippedFile in useZIP.namelist(): # loops through all files in the directory
                    if hasPicExtension(zippedFile): # if it ends with photo
                        print zippedFile
                        useZIP.extract(zippedFile, path=dirPath) # extracts the picture to the path + word/media/
                        shutil.move(dirPath + str(zippedFile),dirPath + dirFileName[:dirFileName.index(".")] + " - " + str(picNum)) # moves the picture out
                        picNum += 1
                #delDOCXEvidence(dirPath) # removes the extracted file structure
                #os.remove(useZIP.filename) # removes zip file
                # no evidence
            if dirFileName.endswith(".xlsx"):
                useZIP = zipDoc(dirFile,dirPath) # turns it into a zip
                picNum = 1 # number of pictures in file
                for zippedFile in useZIP.namelist(): # loops through all files in the directory
                    if hasPicExtension(zippedFile): # if it ends with photo
                        print zippedFile
                        useZIP.extract(zippedFile, path=dirPath) # extracts the picture to the path + word/media/
                        shutil.move(dirPath + str(zippedFile),dirPath + dirFileName[:dirFileName.index(".")] + " - " + str(picNum)) # moves the picture out
                        picNum += 1
                #delXLSXEvidence(dirPath) # removes the extracted file structure
                #os.remove(useZIP.filename) # removes zip file
                # no evidence

    else:
        print("Not a directory path!")
        exit(1)

# ****************************** 3.1-METADATA DETECTION FOR PDF FILES ******************************

def GetPdfMetadata(path):
    print '\nprinting metadata from pdf...\n'
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print info
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

# ****************************** 3.2-METADATA DETECTION FOR ALL FILES(EXCEPT PDFs) ******************************

def metadata_for(filename):
    print '\nprinting metadata...\n'

    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print ("Unable to parse file")
        exit(1)
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print ("Metadata extraction error: %s" % unicode(err))
        metadata = None
    if not metadata:
        print ("Unable to extract metadata")
        exit(1)

    text = metadata.exportPlaintext()
    charset = getTerminalCharset()
    for line in text:
      print makePrintable(line, charset)

    #print metadata

# ****************************** 4-HASH CODE GENERATOR ******************************


def HashMyFile(filename):
   print '\nHashing file...\n'
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   print h.hexdigest()


if __name__== "__main__":
  extractedText=ExtractTextFromFile('sample2.docx','pdfminer','eng') #text2 = textract.process('sample.pdf',method='tesseract',language='eng') #PDF to Text
  DetectLanguage(extractedText)
  ExtractImagePdf('sampleimage.pdf')
  extractPicsFromDir('/home/aligalip/project-tesseract-all/extracted_images/')
  GetPdfMetadata('sample.pdf')
  metadata_for('novel.jpg')
  HashMyFile("test2.xlsx")
