"""
@Author : Soham Naik
@Date: 06/02/2024
@Goal: To implement the Email Sending Application


This program is a simple Tkinter-based GUI application for sending emails.
It allows users to log in, register, compose emails with optional attachments, and send them.
The application utilizes the smtplib library for email sending, and the email.mime module for creating MIME messages.
User information is stored and validated during registration and login processes.

Note:
    1. Registration GUI Page just display the information on console.
    2. As checked, Login GUI Page is working properly.


Modules:
- smtplib: Provides the functionality to send emails using the Simple Mail Transfer Protocol (SMTP).
- email.mime.multipart: Defines the MIMEMultipart class for creating multipart email messages.
- email.mime.text: Defines the MIMEText class for adding plain text to email messages.
- email.mime.base: Defines the MIMEBase class for handling non-text file attachments.
- email.encoders: Provides functions for encoding and decoding email attachments.

Functions:
- OnAttachmentChecker: Update the state of the file button based on the attachment checkbox value.
- open_file_dialog: Open a file dialog to select a file and update the file path variable.
- OnMailClear: Clear the mail-related fields and reset states.
- main_send: Send the email message through the server.
- OnMailConfigure: Configure and send the email based on the provided information.
- mail_sending_page: Create and display the GUI for the email sending page.
- OnLogin: Handle the login process and transition to the email sending page.
- OnRegister: Handle the registration process and display a confirmation message.
- OnClear: Clear the registration-related fields.
- sign_up_page_func: Create and display the GUI for the sign-up page.
- sign_in_page_func: Create and display the GUI for the sign-in page.
- main_page: Create and display the main page GUI.
- root_window_func: Create and display the main Tkinter window.
- main: Entry point of the application.

"""


import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from tkinter import filedialog




def OnBackSignIn()->None:
    """
    Function to handle the 'Back' button click on the Sign In page.
    """
    login_page_frame.destroy()
    main_page()

def OnBackSignUp()->None:
    """
    Function to handle the 'Back' button click on the Sign Up page.
    """
    signup_page_frame.destroy()
    main_page()

def OnLogOut()->None:
    """
    Function to handle the 'Log Out' button click on the Mail Sending page.
    Closes the server connection and destroys the mail page.
    """
    mail_page_frame.destroy()
    main_page()
    
    

def login_authentication(server: object, sender_email: str, sender_password: str)->bool:
        """
        Authenticate the user by attempting to log in to the SMTP server.

        Parameters:
        - server: SMTP server object
        - sender_email: Email address of the sender
        - sender_password: Password for the sender's email account

        Returns:
        - True if login is successful, False otherwise
        """
        try:
            server.login(sender_email.strip(), sender_password.strip())
            print("Login Successfull!")
            return True
        except Exception as e:
            print(f"Authentication error occured:{e}")
            r = messagebox.askretrycancel(title=None, message="Authentication Error:" + str(e))
            login_btn['state'] = 'enabled'
            back_btn['state'] = 'enabled'
            progress.set("")
            server.quit()
            return False

def server_connection(sender_email: str, sender_password: str)->bool: 
    """
    Establish a connection to the SMTP server.

    Parameters:
    - sender_email: Email address of the sender
    - sender_password: Password for the sender's email account

    Returns:
    - True if the connection is successful, False otherwise
    """
    global server, login_result

    server = None
    login_result = None

    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        print("Server is created!")
        login_result = login_authentication(server, sender_email, sender_password) 
    except Exception as e:
        print(f"Connection error occured: {e}")
        r = messagebox.askretrycancel(title=None, message="Connection Error:" + str(e))
        login_btn['state'] = 'enabled'
        back_btn['state'] = 'enabled'
        progress.set("")
        server.quit()
        return False 

    if login_result == True:
        return True
    else:
        server.quit()
        return False

def is_Emailvalidate(sender_email: str)->bool:
        """
        Validate the format of an email address.

        Parameters:
        - sender_email: Email address to be validated

        Returns:
        - True if the email address is valid, False otherwise
        """

        if type(sender_email) != str:
            return False
        
        if sender_email == '':
            return False
        
        if ('@' or '.') not in sender_email:
            return False
        
        local, domain = sender_email.split('@', 1)

        if not local or not domain:
            return False
        
        if '.' not in domain:
            return False
        
        return True
    
def is_password(sender_password: str)->bool:
    """
    Validate the format of a password.

    Parameters:
    - sender_password: Password to be validated

    Returns:
    - True if the password is valid, False otherwise
    """

    if (
        sender_password == '' or 
        len(sender_password) < 5 or 
        type(sender_password) != str
    ):
        return False
        
    return True

def OnAttachmentChecker()->None:
    """
    Update the state of the file button based on the attachment checkbox value.

    If the attachment checkbox is set to 'Yes', enable the file button;
    otherwise, disable it.

    Returns:
    None
    """

    if attachment_checker.get() == 'Yes':
        file_btn['state'] = 'enabled' 
        file_path=""
    elif attachment_checker.get() == 'No':
        file_btn['state'] = 'disabled'
        file_path=""
        file_name.set("")

def open_file_dialog()->(str | None):
    """
    Open a file dialog to select a file and update the file path variable.

    This function uses the filedialog module to open a dialog for selecting a file.

    Returns:
    str or None: The selected file path or None if no file is selected.
    """

    global file_path, file_name
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("All files", "*.*"),) #("Text files", "*.txt"), 
    )
    # Display the selected file path or perform further actions
    if file_path:
        print(f"Selected file: {file_path}")
        file_name_temp = file_path.split("/")
        file_name_temp = file_name_temp[len(file_name_temp)-1]
        file_name.set(str(str(file_name_temp)+ str(" is attached.")))
        return file_path
    else:
        return None

def OnMailClear()->None:
    """
    Clear the mail-related fields and reset states.

    This function clears the receiver email, mail subject, mail body, and attachment-related information.

    Returns:
    None
    """
    global file_btn,receiver_email,mail_subject,mail_body,file_path,attachment_checker,server
    receiver_email.set("")
    mail_subject.set("")
    mail_body.delete("1.0",END)
    attachment_checker.set("")
    file_path = ""
    file_name.set("")
    file_btn['state'] = 'disabled' 

def main_send(message:object)->None:
    """
    Send the email message through the server.

    Parameters:
    - message (MIMEMultipart): The email message to be sent.

    This function uses the `server.send_message` method to send the email through the configured server.
    It handles exceptions during the sending process and displays appropriate messages.

    Raises:
    Exception: If there is an error during the email sending process.

    Returns:
    None
    """
    try:
        server.send_message(message)     
        print("Message sent successfully!")
        r = messagebox.askokcancel(title="INFO", message="Mail Send Successfully!!")
        server.quit()
        send_btn['state'] = 'enabled'
        clear_btn['state'] = 'enabled'
    except Exception as e:
        r = messagebox.askretrycancel(title="Error", message="Connection Error:" + str(e))
        send_btn['state'] = 'enabled'
        clear_btn['state'] = 'enabled' 

def OnMailConfigure()->None:
    """
    Configure and send the email based on the provided information.

    This function validates the receiver email, mail subject, and mail body.
    It uses the `MIMEMultipart` class to create an email message and attaches the file (if specified).

    If the email configuration is successful, it calls the `main_send` function to send the email.

    Raises:
    Exception: If there is an error during the email configuration or sending process.

    Returns:
    None
    """
    global file_btn,receiver_email,mail_subject,mail_body,file_path,attachment_checker,server

    send_btn['state'] = 'disabled'
    clear_btn['state'] = 'disabled'

    receiver_address = receiver_email.get().strip()
    mail_subject_value = mail_subject.get().strip()
    mail_body_text = mail_body.get("1.0", END)

    message = MIMEMultipart()
    receiver_result = is_Emailvalidate(receiver_address)
    if receiver_result == True:
        message['From'] = sender_email
        message['To'] = receiver_address
        if mail_subject_value != '':
            message['Subject'] = mail_subject_value
            if mail_body_text != '' and len(mail_body_text) > 1:
                text_body = MIMEText(mail_body_text, 'plain')
                message.attach(text_body)
                if attachment_checker.get() == 'Yes' and file_path != '':
                    try:
                        file_object = MIMEBase('application', 'octect-stream')
                        file_handle = open(file_path, 'rb')
                        file_object.set_payload((file_handle).read())
                        encoders.encode_base64(file_object)

                        file_name = file_path.split("/")
                        file_name = file_name[len(file_name)-1]
                        file_object.add_header('Content-Disposition', 'attachment', filename = file_name)
                        message.attach(file_object)
                        main_send(message)
                    except Exception as e:
                        print(f"Error: {e}")
                        r = messagebox.askretrycancel(title=None, message="File Error:" + str(e))
                        send_btn['state'] = 'enabled'
                        clear_btn['state'] = 'enabled'
                elif attachment_checker.get() == 'Yes' and file_path == '':
                        r = messagebox.askretrycancel(title=None, message="Please select the file")
                        send_btn['state'] = 'enabled'
                        clear_btn['state'] = 'enabled'
                elif attachment_checker.get() != "Yes":
                    main_send(message)
                 
            else:
                r = messagebox.askretrycancel(title="Invalid input", message="Please check mail body!")               
                send_btn['state'] = 'enabled'
                clear_btn['state'] = 'enabled'
        else:           
            r = messagebox.askretrycancel(title="Invalid input", message="Please check mail subject!")    
            send_btn['state'] = 'enabled'
            clear_btn['state'] = 'enabled'
    else:
        r = messagebox.askretrycancel(title="Invalid input", message="Please check receiver email address!")   
        send_btn['state'] = 'enabled'
        clear_btn['state'] = 'enabled'


def mail_sending_page()->None:
    """
    Create and display the GUI for the email sending page.

    This function configures the GUI elements using the `ttk` module and binds functions to various buttons.
    It creates an instance of the `MIMEMultipart` class for constructing the email message.

    Returns:
    None
    """
    global attachment_checker, file_btn,receiver_email,mail_subject,mail_body,send_btn,clear_btn,file_name,file_path,mail_page_frame
    login_page_frame.destroy()

    root_window.geometry("800x750")

    style = ttk.Style()
    style.configure('TMailPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
    style.configure('TMailPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
    style.configure('TMailButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TMailLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TMailButton.TRadiobutton', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TMailButton.TCheckbutton', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TMailEntry.TEntry', font=('Times', 14), background='white', height=5)
    
    mail_page_frame = ttk.Frame(root_window, padding='3 3 12 12', relief='raised', borderwidth=10)
    mail_page_frame.grid(row=1, column=1)
    mail_page_frame.configure(style='TMailPage.TFrame')
    mail_page_frame.rowconfigure(1, weight=1)
    mail_page_frame.columnconfigure(1, weight=1)

    mail_title_label = ttk.Label(mail_page_frame, text="Mail Sending Box")
    mail_title_label.grid(row=1, column=2, sticky=(W,E))
    mail_title_label.configure(style='TMailPageTitle.TLabel')

    mail_list = []
    mail_label_txt = ['Enter Recevier Email:', 'Enter Email Subject:', 'Enter Email Body:']
    for i in range(3):
        mail_var = ttk.Label(mail_page_frame, text=mail_label_txt[i])
        mail_var.grid(row=i+2, column=1, sticky=(W,E,N))
        mail_var.configure(style='TMailLabel.TLabel')
        mail_list.append(mail_var)
    
    mail_receiver_label, mail_subject_label, mail_body_label = mail_label_txt
    #for i in range()

    receiver_email = StringVar()
    receiver_email_entry = ttk.Entry(mail_page_frame, textvariable=receiver_email, width=40)
    receiver_email_entry.grid(row=2, column=2, sticky=(W,E))
    receiver_email_entry.configure(font=('Times', 14))

    mail_subject = StringVar()
    mail_subject_entry = ttk.Entry(mail_page_frame, textvariable=mail_subject, width=40)
    mail_subject_entry.grid(row=3, column=2, sticky=(W,E))
    mail_subject_entry.configure(font=('Times', 14))

    mail_body = Text(mail_page_frame, wrap=WORD, width=40, height=10)
    mail_body.grid(row=4, column=2, sticky=(W, E))
    mail_body.configure(font=('Times', 14))

    attachment_checker = StringVar()
    attachment_checker_label = ttk.Checkbutton(
        mail_page_frame, 
        text="Do you want to attach any file or image?", 
        variable=attachment_checker, 
        onvalue="Yes", 
        offvalue="No",
        style='TMailButton.TCheckbutton',
        command=OnAttachmentChecker
        )
    attachment_checker_label.grid(row=5, column=1, sticky=(W,E))
   
    file_name = StringVar()
    file_path = ''
    file_btn = ttk.Button(mail_page_frame, state=DISABLED)
    file_btn.configure(text='+', style='TMailButton.TButton', command=open_file_dialog)
    file_btn.grid(row=5, column=2, sticky=(W,E))
 
    file_name_label = ttk.Label(mail_page_frame, textvariable=file_name)
    file_name_label.grid(row=6,column=1, sticky=(W, E))
    file_name_label.configure(style='TMailLabel.TLabel')

    send_btn = ttk.Button(mail_page_frame)
    send_btn.configure(text='Send Mail', style='TMailButton.TButton', command=OnMailConfigure)
    send_btn.grid(row=7, column=1, sticky=(W,E))

    clear_btn = ttk.Button(mail_page_frame)
    clear_btn.configure(text='Clear', style='TMailButton.TButton', command=OnMailClear)
    clear_btn.grid(row=7, column=2, sticky=(W,E))

    logout_btn = ttk.Button(mail_page_frame)
    logout_btn.configure(text='Log Out', style='TMailButton.TButton', command=OnLogOut)
    logout_btn.grid(row=8, column=1, sticky=(W,E))

    exit_btn = ttk.Button(mail_page_frame)
    exit_btn.grid(row=8, column=2, sticky=(W,E))
    exit_btn.configure(text='Exit', style='TMailButton.TButton', command=lambda : sys.exit(0))

    #mail_page_frame.bind("<Return>", OnMailConfigure)
    receiver_email_entry.focus()

    for widget in mail_page_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)




def OnLogin(*args)->None:
    """
    Handle the login process and transition to the email sending page.

    This function validates the entered email and password.
    If the validation is successful, it attempts to establish a connection using `server_connection`.
    If the login is successful, it enables the login and back buttons and transitions to the email sending page.

    Raises:
    Exception: If there is an error during the login process.

    Returns:
    None
    """
    global sender_email, sender_password, login_btn, back_btn
    login_btn['state'] = 'disabled'
    back_btn['state'] = 'disabled'
    progress.set("Please wait...!")
    root_window.update()
    sender_email = lgn_email.get().strip()
    sender_password = lgn_password.get().strip()

    email_result = is_Emailvalidate(sender_email)
    password_result = is_password(sender_password)
    
    if(email_result == True and password_result == True):
        login = server_connection(sender_email, sender_password)
        if login == True:
            login_btn['state'] = 'enabled'
            back_btn['state'] = 'enabled'
            root_window.update()
            mail_sending_page()
        else:
            print("Failed!")
            messagebox.askretrycancel(title="Error", message="Connection Error!")

    elif(email_result==True and password_result == False):
        r = messagebox.askretrycancel(title="Invalid input", message="Wrong password!")
        login_btn['state'] = 'enabled'
        back_btn['state'] = 'enabled'
        progress.set("")
    elif(email_result==False and password_result == True):
        r = messagebox.askretrycancel(title="Invalid input", message="Wrong email id!")
        login_btn['state'] = 'enabled'
        back_btn['state'] = 'enabled'
        progress.set("")
    else:
        r = messagebox.askretrycancel(title="Invalid input", message="Please check email id and password!")
        login_btn['state'] = 'enabled'
        back_btn['state'] = 'enabled'
        progress.set("")

def OnRegister(*args)->None:
    """
    Handle the registration process and display a confirmation message.

    This function gathers user registration information, performs basic validation, and displays a confirmation message.

    Returns:
    None
    """
    print(reg_name.get(),"\n",
    reg_email.get(),"\n",
    reg_mobile.get(),"\n",
    reg_age.get(),"\n",
    reg_password.get(),"\n",
    reg_repassword.get(),"\n",
    gender_select_var.get(),"\n")
    r = messagebox.askokcancel(title="INFO", message="Registration is done!")
    OnClear()

def OnClear()->None:
    """
    Clear the registration-related fields.

    This function clears the registration form fields.

    Returns:
    None
    """
    reg_name.set('') 
    reg_email.set('')
    reg_mobile.set('')
    reg_age.set('')
    reg_password.set('')
    reg_repassword.set('')
    gender_select_var.set('')

def sign_up_page_func()->None:
    """
    Create and display the GUI for the sign-up page.

    This function configures the GUI elements using the `ttk` module and binds functions to various buttons.

    Returns:
    None
    """

    global reg_name, reg_email, reg_mobile, reg_age, reg_password, reg_repassword, gender_select_var, signup_page_frame

    
    main_page_frame.destroy()
    root_window.geometry("700x600")

    style = ttk.Style()
    style.configure('TSignUpPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
    style.configure('TSignUpPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
    style.configure('TSignUpButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TSignUpLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TSignUpButton.TRadiobutton', font=('Times', 14), justify='center', background='#BEB1AE')
    
    signup_page_frame = ttk.Frame(root_window, padding='3 3 12 12', relief='raised', borderwidth=10)
    signup_page_frame.grid(row=1, column=1)
    signup_page_frame.configure(style='TSignUpPage.TFrame')
    signup_page_frame.rowconfigure(1, weight=1)
    signup_page_frame.columnconfigure(1, weight=1)

    register_title_label = ttk.Label(signup_page_frame, text="Registration")
    register_title_label.grid(row=1, column=2, sticky=(W,E))
    register_title_label.configure(style='TSignUpPageTitle.TLabel')

    reg_list = []
    registration_txt = ['Enter Name:', 'Enter Email:', 'Enter Mobile no:', 'Enter Age:']
    for i in range(4):
        reg_var = ttk.Label(signup_page_frame, text=registration_txt[i])
        reg_var.grid(row=i+2, column=1, sticky=(W,E))
        reg_var.configure(style='TSignUpLabel.TLabel')
        reg_list.append(reg_var)
    
    reg_name_label, reg_email_label, reg_mobile_label, reg_age_label = reg_list
    #for i in range()

    reg_name = StringVar()
   
    reg_name_entry = ttk.Entry(signup_page_frame, textvariable=reg_name, width=30)
    reg_name_entry.grid(row=2, column=2, sticky=(W,E))
    reg_name_entry.configure(font=('Times', 14))

    reg_email = StringVar()
    reg_email_entry = ttk.Entry(signup_page_frame, textvariable=reg_email, width=30)
    reg_email_entry.grid(row=3, column=2, sticky=(W,E))
    reg_email_entry.configure(font=('Times', 14))

    
    reg_mobile = StringVar()
    reg_mobile_entry = ttk.Entry(signup_page_frame, textvariable=reg_mobile, width=30)
    reg_mobile_entry.grid(row=4, column=2, sticky=(W,E))
    reg_mobile_entry.configure(font=('Times', 14))

    
    reg_age = IntVar()
    reg_age_entry = ttk.Entry(signup_page_frame, textvariable=reg_age, width=30)
    reg_age_entry.grid(row=5, column=2, sticky=(W,E))
    reg_age_entry.configure(font=('Times', 14))

    gender_select_var = StringVar()
    gender_male_btn = ttk.Radiobutton(signup_page_frame, variable=gender_select_var, text='Male', value='Male', style='TSignUpButton.TRadiobutton')
    gender_male_btn.grid(row=6, column=1, sticky=(W,E))

    gender_female_btn = ttk.Radiobutton(signup_page_frame, variable=gender_select_var, text='Female', value='Female', style='TSignUpButton.TRadiobutton')
    gender_female_btn.grid(row=6, column=2, sticky=(W,E))

    reg_password = StringVar()
    reg_password_label = ttk.Label(signup_page_frame, text='Enter Password:', )
    reg_password_label.grid(row=7, column=1, sticky=(W,E))
    reg_password_label.configure(style='TSignUpLabel.TLabel')
    reg_password_entry = ttk.Entry(signup_page_frame, textvariable=reg_password, width=30)
    reg_password_entry.grid(row=7, column=2, sticky=(W,E))
    reg_password_entry.configure(font=('Times', 14))

    reg_repassword = StringVar()
    reg_repassword_label = ttk.Label(signup_page_frame, text='Re-Enter Password:', )
    reg_repassword_label.grid(row=8, column=1, sticky=(W,E))
    reg_repassword_label.configure(style='TSignUpLabel.TLabel')
    reg_repassword_entry = ttk.Entry(signup_page_frame, textvariable=reg_repassword, width=30)
    reg_repassword_entry.grid(row=8, column=2, sticky=(W,E))
    reg_repassword_entry.configure(font=('Times', 14))

    register_btn = ttk.Button(signup_page_frame, width=30)
    register_btn.configure(text='Register', style='TSignUpButton.TButton', command=OnRegister)
    register_btn.grid(row=9, column=1, sticky=(W,E))

    clear_btn = ttk.Button(signup_page_frame)
    clear_btn.configure(text='Clear', style='TSignUpButton.TButton', command=OnClear)
    clear_btn.grid(row=9, column=2, sticky=(W,E))

    back_btn = ttk.Button(signup_page_frame)
    back_btn.configure(text='Back', style='TSignUpButton.TButton', command=OnBackSignUp)
    back_btn.grid(row=10, column=1, sticky=(W,E))

    reg_name_entry.focus()
    root_window.bind("<Return>", OnRegister)

    for widget in signup_page_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)



def sign_in_page_func()->None:
    """
    Create and display the GUI for the sign-in page.

    This function configures the GUI elements using the `ttk` module and binds functions to various buttons.

    Returns:
    None
    """
    global lgn_email, lgn_password,login_page_frame,login_btn,back_btn,progress

    main_page_frame.destroy()
    root_window.geometry("600x500")

    style = ttk.Style()
    style.configure('TLoginPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
    style.configure('TLoginPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
    style.configure('TLoginButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TLoginLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
    style.configure('TProgressLabel.TLabel', font=('Times',12), justify='center', background='#BEB1AE')
    
    login_page_frame = ttk.Frame(root_window, padding='3 3 12 12', relief='raised', borderwidth=10)
    login_page_frame.grid(row=1, column=1)
    login_page_frame.configure(style='TLoginPage.TFrame')
    login_page_frame.rowconfigure(1, weight=1)
    login_page_frame.columnconfigure(1, weight=1)

    login_page_title = ttk.Label(login_page_frame, text='Login')
    login_page_title.grid(row=1, column=2, sticky=(W,E,N,S))
    login_page_title.configure(style='TLoginPageTitle.TLabel')
    
    
    login_txt = ['Email', 'Password']
    login_label = []
    lgn_email = StringVar()
    lgn_password = StringVar()

    for i in range(2):
        login_var = ttk.Label(login_page_frame, text=login_txt[i])
        login_var.grid(row=i+2, column=1, sticky=(W,E))
        login_var.configure(style='TLoginLabel.TLabel')
        login_label.append(login_var)
    email_label, password_label = login_label
   
    email_entry = ttk.Entry(login_page_frame, textvariable=lgn_email, width=30)
    email_entry.grid(row=2, column=2, sticky=(W,E))
    email_entry.configure(font=('Times', 14))

    password_entry = ttk.Entry(login_page_frame, show='*', textvariable=lgn_password, width=30)
    password_entry.grid(row=3, column=2, sticky=(W,E))
    password_entry.configure(font=('Times', 14))

    login_btn = ttk.Button(login_page_frame)
    login_btn.configure(text='Login', style='TLoginButton.TButton', command=OnLogin)
    login_btn.grid(row=4, column=2, sticky=(W,E))

    back_btn = ttk.Button(login_page_frame)
    back_btn.configure(text='Back', style='TLoginButton.TButton', command=OnBackSignIn)
    back_btn.grid(row=4, column=1, sticky=(W,E))

    progress = StringVar()
    progress.set("")
    progress_label = ttk.Label(login_page_frame, textvariable=progress)
    progress_label.grid(row=5,column=1, sticky=(W, E))
    progress_label.configure(style='TProgressLabel.TLabel')

    email_entry.focus()
    root_window.bind("<Return>", OnLogin)

    for widget in login_page_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)
#---

def main_page()->None:
    """
    Create and display the main page GUI.

    This function configures the GUI elements using the `ttk` module and binds functions to various buttons.

    Returns:
    None
    """
    global main_page_frame

    try:

        root_window.geometry('600x500')

        style = ttk.Style()
        style.configure('TMainPage.TFrame', font=('Times', 20, 'bold'), justify='center', background='#BEB1AE')
        style.configure('TMainPageTitle.TLabel', font=('Times', 30, 'bold'), justify='center', background='#BEB1AE' )
        style.configure('TSignUp.TButton', font=('Times', 26), justify='center', background='#BEB1AE')
        

        main_page_frame = ttk.Frame(root_window, padding='3 3 12 12', relief='raised', borderwidth=10)
        main_page_frame.grid(row=1, column=1)
        main_page_frame.configure(style='TMainPage.TFrame')
        main_page_frame.rowconfigure(1, weight=1)
        main_page_frame.columnconfigure(1, weight=1)

        main_page_title = ttk.Label(main_page_frame, text='Email Sending Application')
        main_page_title.grid(row=1, column=1, sticky=(W,E,N,S), pady='0 5')
        main_page_title.configure(style='TMainPageTitle.TLabel')
        
        SignUp_btn = ttk.Button(main_page_frame)
        SignUp_btn.configure(text='Sign Up', style='TSignUp.TButton', command=sign_up_page_func)
        SignUp_btn.grid(row=2, column=1, sticky=(W,E,N,S))


        SignIn_btn = ttk.Button(main_page_frame)
        SignIn_btn.configure(text='Sign In', style='TSignUp.TButton', command=sign_in_page_func)
        SignIn_btn.grid(row=3, column=1, sticky=(W,E,N,S))


        for widget in main_page_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    except Exception as e:
        messagebox.askokcancel(title="Error", message=e)
        sys.exit(-1)



def root_window_func()->None:
    """
    Create and display the main Tkinter window.

    This function configures the main window title, icon, and size.
    It sets up the main loop for the Tkinter application.

    Returns:
    None
    """
    global root_window
    try:
        root_window = Tk()
        root_window.title("Email Sending Application")
        root_window.iconbitmap("logo1.ico")
        root_window.geometry('600x500')
        root_window.config(bg='#F0F0F0')
        root_window.rowconfigure(1, weight=1)
        root_window.columnconfigure(1, weight=1)
        main_page()
        root_window.mainloop()
    except Exception as e:
        messagebox.askokcancel(title="Error", message=e)
        sys.exit(-1)
    
def main()->None:
    """
    Entry point of the application.

    This function calls the `root_window_func` to start the Tkinter application.

    Returns:
    None
    """
    root_window_func()


try:
    main()
except Exception as e:
    """
    Handle any unexpected exceptions during application execution.

    If an exception occurs, display an error message and exit the application.
    """
    messagebox.askokcancel(title="Error", message=e)
    sys.exit(-1) 