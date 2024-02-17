from tkinter import *
from tkinter import ttk
import sys
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import filedialog

"""
Modules:
- smtplib: Provides the functionality to send emails using the Simple Mail Transfer Protocol (SMTP).
- email.mime.multipart: Defines the MIMEMultipart class for creating multipart email messages.
- email.mime.text: Defines the MIMEText class for adding plain text to email messages.
- email.mime.base: Defines the MIMEBase class for handling non-text file attachments.
- email.encoders: Provides functions for encoding and decoding email attachments.
- filedialog: The filedialog module in tkinter provides functions for creating file dialog windows, 
              allowing users to select files or directories from their system.
- messagebox: The messagebox module in tkinter provides a set of functions for creating message boxes or dialog boxes 
              to display various types of messages or prompts to the user.
- sys: The sys module provides access to some variables used or maintained by the Python interpreter 
       and to functions that interact strongly with the interpreter.
- tkinter: The tkinter module is Python's standard GUI (Graphical User Interface) package. 
           It provides various tools and widgets for creating graphical applications and interfaces.
              
"""