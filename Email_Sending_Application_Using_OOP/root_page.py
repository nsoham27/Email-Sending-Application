from HeaderFile import *
from front_page import FrontPageWindow


class RootPageWindow:

    """
    Represents the main window of the Email Sending Application.

    This class initializes the main window of the Email Sending Application using the Tkinter library in Python.
    It creates a graphical user interface (GUI) for the application and configures its appearance and behavior.
    The main window contains the front page elements where users can interact with the application.

    Modules:
    - __init__ : Constructor
    - mainloop : Start the Tkinter event loop.

    Attributes:
    - root_window (Tk): The root Tkinter window for the application.
    """
    def __init__(self: object) -> None:

        """
        Initializes the RootPageWindow class.

        This method creates the root Tkinter window, sets its title, icon, size, and background color.
        It configures the window's layout to be resizable and adds the necessary widgets and components
        for the front page of the application.

        Parameters:
        - None

        Returns:
        - None
        """

        self.root_window = Tk() # Create the root Tkinter window
        self.root_window.title("Email Sending Application")
        self.root_window.iconbitmap("logo1.ico")
        self.root_window.geometry("600x500")
        self.root_window.config(bg='#F0F0F0')
        self.root_window.rowconfigure(1, weight=1)
        self.root_window.columnconfigure(1, weight=1)

        # Initialize the FrontPageWindow within the root window
        FrontPageWindow(self.root_window)

        
    def mainloop(self: object)->None:
        """
        Start the Tkinter event loop.

        This method starts the Tkinter event loop, allowing the application to interact with user inputs
        and events. It runs indefinitely until the user closes the application window.

        Parameters:
        - None

        Returns:
        - None
        """
        self.root_window.mainloop() # Start the Tkinter event loop