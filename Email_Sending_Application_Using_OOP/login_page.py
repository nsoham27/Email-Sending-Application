from HeaderFile import *

"""
This file contains the LoginPageWindow class, which represents the login page of the email sending application.
It provides functionality for users to log in with their email credentials.
"""

class LoginPageWindow():
    """
    This class represents the login page window of the email sending application.
    It provides functionality for users to log in with their email credentials.
    Functions:
    - __init__(self, win_top: Tk) -> None:
    Initializes the LoginPageWindow object.

    - is_Emailvalidate(self, sender_email: str) -> bool:
    Validates the format of an email address.

    - is_password(self, sender_password: str) -> bool:
    Validates the format of a password.

    - login_authentication(self, server: object, sender_email: str, sender_password: str) -> bool:
    Authenticates the user's email credentials with the SMTP server.

    - server_connection(self, sender_email: str, sender_password: str) -> bool:
    Establishes a connection with the SMTP server using the user's email credentials.

    - OnLogin(self, *args):
    Callback function triggered when the user attempts to log in.

    - OnBackSignIn(self):
    Callback function triggered when the user clicks the "Back" button to return to the sign-in page.

    - server_end(self):
    Terminates the SMTP server connection.

    - mainloop(self):
    Enters the Tkinter main event loop.
    """

    def __init__(self, win_top)->None:
        """
        Initialize the LoginPageWindow class.

        Parameters:
        - win_top (Tk): The Tkinter root window object.
        """
        
        self.win_top = win_top
        self.win_top.geometry('600x500')

        self.style = ttk.Style()
        self.style.configure('TLoginPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
        self.style.configure('TLoginPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
        self.style.configure('TLoginButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TLoginLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TProgressLabel.TLabel', font=('Times',12), justify='center', background='#BEB1AE')
        
        self.login_page_frame = ttk.Frame(self.win_top, padding='3 3 12 12', relief='raised', borderwidth=10)
        self.login_page_frame.grid(row=1, column=1)
        self.login_page_frame.configure(style='TLoginPage.TFrame')
        self.login_page_frame.rowconfigure(1, weight=1)
        self.login_page_frame.columnconfigure(1, weight=1)

        self.login_page_title = ttk.Label(self.login_page_frame, text='Login')
        self.login_page_title.grid(row=1, column=2, sticky=(W,E,N,S))
        self.login_page_title.configure(style='TLoginPageTitle.TLabel')
        
        
        self.login_txt = ['Email', 'Password']
        self.login_label = []
        self.lgn_email = StringVar()
        self.lgn_password = StringVar()

        for i in range(2):
            self.login_var = ttk.Label(self.login_page_frame, text=self.login_txt[i])
            self.login_var.grid(row=i+2, column=1, sticky=(W,E))
            self.login_var.configure(style='TLoginLabel.TLabel')
            self.login_label.append(self.login_var)
        self.email_label, self.password_label = self.login_label
    
        self.email_entry = ttk.Entry(self.login_page_frame, textvariable=self.lgn_email, width=30)
        self.email_entry.grid(row=2, column=2, sticky=(W,E))
        self.email_entry.configure(font=('Times', 14))

        self.password_entry = ttk.Entry(self.login_page_frame, show='*', textvariable=self.lgn_password, width=30)
        self.password_entry.grid(row=3, column=2, sticky=(W,E))
        self.password_entry.configure(font=('Times', 14))

        self.login_btn = ttk.Button(self.login_page_frame)
        self.login_btn.configure(text='Login', style='TLoginButton.TButton', command=self.OnLogin)
        self.login_btn.grid(row=4, column=2, sticky=(W,E))

        self.back_btn = ttk.Button(self.login_page_frame)
        self.back_btn.configure(text='Back', style='TLoginButton.TButton', command=self.OnBackSignIn)
        self.back_btn.grid(row=4, column=1, sticky=(W,E))

        self.progress = StringVar()
        self.progress.set("")
        self.progress_label = ttk.Label(self.login_page_frame, textvariable=self.progress)
        self.progress_label.grid(row=5,column=1, sticky=(W, E))
        self.progress_label.configure(style='TProgressLabel.TLabel')

        self.email_entry.focus()
        self.win_top.bind("<Return>", self.OnLogin)


        for widget in self.login_page_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
    #---
    
    def is_Emailvalidate(self, sender_email: str)->bool:
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
    
    def is_password(self, sender_password: str)->bool:
        """
        Check if the provided password meets the criteria.

        Parameters:
        - sender_password (str): Password to be validated.

        Returns:
        - bool: True if the password is valid, False otherwise.
        """

        # Validate password format
        # ...

        if (
            sender_password == '' or 
            len(sender_password) < 5 or 
            type(sender_password) != str
        ):
            return False
            
        return True

    def login_authentication(self, server: object, sender_email: str, sender_password: str)->bool:
        
        """
        Authenticate the user's email login credentials.

        Parameters:
        - server (object): SMTP server object.
        - sender_email (str): User's email address.
        - sender_password (str): User's email password.

        Returns:
        - bool: True if authentication is successful, False otherwise.
        """

        # Authenticate user
        # ...
        try:
            server.login(sender_email.strip(), sender_password.strip())
            print("Login Successfull!")
            return True
        except Exception as e:
            print(f"Authentication error occured:{e}")
            r = messagebox.askretrycancel(title=None, message="Authentication Error:" + str(e))
            return False

    def server_connection(self, sender_email: str, sender_password: str)->bool: 
        """
        Establish a connection to the SMTP server.

        Parameters:
        - sender_email (str): User's email address.
        - sender_password (str): User's email password.

        Returns:
        - bool: True if connection is successful, False otherwise.
        """

        # Connect to SMTP server
        # ...
    
        self.server = None
        self.login_result = False

        try:
            self.server = smtplib.SMTP("smtp.office365.com", 587)
            self.server.starttls()
            print("Server is created!")
            self.login_result = self.login_authentication(self.server, sender_email, sender_password) 
            if self.login_result == True:
                return True
            else:
                return False
        except Exception as e:
            messagebox.askretrycancel(title="Error", message=e)
            return False
    
    def OnLogin(self: object, *args: tuple)->None:

        """
        Callback function for the login button click event.
        """

        # Perform login operation
        # ...
        self.login_btn['state'] = 'disabled'
        self.back_btn['state'] = 'disabled'
        self.progress.set("Please wait...!")
        self.win_top.update()
        self.sender_email = self.lgn_email.get().strip()
        self.sender_password = self.lgn_password.get().strip()

        self.email_result = self.is_Emailvalidate(self.sender_email)
        self.password_result = self.is_password(self.sender_password)
    
        if(self.email_result == True and self.password_result == True):
            self.login = self.server_connection(self.sender_email, self.sender_password)
            if self.login == True:
                from mail_page import MailPageWindow
                self.login_btn['state'] = 'enabled'
                self.back_btn['state'] = 'enabled'
                self.win_top.update()
                self.login_page_frame.destroy()  
                MailPageWindow(self.win_top, self.server, self.sender_email, self.sender_password)  
                  
            else:
                print("Failed!")
                self.server_end()
                self.login_btn['state'] = 'enabled'
                self.back_btn['state'] = 'enabled'
                self.progress.set("")
                self.win_top.update()
        elif(self.email_result==True and self.password_result == False):
            r = messagebox.askretrycancel(title="Invalid input", message="Wrong password!")
            self.login_btn['state'] = 'enabled'
            self.back_btn['state'] = 'enabled'
            self.progress.set("")
        elif(self.email_result==False and self.password_result == True):
            r = messagebox.askretrycancel(title="Invalid input", message="Wrong email id!")
            self.login_btn['state'] = 'enabled'
            self.back_btn['state'] = 'enabled'
            self.progress.set("")
        else:
            r = messagebox.askretrycancel(title="Invalid input", message="Please check email id and password!")
            self.login_btn['state'] = 'enabled'
            self.back_btn['state'] = 'enabled'
            self.progress.set("")

    def OnBackSignIn(self: object)-> None:
        """
        Callback function for the back button click event.
        """

        # Navigate back to the front page
        # ...
        from front_page import FrontPageWindow
        self.login_page_frame.destroy()
        FrontPageWindow(self.win_top)

    def server_end(self: object)->None:
        """
        Terminate the SMTP server connection.
        """

        # Close the SMTP server connection
        # ...
        self.server.quit()

    def mainloop(self: object)-> None:
        """
        Start the main event loop of the login page window.
        """
        self.win_top.mainloop()


