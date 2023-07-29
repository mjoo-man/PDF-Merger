'''
My attempt at creating a pdf merger in python so that i can add engineering sheets to my hw files

Basic Operations:

-Hit run and select the files you want merged together
- the code will merge files in order of selection
- the merged file will appear in the same folder as the FIRST selected document
	with the same filename+'-merged' after it
'''
from PyPDF2 import PdfMerger, PdfReader
import os
import sys
##########################################################
# Code copied from File ops/getFilePath.py on 11-20-2021
from tkinter import filedialog as fd
from tkinter import Tk

# function will prompt the user to select a file and return its absolute path
def getFilePath(message):
	Tk().withdraw()
	filepath = fd.askopenfilename()
	return filepath
############################################################

merger = PdfMerger()

file = '0'
pdfs = []
while len(file) != 0: #run continuously to select all pdfs until nothing is selected

	file = getFilePath('Select file to Merge')
	if len(file) != 0:
		pdfs.append(file)

for pdf in  pdfs:
	merger.append(PdfReader(open(pdf, 'rb')))

#title the file after the first file picked and add merged
filename = os.path.basename(pdfs[0]).split(".")[0] + '-merged.pdf'
#set the working directory to the first file picked
savedir = os.path.dirname(pdfs[0])
os.chdir(savedir)
merger.write(filename)
merger.close()
