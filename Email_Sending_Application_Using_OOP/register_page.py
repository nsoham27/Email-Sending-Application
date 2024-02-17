from HeaderFile import *

"""
File :This file contains the RegisterPageWindow class, which provides functionality for users to register with the email sending application.
It allows users to input their name, email, mobile number, age, password, and gender, and provides options to register, clear input fields,
and navigate back to the sign-up page.
"""

class RegisterPageWindow():
    """
    This class represents the registration page window of the email sending application.

    Functions:
    - __init__(self: object, win_top=None) -> None:
    Initializes the RegisterPageWindow object.

    - OnRegister(self: object, *args) -> None:
    Callback function triggered when the user attempts to register. It retrieves user input data and displays a message box indicating successful registration.

    - OnClear(self: object) -> None:
    Callback function triggered when the user clicks the "Clear" button. It clears all input fields.

    - OnBackSignUp(self: object) -> None:
    Callback function triggered when the user clicks the "Back" button to return to the sign-up page.

    - mainloop(self) -> None:
    Enters the Tkinter main event loop.
    """

    def __init__(self: object, win_top=None) -> None:   

        """
        Initializes the RegisterPageWindow object.

        Parameters:
        - win_top: The parent window where the registration page will be displayed. Defaults to None.
        """
        
        self.win_top = win_top
        self.win_top.geometry("700x600")

        self.style = ttk.Style()
        self.style.configure('TSignUpPage.TFrame', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE')
        self.style.configure('TSignUpPageTitle.TLabel', font=('Times', 16, 'bold'), justify='center', background='#BEB1AE' )
        self.style.configure('TSignUpButton.TButton', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TSignUpLabel.TLabel', font=('Times', 14), justify='center', background='#BEB1AE')
        self.style.configure('TSignUpButton.TRadiobutton', font=('Times', 14), justify='center', background='#BEB1AE')
        
        self.signup_page_frame = ttk.Frame(self.win_top, padding='3 3 12 12', relief='raised', borderwidth=10)
        self.signup_page_frame.grid(row=1, column=1)
        self.signup_page_frame.configure(style='TSignUpPage.TFrame')
        self.signup_page_frame.rowconfigure(1, weight=1)
        self.signup_page_frame.columnconfigure(1, weight=1)

        self.register_title_label = ttk.Label(self.signup_page_frame, text="Registration")
        self.register_title_label.grid(row=1, column=2, sticky=(W,E))
        self.register_title_label.configure(style='TSignUpPageTitle.TLabel')

        self.reg_list = []
        self.registration_txt = ['Enter Name:', 'Enter Email:', 'Enter Mobile no:', 'Enter Age:']
        for i in range(4):
            self.reg_var = ttk.Label(self.signup_page_frame, text=self.registration_txt[i])
            self.reg_var.grid(row=i+2, column=1, sticky=(W,E))
            self.reg_var.configure(style='TSignUpLabel.TLabel')
            self.reg_list.append(self.reg_var)
        
        self.reg_name_label, self.reg_email_label, self.reg_mobile_label, self.reg_age_label = self.reg_list
        #for i in range()

        self.reg_name = StringVar()
    
        self.reg_name_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_name, width=30)
        self.reg_name_entry.grid(row=2, column=2, sticky=(W,E))
        self.reg_name_entry.configure(font=('Times', 14))

        self.reg_email = StringVar()
        self.reg_email_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_email, width=30)
        self.reg_email_entry.grid(row=3, column=2, sticky=(W,E))
        self.reg_email_entry.configure(font=('Times', 14))

        
        self.reg_mobile = StringVar()
        self.reg_mobile_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_mobile, width=30)
        self.reg_mobile_entry.grid(row=4, column=2, sticky=(W,E))
        self.reg_mobile_entry.configure(font=('Times', 14))

        
        self.reg_age = IntVar()
        self.reg_age_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_age, width=30)
        self.reg_age_entry.grid(row=5, column=2, sticky=(W,E))
        self.reg_age_entry.configure(font=('Times', 14))

        self.gender_select_var = StringVar()
        self.gender_male_btn = ttk.Radiobutton(self.signup_page_frame, variable=self.gender_select_var, text='Male', value='Male', style='TSignUpButton.TRadiobutton')
        self.gender_male_btn.grid(row=6, column=1, sticky=(W,E))

        self.gender_female_btn = ttk.Radiobutton(self.signup_page_frame, variable=self.gender_select_var, text='Female', value='Female', style='TSignUpButton.TRadiobutton')
        self.gender_female_btn.grid(row=6, column=2, sticky=(W,E))

        self.reg_password = StringVar()
        self.reg_password_label = ttk.Label(self.signup_page_frame, text='Enter Password:', )
        self.reg_password_label.grid(row=7, column=1, sticky=(W,E))
        self.reg_password_label.configure(style='TSignUpLabel.TLabel')
        self.reg_password_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_password, width=30)
        self.reg_password_entry.grid(row=7, column=2, sticky=(W,E))
        self.reg_password_entry.configure(font=('Times', 14))

        self.reg_repassword = StringVar()
        self.reg_repassword_label = ttk.Label(self.signup_page_frame, text='Re-Enter Password:', )
        self.reg_repassword_label.grid(row=8, column=1, sticky=(W,E))
        self.reg_repassword_label.configure(style='TSignUpLabel.TLabel')
        self.reg_repassword_entry = ttk.Entry(self.signup_page_frame, textvariable=self.reg_repassword, width=30)
        self.reg_repassword_entry.grid(row=8, column=2, sticky=(W,E))
        self.reg_repassword_entry.configure(font=('Times', 14))

        self.register_btn = ttk.Button(self.signup_page_frame, width=30)
        self.register_btn.configure(text='Register', style='TSignUpButton.TButton', command=self.OnRegister)
        self.register_btn.grid(row=9, column=1, sticky=(W,E))

        self.clear_btn = ttk.Button(self.signup_page_frame)
        self.clear_btn.configure(text='Clear', style='TSignUpButton.TButton', command=self.OnClear)
        self.clear_btn.grid(row=9, column=2, sticky=(W,E))

        self.back_btn = ttk.Button(self.signup_page_frame)
        self.back_btn.configure(text='Back', style='TSignUpButton.TButton', command=self.OnBackSignUp)
        self.back_btn.grid(row=10, column=1, sticky=(W,E))

        self.reg_name_entry.focus()
        self.win_top.bind("<Return>", self.OnRegister)

        for widget in self.signup_page_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    def OnRegister(self: object, *args)->None:
        """
        Callback function triggered when the user attempts to register.

        Retrieves user input data and displays a message box indicating successful registration.

        Parameters:
        - args: Additional arguments passed to the function.
        """
        print(self.reg_name.get(),"\n",
        self.reg_email.get(),"\n",
        self.reg_mobile.get(),"\n",
        self.reg_age.get(),"\n",
        self.reg_password.get(),"\n",
        self.reg_repassword.get(),"\n",
        self.gender_select_var.get(),"\n")
        r = messagebox.askokcancel(title="INFO", message="Registration is done!")
        self.OnClear()

    def OnClear(self: object)-> None:
        """
        Callback function triggered when the user clicks the "Clear" button.

        Clears all input fields on the registration page.
        """
        self.reg_name.set('') 
        self.reg_email.set('')
        self.reg_mobile.set('')
        self.reg_age.set('')
        self.reg_password.set('')
        self.reg_repassword.set('')
        self.gender_select_var.set('')

    def OnBackSignUp(self: object)->None:
        """
        Callback function triggered when the user clicks the "Back" button to return to the sign-up page.

        Navigates back to the front page window.
        """
        from front_page import FrontPageWindow
        self.signup_page_frame.destroy()
        FrontPageWindow(self.win_top)

    def mainloop(self: object)-> None:
        """
        Enters the Tkinter main event loop.
        """
        self.win_top.mainloop()

