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


w = 350
h = 90  
words = ["Paciente"]
img = open('Encabezado.jpg', "rb").read()
rect = fitz.Rect(0, 0, w, h)
docs = glob.glob('*.PDF')
for fname in docs:
        file_handle = fitz.open(fname)
        for pag in file_handle:
            pag.insertImage(rect, stream = img)
            text = pag.getText("text")
            words = text.lower().split()
            name = ' '.join([str(elem) for elem in words[words.index('paciente')+2:words.index('resultado')]])
            file_handle.save(name +'.pdf'.format(fname))  
        file_handle.close() 
        
        
        