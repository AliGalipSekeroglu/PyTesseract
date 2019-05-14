# PyTesseract
Language detection,extract text and images from DOCX,XLSX,PDF,JPEG,PNG,BMP and GIF files through PyTesseract. This repository also includes calculating hash and metadata of a given file.I've developed this project on Linux Ubuntu 18.04,through Python 2.7 version which already comes with Ubuntu. You can also get the codes for text extraction through OpenCV as a comment under the given Python codes.

You can get more details about Google's Tesseract project here :                                                                      
**`https://opensource.google.com/projects/tesseract`**

There are 2 screenshots of the project,you can either use terminal to see the results or Python codes to do what you need from this project such as detecting the given file's language, extracting the text and so on.

![sc2](https://user-images.githubusercontent.com/29866395/57572445-19f9f600-7423-11e9-8f8a-53c9fe2a6366.jpg)

![sc1](https://user-images.githubusercontent.com/29866395/57572440-064e8f80-7423-11e9-877b-f2c488c2c694.jpg)



# How to Setup Tesseract

This part will take long a bit due to many dependencies of Tesseract. First of all, I am going to give you another Github page that you can find detailed explanations in terms of your OS:                                                                                                                                                                                                           
**`https://github.com/tesseract-ocr`**                                                                            
**`https://github.com/tesseract-ocr/tesseract/wiki/Compiling`**                                                         

When you open **`tesseract-ocr`** page,you will get a few trained language models named **`tessdata_fast`**  or **`tessdata_best.`**. I've used **`tessdata_fast`** due to have less space that I have so you can decide which one you would like to use.                             

I strongly recommend you to follow instructions to setup Tesseract to your OS by following second link that I shared(/wiki/Compiling).     
There are also video representations of the compiling for Tesseract and Leptonica on Ubuntu,you can easily get your first results from terminal.

After all dependencies that you will finish after following instructions, you must also get all these (Linux Ubuntu users) below:     

