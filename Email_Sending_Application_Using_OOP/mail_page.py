from HeaderFile import *

class MailPageWindow():
    """
    This class represents the mail sending page window of the email sending application.
    It allows users to compose and send emails with attachments.

    Parameters:
    - win_top: The parent window where the mail page will be displayed.
    - server: The SMTP server object used for sending emails.
    - sender_email: The email address of the sender.
    - sender_password: The password of the sender's email account.

    Functions:
    - __init__: Initializes the MailPageWindow object.
    - OnAttachmentChecker: Enables or disables the file selection button.
    - open_file_dialog: Opens a file dialog window to select an attachment file.
    - main_send: Sends the email message using the SMTP server.
    - is_Emailvalidate: Validates the format of an email address.
    - OnMailConfigure: Constructs and sends the email message based on user input.
    - OnMailClear: Clears all input fields on the mail page.
    - OnLogOut: Logs out the user and returns to the front page window.
    - OnExit: Exits the application gracefully.
    - mainloop: Enters the Tkinter main event loop.
    """
    def __init__(self: object, win_top, server, sender_email, sender_password) -> None:
        """
        Initializes the MailPageWindow object.

        Parameters:
        - win_top: The parent window where the mail page will be displayed.
        - server: The SMTP server object used for sending emails.
        - sender_email: The email address of the sender.
        - sender_password: The password of the sender's email account.
        """
        
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.server = server
        self.win_top = win_top
        self.win_top.geometry("800x700")

        self.style = ttk.Style()
        self.style.configure('TMailPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
        self.style.configure('TMailPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
        self.style.configure('TMailButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TMailLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TMailButton.TRadiobutton', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TMailButton.TCheckbutton', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TMailEntry.TEntry', font=('Times', 14), background='white', height=5)
        
        self.mail_page_frame = ttk.Frame(self.win_top, padding='3 3 12 12', relief='raised', borderwidth=10)
        self.mail_page_frame.grid(row=1, column=1)
        self.mail_page_frame.configure(style='TMailPage.TFrame')
        self.mail_page_frame.rowconfigure(1, weight=1)
        self.mail_page_frame.columnconfigure(1, weight=1)

        self.mail_title_label = ttk.Label(self.mail_page_frame, text="Mail Sending Box")
        self.mail_title_label.grid(row=1, column=2, sticky=(W,E))
        self.mail_title_label.configure(style='TMailPageTitle.TLabel')

        self.mail_list = []
        self.mail_label_txt = ['Enter Recevier Email:', 'Enter Email Subject:', 'Enter Email Body:']
        for i in range(3):
            self.mail_var = ttk.Label(self.mail_page_frame, text=self.mail_label_txt[i])
            self.mail_var.grid(row=i+2, column=1, sticky=(W,E,N))
            self.mail_var.configure(style='TMailLabel.TLabel')
            self.mail_list.append(self.mail_var)
        
        self.mail_receiver_label, self.mail_subject_label, self.mail_body_label = self.mail_label_txt
        #for i in range()

        self.receiver_email = StringVar()
        self.receiver_email_entry = ttk.Entry(self.mail_page_frame, textvariable=self.receiver_email, width=40)
        self.receiver_email_entry.grid(row=2, column=2, sticky=(W,E))
        self.receiver_email_entry.configure(font=('Times', 14))

        self.mail_subject = StringVar()
        self.mail_subject_entry = ttk.Entry(self.mail_page_frame, textvariable=self.mail_subject, width=40)
        self.mail_subject_entry.grid(row=3, column=2, sticky=(W,E))
        self.mail_subject_entry.configure(font=('Times', 14))

        self.mail_body = Text(self.mail_page_frame, wrap=WORD, width=40, height=10)
        self.mail_body.grid(row=4, column=2, sticky=(W, E))
        self.mail_body.configure(font=('Times', 14))

        self.attachment_checker = StringVar()
        self.attachment_checker_label = ttk.Checkbutton(
            self.mail_page_frame, 
            text="Do you want to attach any file or image?", 
            variable=self.attachment_checker, 
            onvalue="Yes", 
            offvalue="No",
            style='TMailButton.TCheckbutton',
            command=self.OnAttachmentChecker
            )
        self.attachment_checker_label.grid(row=5, column=1, sticky=(W,E))
    
        self.file_name = StringVar()
        self.file_path = ''
        self.file_btn = ttk.Button(self.mail_page_frame, state=DISABLED)
        self.file_btn.configure(text='+', style='TMailButton.TButton', command=self.open_file_dialog)
        self.file_btn.grid(row=5, column=2, sticky=(W,E))
    
        self.file_name_label = ttk.Label(self.mail_page_frame, textvariable=self.file_name)
        self.file_name_label.grid(row=6,column=1, sticky=(W, E))
        self.file_name_label.configure(style='TMailLabel.TLabel')

        self.send_btn = ttk.Button(self.mail_page_frame)
        self.send_btn.configure(text='Send Mail', style='TMailButton.TButton', command=self.OnMailConfigure)
        self.send_btn.grid(row=7, column=1, sticky=(W,E))

        self.clear_btn = ttk.Button(self.mail_page_frame)
        self.clear_btn.configure(text='Clear', style='TMailButton.TButton', command=self.OnMailClear)
        self.clear_btn.grid(row=7, column=2, sticky=(W,E))

        logout_btn = ttk.Button(self.mail_page_frame)
        logout_btn.configure(text='Log Out', style='TMailButton.TButton', command=self.OnLogOut)
        logout_btn.grid(row=8, column=1, sticky=(W,E))

        exit_btn = ttk.Button(self.mail_page_frame)
        exit_btn.grid(row=8, column=2, sticky=(W,E))
        exit_btn.configure(text='Exit', style='TMailButton.TButton', command=self.OnExit)

        #mail_page_frame.bind("<Return>", OnMailConfigure)
        self.receiver_email_entry.focus()

        for widget in self.mail_page_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    def OnAttachmentChecker(self: object)->None:
        """
        Callback function triggered when the attachment checker checkbox is clicked.

        Enables or disables the file selection button based on the checkbox state.
        """
        if self.attachment_checker.get() == 'Yes':
            self.file_btn['state'] = 'enabled' 
            self.file_path=""
        elif self.attachment_checker.get() == 'No':
            self.file_btn['state'] = 'disabled'
            self.file_path=""
            self.file_name.set("")


    def open_file_dialog(self: object)->(str | None):
        """
        Opens a file dialog window to select a file for attachment.

        Returns:
        - The path of the selected file, or None if no file is selected.
        """
        self.file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("All files", "*.*"),) #("Text files", "*.txt"),
        )
    # Display the selected file path or perform further actions
        if self.file_path:
            print(f"Selected file: {self.file_path}")
            self.file_name_temp = self.file_path.split("/")
            self.file_name_temp = self.file_name_temp[len(self.file_name_temp)-1]
            self.file_name.set(str(str(self.file_name_temp)+ str(" is attached.")))
            return self.file_path
        else:
            return None
    
    def main_send(self, message:object)->None: 
        """
        Sends the email message using the SMTP server.

        Parameters:
        - message: The MIME message object to be sent.
        """
        try:
            self.server.send_message(message)     
            print("Message sent successfully!")
            r = messagebox.askokcancel(title="INFO", message="Mail Send Successfully!!")
            self.send_btn['state'] = 'enabled'
            self.clear_btn['state'] = 'enabled'
        except Exception as e:
            r = messagebox.askretrycancel(title="Error", message="Connection Error:" + str(e))
            self.send_btn['state'] = 'enabled'
            self.clear_btn['state'] = 'enabled' 

    def is_Emailvalidate(self:object, sender_email: str)->bool:
        """
        Validates the format of an email address.

        Parameters:
        - sender_email: The email address to be validated.

        Returns:
        - True if the email address is valid, False otherwise.
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
    
    def OnMailConfigure(self: object)->None:
        """
        Callback function triggered when the user attempts to configure and send an email.

        Constructs the email message based on user input and sends the email.
        If the email has attachments, it handles attachment file selection and attachment to the email.
        """

        self.send_btn['state'] = 'disabled'
        self.clear_btn['state'] = 'disabled'

        self.receiver_address = self.receiver_email.get().strip()
        self.mail_subject_value = self.mail_subject.get().strip()
        self.mail_body_text = self.mail_body.get("1.0", END)

        self.message = MIMEMultipart()
        self.receiver_result = self.is_Emailvalidate(self.receiver_address)
        if self.receiver_result == True:
            self.message['From'] = self.sender_email
            self.message['To'] = self.receiver_address
            if self.mail_subject_value != '':
                self.message['Subject'] = self.mail_subject_value
                if self.mail_body_text != '' and len(self.mail_body_text) > 1:
                    self.text_body = MIMEText(self.mail_body_text, 'plain')
                    self.message.attach(self.text_body)
                    if self.attachment_checker.get() == 'Yes' and self.file_path != '':
                        try:
                            self.file_object = MIMEBase('application', 'octect-stream')
                            self.file_handle = open(self.file_path, 'rb')
                            self.file_object.set_payload((self.file_handle).read())
                            encoders.encode_base64(self.file_object)

                            self.file_name = self.file_path.split("/")
                            self.file_name = self.file_name[len(self.file_name)-1]
                            self.file_object.add_header('Content-Disposition', 'attachment', filename = self.file_name)
                            self.message.attach(self.file_object)
                            self.main_send(self.message)
                        except Exception as e:
                            print(f"Error: {e}")
                            r = messagebox.askretrycancel(title=None, message="File Error:" + str(e))
                            self.send_btn['state'] = 'enabled'
                            self.clear_btn['state'] = 'enabled'
                    elif self.attachment_checker.get() == 'Yes' and self.file_path == '':
                            r = messagebox.askretrycancel(title=None, message="Please select the file")
                            self.send_btn['state'] = 'enabled'
                            self.clear_btn['state'] = 'enabled'
                    elif self.attachment_checker.get() != "Yes":
                        self.main_send(self.message)
                    
                else:
                    r = messagebox.askretrycancel(title="Invalid input", message="Please check mail body!")               
                    self.send_btn['state'] = 'enabled'
                    self.clear_btn['state'] = 'enabled'
            else:           
                r = messagebox.askretrycancel(title="Invalid input", message="Please check mail subject!")    
                self.send_btn['state'] = 'enabled'
                self.clear_btn['state'] = 'enabled'
        else:
            r = messagebox.askretrycancel(title="Invalid input", message="Please check receiver email address!")   
            self.send_btn['state'] = 'enabled'
            self.clear_btn['state'] = 'enabled'



    def OnMailClear(self: object)->None:
        """
        Callback function triggered when the user clicks the "Clear" button to clear input fields.

        Clears all input fields on the mail page, including recipient email, subject, body, and attachment information.
        """
        self.receiver_email.set("")
        self.mail_subject.set("")
        self.mail_body.delete("1.0",END)
        self.attachment_checker.set("")
        self.file_path = ""
        self.file_name.set("")
        self.file_btn['state'] = 'disabled' 


    def OnLogOut(self: object)->None:
        """
        Callback function triggered when the user clicks the "Log Out" button.

        Logs out the user by closing the SMTP server connection and navigating back to the front page window.
        """
        r = messagebox.askquestion(title="Question", message="Are you sure you want to log off?")
        print(r)
        if r == 'yes':
            from front_page import FrontPageWindow
            self.server.quit()
            self.mail_page_frame.destroy()
            FrontPageWindow(self.win_top)
        else:
            pass
    
    def OnExit(self: object)->None:
        """
        Callback function triggered when the user clicks the "Exit" button.

        Exits the application gracefully by closing the SMTP server connection and terminating the application.
        """
        r = messagebox.askquestion(title="Question", message="Are you sure you want to Exit?")
        if r == 'yes':
            self.server.quit()
            sys.exit(0)

    def mainloop(self: object)->None:
        """
        Enters the Tkinter main event loop, allowing the mail page window to handle user interactions and events.
        """
        self.win_top.mainloop()


