import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Authentication:

    def __init__(
            self: object, 
            sender_email_address: str,
            password: str
        ) -> None:

        try:
            if type(sender_email_address) != str:
                raise TypeError("Bad type: Sender email address.")
            if type(password) != str:
                raise TypeError("Bad type:Sender email Password.")
            
            if (
                sender_email_address == '' or
                ('@' or '.') not in sender_email_address
                ):
                raise ValueError("Sender email address is not in correct format!")
            local, domain = sender_email_address.split('@', 1)

            if (not local or not domain) or ('.' not in domain):
                raise ValueError("Sender email address is not in correct format!")

            if password == '' or len(password) < 5:
                raise ValueError("Sender email password is not in correct format!")

        except TypeError as e:
            print(f"Error occured: {e}")
            sys.exit(-1)
        except ValueError as e:
            print(f"Error occured:{e}")
            sys.exit(-1)
    
        self.sender_email_address = sender_email_address
        self.password = password
        
    def is_Emailvalidate(self: object, email_address)->bool:

        if type(email_address) != str:
            return False
        
        if email_address == '':
            return False
        
        if ('@' or '.') not in email_address:
            return False
        
        local, domain = email_address.split('@', 1)

        if not local or not domain:
            return False
        
        if '.' not in domain:
            return False
        
        return True
    
    def is_password(self: object)->bool:

        if (
            self.password == '' or 
            len(self.password) < 5 or 
            type(self.password) != str
        ):
            return False
        
        return True
    
    def login_authentication(self: object, server: object):
        try:
            server.login(self.sender_email_address.strip(), self.password.strip())
            print("Login Successfull!")
            return True
        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication error occured:{e}")
            server.quit()
            return False
        except smtplib.SMTPException as e:
            print(f"Error occured: {e}")
            server.quit()
            return False


class Server(Authentication):

    def __init__(self: object, sender_email_address: str, password: str) -> None:
        Authentication.__init__(self, sender_email_address, password)
        self.login_result = False
        self.server = ''

        if (Authentication.is_Emailvalidate(self, sender_email_address) and Authentication.is_password(self)) == True:
            
            try:
                self.server = smtplib.SMTP("smtp.office365.com", 587)
                self.server.starttls()
                print("Server is created!")
                self.login_result = Authentication.login_authentication(self, self.server) 
            except smtplib.SMTPConnectError as e:
                print(f"Connection error occured: {e}")
                self.server.quit()
                return False
            except smtplib.SMTPException as e:
                print(f"Error occured: {e}")
                self.server.quit()
                return False   
        else:
            print("Sender email address or password is not in correct format!")
            return False
        

        if self.login_result == True:
            return True
        else:
            self.server.quit()
            return False


class Email(Server):

    def __init__(self: object, sender_email_address: str, password: str) -> None:
        result = Server.__init__(self,sender_email_address, password)
        
        try:
            receiver_email_address = input("Enter a receiver email address:")
            if Authentication.is_Emailvalidate(self, receiver_email_address) == False:
                raise ValueError("Receiver email address is not in correct format!")
        except ValueError as e:
            print(f"Error occured: {e}")
            self.server.quit()
            sys.exit(-1)

        self.receiver_email_address = receiver_email_address
 
    
    
    def message_body(self: object, text:str, message: object)->object:
    # create an email message text object
        try:
            text_body = MIMEText(text, 'plain')
            message.attach(text_body)
            return message
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(-1)

    def message_attachment(self: object, file_path:str, message:object)->object:

        try:
            file_object = MIMEBase('application', 'octect-stream')
            file_handle = open(file_path, 'rb')
            file_object.set_payload((file_handle).read())
            encoders.encode_base64(file_object)

            file_name = file_path.split("\\")
            file_name = file_name[len(file_name)-1]

            file_object.add_header('Content-Disposition', 'attachment', filename = file_name)
            message.attach(file_object)
            return message
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(-1)


    def mail_configure(self: object)->None:
        try:
            message = MIMEMultipart()
        except ImportError as e:
            print(f"Error: {e}")
            sys.exit(-1)
        
        text=input("Please enter a message body:")
        try:
            if text == '':
                raise ValueError("Message body cannot be empty.")
            message = self.message_body(text, message)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(-1)

        response = input("Do you want to attach any file or image?[y|n]:")
        if response in ['y', 'Y', 'yes', 'Yes', 'YES']:

            file_path = input("Please enter the file name with file location:")

            if '"' in file_path:
                file_path = file_path[1:len(file_path)-1]

            try:
                if file_path == '':
                    raise ValueError("File path cannot be empty!")
                elif os.path.exists(file_path):
                    message = self.message_attachment(file_path, message) 
                else:
                    raise FileNotFoundError("File not found at the given location.")
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(-1)
            except FileNotFoundError as e:
                print(f"Error: {e}",f"\nFile Path:{file_path}")
                sys.exit(-1)
            except:
                print("Something went wrong! please check again.")
                sys.exit(-1)


        subject=input("Please enter a message subject:")
        try:
            if subject == '':
                raise ValueError("Message subject cannot be empty.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(-1)

        message['From'] = self.sender_email_address
        message['To'] = self.receiver_email_address
        message['Subject'] = subject

        return message

    def Send_email(self: object, message: object):    
        try:
            self.server.send_message(message)
            print("Message sent successfully!")
            self.server.quit()
            #sys.exit(0)
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Error: {e}")
            self.server.quit()
            sys.exit(-1)
        except smtplib.SMTPSenderRefused as e:
            print(f"Error: {e}")
            self.server.quit()
            sys.exit(-1)
        except smtplib.SMTPDataError as e:
            print(f"Error: {e}")
            self.server.quit()
            sys.exit(-1)
        except Exception as e:
            print(f"Error: {e}")
            self.server.quit()
            sys.exit(-1)

        
def main()->None:

    sender_email_address = input("Please enter a sender email address:")
    password = input("Please enter a sender email password:")
    
    try:
        E1 = Email(sender_email_address, password)
        email = E1.mail_configure()
        E1.Send_email(email)
        print("Sender:", E1.sender_email_address, "-->" ,"Receiver:", E1.receiver_email_address)
        sys.exit(0)
    except TypeError as e:
        print(f"Error occured: {e}")
        sys.exit(-1)

try:
    main()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(-1) 