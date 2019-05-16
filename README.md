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
•	**`sudo apt install python-pip                                                                                         
•	sudo pip3 install pillow pytesseract                                                                                    
•	sudo snap install sublime-text –classic                                                                             
•	pip install pytesseract                                                                               
•	sudo apt-get update                                                                                                     
•	sudo apt-get install python 3.6                                                                                             
•	sudo apt-get install imagemagick                                                                                
•	sudo pip install wand                                                                                                         
•	pip install langdetect                                                                                                            
•	pip install opencv-python                                                                                                   
•	sudo pip install python-dev                                                                                               
•	sudo pip install hashlib                                                                                          
•	pip install –upgrade setuptools                                                                                         
•	pip install pillow                                                                                                
•	apt-get install tesseract-ocr libtesseract –dev libleptonica-dev                                                                      
•	pip install tesserocr                                                                                                             
•	apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \ flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig                                                                                                
•	sudo apt-get install –y python python-dev                                                                                         
•	python-pip build-essential swig git libpulse-dev                                                                                       
•pip install sphinx                                                                                                     
•sudo apt-get install libasound2-dev                                                                                      
•pip install pocketsphinx                                                                                                          
•pip install textract                                                                                              
•	pip install pdfminer
•	pip install langdetect                                                                                                        
•	pip install pypdf2                                                                          
•	pip install docx2txt                                                                              
•	pip install pathlib`**                                                                            


In the end, you are going to be able to see these results below :

![sc3](https://user-images.githubusercontent.com/29866395/57735681-1af28800-76ae-11e9-8528-d1e04fd1651f.jpg)


# Possible Problems You Might Encounter and Links for Solutions
I deal with a few problems during coding (not to hard to come over) so I am also adding links that I've used,if you even still have a problem,you can reach me by e-mail or LinkedIn. Stay with Python!


https://askubuntu.com/questions/92379/how-do-i-get-permissions-to-edit-system-configuration-files                                 
https://askubuntu.com/questions/770262/python-hashlib-fails-to-install-pip                                                    
https://stackoverflow.com/questions/27850629/python-hachoir-metadata-reading-fps-tag-from-mp4-file/27859415                   
https://stackoverflow.com/questions/44435595/extract-pictures-from-word-and-excel-with-python                                   
https://stackoverflow.com/questions/21697645/how-to-extract-metadata-from-a-image-using-python                                        
https://stackoverflow.com/questions/39142778/python-how-to-determine-the-language                                                       
https://stackoverflow.com/questions/52699608/wand-policy-error-error-constitute-c-readimage-412                                     
https://stackoverflow.com/questions/53458606/using-tesseract-to-extract-text-and-pictures-photos-charts-and-tables-referen            
https://stackoverflow.com/questions/47133072/how-to-extract-images-from-a-scanned-pdf                                       
https://stackoverflow.com/questions/27850629/python-hachoir-metadata-reading-fps-tag-from-mp4-file/27859415                 
https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image                            
https://stackoverflow.com/questions/39142778/python-how-to-determine-the-language                                             
https://stackoverflow.com/questions/4969497/video-meta-data-using-python                                                  
https://stackoverflow.com/questions/44916890/converting-doc-to-pure-text-using-python                                         
https://stackoverflow.com/questions/27691678/finding-image-present-docx-file-using-python                                       

