#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:55:39 2021

@author: alan
"""
#pip install PyPDF2

import PyPDF2
import glob
import cv2
import fitz
import re
from Downloader import *
import sys



####    Download files from Eli


download = Downloader()
download.getAttach()
w = 390
h = 125     

words = ["Paciente"]
img = open('Encabezado.jpg', "rb").read()
rect = fitz.Rect(0, 0, w, h)
docs = glob.glob('adjuntos/*.PDF')
for fname in docs:
        
        file_handle = fitz.open(fname)
        for pag in file_handle:
            pag.insertImage(rect, stream = img, keep_proportion=False)
            text = pag.getText("text")
            words = text.lower().split()
            try:
                name = ' '.join([str(elem) for elem in words[words.index('paciente')+2:words.index('resultado')]])
            except Exception:
                name = ' '.join([str(elem) for elem in words[words.index('paciente:')+1:words.index('resultado')]])
            file_handle.save('membretados/{}'.format(name) +'.pdf')  
        file_handle.close() 
        
        
            