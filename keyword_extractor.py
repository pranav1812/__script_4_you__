# Script to Extract main keywords from text-pdf and text files such as to get idea of what is basically the file about.
# It prints the Keywords along with the occurence score.


# PyPDF2 deals with functions related to text-based pdfs
# Rake deals with extracting keywords based upon stoplist words.
# importing libraries
import RAKE as rake
import PyPDF2

print('Welcome to Summary Extractor...')

# Object of Rake being generated 
rake_object = rake.Rake("SmartStoplist.txt")

# Inputing the file from which keywords to be extracted
filename = input("Enter the path of your file: ")

# Extracting keywords from text-pdf files
if filename.endswith('.pdf'):
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print(pdfReader.numPages)
    # This statement is used to print number of pages in the pdf
    
    text = ""
    # loop through the pages of pdf and extracting keywords page by page
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        text = text + pageObj.extractText()
        # This extractText() function is used to extract information from the page we read in pdf using getPage()
   
    keywords = rake_object.run(text,5,3,4)
    print ("Keywords:", keywords)

# Extracting Keywords from text files
elif filename.endswith('.txt'):
    sample_file = open(filename,'r')
    text = sample_file.read()
    keywords = rake_object.run(text,5,3,4)
    print ("Keywords:", keywords)

# If file is neither pdf nor txt it will send this msg
else:
    print("File is neither pdf nor text")
# Script Ends