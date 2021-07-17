#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:04:39 2021

@author: alan
"""

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from optparse import OptionParser
import smtplib
import sys
import urllib.request, urllib.parse, urllib.error
import base64
import os

client_id = "664990419712-gpdfa298nnk95b8mivog32hafda7g79v.apps.googleusercontent.com"
client_secret = "Yyj0Y6Un3lHO12XexQsl2K7c"
refresh_token = "1//05pKdpdNeAFWSCgYIARAAGAUSNwF-L9Ir8Dt9ngZEa298_6p4TLDKjx_DuBRzdDMx7mDZfxiefZshfWO-o4569GBzWq5H2IH71zo"
GOOGLE_ACCOUNTS_BASE_URL = 'https://accounts.google.com'


# Hardcoded dummy redirect URI for non-web apps.
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'


def AccountsUrl(command):
    """Generates the Google Accounts URL.
    
    Args:
      command: The command to execute.
    
    Returns:
      A URL for the given command.
    """
    return '%s/%s' % (GOOGLE_ACCOUNTS_BASE_URL, command)

def generate_oauth2_string(username, access_token, as_base64=False):
    auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
    if as_base64:
        auth_string = base64.b64encode(auth_string.encode('ascii')).decode('ascii')
    return auth_string 

def send (receiver, filename, folio, nombre ):
    # The URL root for accessing Google Accounts.

    params = {}
    params['client_id'] = client_id
    params['client_secret'] = client_secret
    params['refresh_token'] = refresh_token
    params['grant_type'] = 'refresh_token'
    request_url = AccountsUrl('o/oauth2/token')
    
    response = urllib.request.urlopen(request_url, urllib.parse.urlencode(params).encode("utf-8")).read()
    resp = json.loads(response)

    subject = "Resultados de Laboratorio, Paciente: {} {} ".format(folio,nombre)
    sender_email = "resultados@omedic.com.mx"
    receiver_email = receiver
    password = "NuevaContrasena2121."
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    html = """ <span style="font-size:small">--&nbsp;</span><br style="font-size:small"><div><div dir="ltr"><p style="font-size:12px;color:rgb(0,0,0);font-family:Helvetica"><b><span style="font-size:9pt;font-family:Arial,sans-serif;color:rgb(104,107,115)">OMEDIC</span><span style="font-size:9pt;font-family:Arial,sans-serif;color:rgb(104,107,115)">&nbsp;| El Valor de Un Diagnóstico Oportuno</span></b></p><p><b style="color:rgb(104,107,115);font-family:Arial,sans-serif;font-size:9pt">Oficina:</b><font face="Arial, sans-serif" color="#686b73"><span style="font-size:9pt">&nbsp;</span><span style="font-size:12px">(55) 8435 9546</span><span style="font-size:9pt">&nbsp;</span></font><b style="color:rgb(104,107,115);font-family:Arial,sans-serif;font-size:9pt">| WhatsApp:&nbsp;</b><font face="Arial, sans-serif" color="#686b73"><span style="font-size:12px">+52 1 55 6826 8367</span></font></p><p style="color:rgb(0,0,0);font-family:Helvetica;font-size:12px"></p><p style="font-size:12px;color:rgb(0,0,0);font-family:Helvetica"><b><font face="Arial, sans-serif" color="#1155cc"><span style="font-size:9pt"><a href="mailto:resultados@omedic.com.mx" target="_blank">resultados@omedic.com.mx</a></span></font><span style="color:rgb(104,107,115);font-family:Arial,sans-serif;font-size:9pt">&nbsp;</span><span style="color:rgb(104,107,115);font-family:Arial,sans-serif;font-size:9pt">|</span><span style="color:rgb(104,107,115);font-family:Arial,sans-serif;font-size:9pt">&nbsp;</span><a href="http://www.omedic.com.mx/" style="color:rgb(17,85,204);font-family:Arial,sans-serif;font-size:9pt" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://www.omedic.com.mx/&amp;source=gmail&amp;ust=1626561496977000&amp;usg=AFQjCNEor1sJQSr6wfIgLNbrUb7pEEEIsg">www<wbr>.omedic.com.mx</a></b><br></p><p style="font-size:12px;font-family:Helvetica"><font color="#444444"><b>¡Queremos seguir mejorando! Por favor ayúdanos con tu retroalimentación en nuestro perfil público:&nbsp;&nbsp;</b></font><a href="https://g.page/OmedicServiciosADomicilio/review?gm" style="font-family:Arial,Helvetica,sans-serif;font-size:small" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://g.page/OmedicServiciosADomicilio/review?gm&amp;source=gmail&amp;ust=1626561496977000&amp;usg=AFQjCNGQWX2I_eh3TZXfjlp67ObuSlN6XA">https://g.page/<wbr>OmedicServiciosADomicilio/<wbr>review?gm</a></p><div style="font-size:small"><b><br></b></div><div style="font-size:small"><b>En caso de solicitar factura por favor llena el siguiente formulario:&nbsp;</b> <a href="https://forms.gle/3CW5QKrGWDztPnYa8" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://forms.gle/3CW5QKrGWDztPnYa8&amp;source=gmail&amp;ust=1626561496977000&amp;usg=AFQjCNFA5DTsvPgPrc_PUN9riy9bw5u_Zg">https://forms.gle/<wbr>3CW5QKrGWDztPnYa8</a></div><div style="font-size:small"><br></div><div style="font-size:small"><img src="https://ci6.googleusercontent.com/proxy/pYoo1qCmSI4DsYgqJARKgcG2FAIHYKcKzQlYYEyfsWXyIrg8aUPMtC5bwbn6KkAzLaNk7-qGOJCHKIp7h9M4GUHqbW3wDZtijP3tbcMZohrKaJUl3gP5U58O4qYic3Lu55ZUJTUPO6xte6qtkUJFF4zRln__rEpQDiG7wR_6TZTaNpSazrsMZAxB_DDd-lpQEs5LVmzN9uYQP7I=s0-d-e1-ft#https://docs.google.com/uc?export=download&amp;id=0B-9KV8TCdfxlRTNTeFg4QW5IblE&amp;revid=0B-9KV8TCdfxlUGNUbk9jdWRxSVVpbDltK1AzRXZvWjhLZEhjPQ" class="CToWUd a6T" tabindex="0" width="200" height="135"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 152px; top: 370.267px;">"""
    
    signature = MIMEText(html, "html")
    
    # Add body to email
    message.attach(signature)
    
    filename = filename + '.pdf'
    # Open PDF file in binary mode
    with open( os.path.abspath(os.getcwd()) + "/membretados/" + filename , "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    
    # Log in to server using secure context and send email
    auth_string = generate_oauth2_string(sender_email, resp['access_token'], as_base64=True)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo(client_id)
    server.starttls()
    server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
    server.sendmail(sender_email, receiver, text)
    server.quit()
