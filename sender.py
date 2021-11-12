# Importing required libraries

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Tkinter import *
from tkMessageBox import showinfo

#SMTP code to send email to selected contacts
fromadr="youremail@gmail.com"
recipients="recipient1@gmail.com, recipient2@gmail.com"
msg=MIMEMultipart()
msg["Subject"]="SOS"
msg["From"]=fromadr
msg['To']=" ".join(recipients)
body = MIMEText("HELP ME! This is an SOS message!"))
msg.attach(body)

#function to start a conection to the smtp server and send a TLS encrypted email
def sendEmail():
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.ehlo()
    conn.starttls()
    conn.login("youremail@gmail.com", "your_gmail_password")
    conn.sendmail(fromadr,recipients,msg.as_string())
    print("Mail(s) Sent!")
    showinfo(title="Status", message="Mail Delivered!")
    conn.quit()


#GUI-application using Tkinter
window=Tk()
window.geometry("400x260")
window.maxsize(400,260)
window.wm_iconbitmap("sos.ico")
window.title("Savepulse - Send an SOS")

#label and button
l=Label(window, text="EMERGENCY? Send an SOS! Click Below!",font="Helvetica, 13",fg="#fff").place(x=40,y=10)
b=Button(window, text="SOS", padx=40, pady=10,bg="#AE0A0A",font=30, command=sendEmail,fg="#fff").place(x=130,y=50)

#background color
window.configure(bg="#0f0f0f")

window.mainloop()
