
# ****************************** 3.1-METADATA DETECTION FOR ALL FILES(EXCEPT PDFs) ******************************

from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
def metadata_for(filename):

    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print "Unable to parse file"
        exit(1)
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print "Metadata extraction error: %s" % unicode(err)
        metadata = None
    if not metadata:
        print "Unable to extract metadata"
        exit(1)

    text = metadata.exportPlaintext()
    charset = getTerminalCharset()
    #for line in text:
        #print makePrintable(line, charset)

    return metadata

pathname = "/home/aligalip/project-tesseract-all/novel.jpg"
meta = metadata_for(pathname)
print meta




"""
# ****************************** 3.2-METADATA DETECTION FOR PDF FILES ******************************


from PyPDF2 import PdfFileReader
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(info)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

if __name__ == '__main__':
    path = 'sample.pdf'
    get_info(path)

"""