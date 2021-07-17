#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:55:39 2021

@author: alan
"""
#pip install PyPDF2
#pip install PyMuPDF
import PyPDF2
import glob
import cv2
import fitz
import re
from WebScraping import *
from Downloader import *
import sys



####    Download files from Eli


download = Downloader()
download.getAttach()
w = 390
h = 125
words = ["Paciente"]
pix = fitz.Pixmap("Encabezado.jpg") 
rect = fitz.Rect(0, 0, w, h)
docs = glob.glob('adjuntos/*.PDF')
for fname in docs:
        allWords = []
        file_handle = fitz.open(fname)
        for pag in file_handle:
            pag.insertImage(rect, pixmap = pix, keep_proportion=False)
            text = pag.getText("text")
            words = text.split()
            allWords += words
            edad = words[words.index('Edad') +  2]
            folio = words[words.index('Paciente') +2]
            name =   ' '.join([str(elem) for elem in words[words.index('Paciente')+3:words.index('RESULTADO')]])
            fileName = folio + '-' + name
            file_handle.save('membretados/' + fileName +'.pdf')  
        file_handle.close() 
        scrap = Scraping(folio, name, edad, allWords, fileName)
        scrap.validate()



