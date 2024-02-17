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
"""


from root_page import RootPageWindow

def main():

    """
    Main function to start the Air Quality Application.

    This function initializes the RootPageWindow, which represents the main window of the Air Quality Application.
    It creates an instance of the RootPageWindow class, which contains the graphical user interface (GUI) elements
    and functionality for the application. The mainloop method is then called on the app_window instance,
    which starts the Tkinter event loop, allowing the application to interact with user inputs and events.

    """
    app_window = RootPageWindow() # Create an instance of the RootPageWindow class
    app_window.mainloop() # Start the Tkinter event loop to run the application

main()