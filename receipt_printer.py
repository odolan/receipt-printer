from subprocess import Popen
import subprocess
import os
import io


#prints out inputed text
def print_text(text):
   correct_printer = 'EPSON_TM_T20II'
   printerControl = os.popen('lpr -P %s' % (correct_printer), 'w')
   printerControl.write(text)
   printerControl.close()

#prints out inputed image
def print_image(img_path):
   #connect and print image on printer
   with open(img_path) as f:
       # call the system's lpr command
       correct_printer = 'EPSON_TM_T20II'
       Popen(['lpr -P %s' % (correct_printer)], stdin=f, shell=True)  # not sure you need shell=True for a simple command
