from HeaderFile import *

"""
This file represents the front page window of the Email Sending Application.
It provides the user interface for signing up or signing in to the application.
"""

class FrontPageWindow():

    """
    Represents the front page window of the Email Sending Application.

    This class creates the front page window of the application, where users can either sign up or sign in.
    It provides functionality to navigate to the sign-up or sign-in pages.
    
    Modules:
    - __init__: Construtor of class FrontPageWindow
    - sign_up_page_func: Navigates to the sign-up page.
    - sign_in_page_func: Navigates to the sign-in page.
    - mainloop: Starts the Tkinter event loop.
    Attributes:
    - win_top (Tk): The top-level Tkinter window for the application.
    """
    def __init__(self: object, win_top: object) -> None:
        """
        Initializes the FrontPageWindow class.

        This method creates the front page window within the specified top-level Tkinter window.
        It configures the appearance and layout of the front page, including the title and buttons for sign-up and sign-in.

        Parameters:
        - win_top (Tk): The top-level Tkinter window for the application.

        Returns:
        - None
        """
        self.win_top = win_top
        self.win_top.geometry("600x500")

        try:
            self.style = ttk.Style()
            self.style.configure('TMainPage.TFrame', font=('Times', 20, 'bold'), justify='center', background='#BEB1AE')
            self.style.configure('TMainPageTitle.TLabel', font=('Times', 30, 'bold'), justify='center', background='#BEB1AE' )
            self.style.configure('TSignUp.TButton', font=('Times', 26), justify='center', background='#BEB1AE')
            

            self.main_page_frame = ttk.Frame(self.win_top, padding='3 3 12 12', relief='raised', borderwidth=10)
            self.main_page_frame.grid(row=1, column=1)
            self.main_page_frame.configure(style='TMainPage.TFrame')
            self.main_page_frame.rowconfigure(1, weight=1)
            self.main_page_frame.columnconfigure(1, weight=1)

            self.main_page_title = ttk.Label(self.main_page_frame, text='Email Sending Application')
            self.main_page_title.grid(row=1, column=1, sticky=(W,E,N,S), pady='0 5')
            self.main_page_title.configure(style='TMainPageTitle.TLabel')
            
            self.SignUp_btn = ttk.Button(self.main_page_frame)
            self.SignUp_btn.configure(text='Sign Up', style='TSignUp.TButton', command=self.sign_up_page_func)
            self.SignUp_btn.grid(row=2, column=1, sticky=(W,E,N,S))


            self.SignIn_btn = ttk.Button(self.main_page_frame)
            self.SignIn_btn.configure(text='Sign In', style='TSignUp.TButton', command=self.sign_in_page_func)
            self.SignIn_btn.grid(row=3, column=1, sticky=(W,E,N,S))


            for widget in self.main_page_frame.winfo_children():
                widget.grid_configure(padx=10, pady=10)

        except Exception as e:
            messagebox.askokcancel(title="Error", message=e)
            sys.exit(-1)

    def sign_up_page_func(self: object)->None:
        """
        Navigates to the sign-up page.

        This method destroys the main page frame and initializes the RegisterPageWindow,
        which represents the sign-up page of the application.

        Parameters:
        - None

        Returns:
        - None
        """
        from register_page import RegisterPageWindow
        self.main_page_frame.destroy()
        self.Register_page = RegisterPageWindow(self.win_top)

    def sign_in_page_func(self: object)->None:
        """
        Navigates to the sign-in page.

        This method destroys the main page frame and initializes the LoginPageWindow,
        which represents the sign-in page of the application.

        Parameters:
        - None

        Returns:
        - None
        """
        from login_page import LoginPageWindow
        self.main_page_frame.destroy()
        self.Login_page = LoginPageWindow(self.win_top)
        
        
    def mainloop(self: object)-> None:
        """
        Starts the Tkinter event loop.

        This method starts the Tkinter event loop, allowing the application to interact with user inputs
        and events. It runs indefinitely until the user closes the application window.

        Parameters:
        - None

        Returns:
        - None
        """
        self.win_top.mainloop()


        
        
