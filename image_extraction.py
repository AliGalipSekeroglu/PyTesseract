"""
# ******************************2.1 IMAGE EXTRACTION FROM PDF FILES ******************************

from PyPDF2 import PdfFileReader
pdf = file("sampleimage.pdf", "rb").read()

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
"""


"""
# ******************************2.2 IMAGE EXTRACTION FROM DOCX and XLSX FILES ******************************

import shutil
import os
import zipfile

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
# when given a directory path, will extract all images from all .docx and .xlsx file types
    if os.path.isdir(dirPath): # if the given path is a directory
        for dirFile in os.listdir(dirPath): # loops through all files in the directory
            dirFileName = dirFile # strips out the file name
            if dirFileName.endswith(".docx"):
                useZIP = zipDoc(dirFile,dirPath) # turns it into a zip
                picNum = 1 # number of pictures in file
                for zippedFile in useZIP.namelist(): # loops through all files in the directory
                    if hasPicExtension(zippedFile): # if it ends with photo
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
                        useZIP.extract(zippedFile, path=dirPath) # extracts the picture to the path + word/media/
                        shutil.move(dirPath + str(zippedFile),dirPath + dirFileName[:dirFileName.index(".")] + " - " + str(picNum)) # moves the picture out
                        picNum += 1
                #delXLSXEvidence(dirPath) # removes the extracted file structure
                #os.remove(useZIP.filename) # removes zip file
                # no evidence

    else:
        print("Not a directory path!")
        exit(1)

uDir = 'home/aligalip/project-tesseract-all/exracted_images'
extractPicsFromDir(uDir)

"""
