#Start

#Imports
from email import message
import json
import tkinter as tk
from tkinter import messagebox
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Code
messagebox.showinfo("A message from the Developer", "Hi! So this app only supports hotmail and outlook (not Gmail) We'll put Gmail soon!")
os.system("title PyMail")
root = tk.Tk()
root.title("PyMail")
root.iconbitmap('app_icon.ico')
App_Version = "V1.0.0"
print(f"Version: {App_Version}")
root.geometry("500x500")
if os.path.exists("info.json"):
    with open ("info.json") as ID:
        data = json.load(ID)
        mail = data["E_Mail"]
        mail_password = data["Password"]
        nickname = data["Nickname"]
        messagebox.showinfo("Welcome Back!", f"Welcome Back to PyMail {nickname}!")
else:
    messagebox.showerror("Error: File not found (404)", "Error: File info.json is missing. Please download this file and try again. Error ID / Code: 404")
    exit(404)
    

    
def send():
    
    sender_email = mail
    receiver_email = f_r
    smtp_server = "smtp.outlook.com"
    smtp_port = 587
    sender_password = mail_password
    subject = f_s
    message = f_msg
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    messagebox.showinfo("Info", "Your E-Mail has been sent!")


    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your email address and password
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        # Login using your gmail address and password
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))
        
def check():
    global f_r
    global f_s
    global f_msg
    f_r = rec_input.get()
    f_s = subject_input.get()
    f_msg = msg_input.get()
    send()  # Move the send() function call here, after getting the user input values

rec_lab = tk.Label(root, text="Receiver E-Mail")
rec_lab.pack()
rec_input = tk.Entry(root)
rec_input.pack()

sub_lab = tk.Label(root, text="Subject")
sub_lab.pack()
subject_input = tk.Entry(root)
subject_input.pack()

msg_lab = tk.Label(root, text="Message")
msg_lab.pack()
msg_input = tk.Entry(root)
msg_input.pack()

send_bt = tk.Button(root, text="SEND!", command=check)
send_bt.pack()

root.mainloop()