# Importing required libraries
import ssl
import geopy
import certifi
from geopy.geocoders import Nominatim
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Tkinter import *
from tkMessageBox import showinfo

#SSLcertificate verification
ctx= ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

#geopy code to find location and coords
geolocator=Nominatim(user_agent="http")
area="Keshwapur"
city="Hubli"
country="India"
loc=geolocator.geocode(area+","+city+","+country)
# print(loc.latitude)
# print(loc.longitude)
add=geolocator.reverse(str(loc.latitude)+","+str(loc.longitude))

#SMTP code to send email to selected contacts
fromadr="akashdev1309@gmail.com"
recipients="charlesbabbage1709@gmail.com, aakashnayak.ubl@gmail.com"
msg=MIMEMultipart()
msg["Subject"]="SOS"
msg["From"]=fromadr
msg['To']=" ".join(recipients)
body = MIMEText(" This is my location!"+"\n"+"Latitude :"+str(loc.latitude)+"\n"+"Longitude :"+str(loc.latitude)+"\n"+"Location :"+str(add.address))
msg.attach(body)

#function to start a conection to the smtp server and send a TLS encrypted email
def sendEmail():
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.ehlo()
    conn.starttls()
    conn.login("akashdev1309@gmail.com", "Akash1309#dev")
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
l=Label(window, text="EMERGENCY? Send an SOS! Click Below!",font="Helvetica, 13",bg="#E67A0B",fg="#fff").place(x=40,y=10)
b=Button(window, text="SOS", padx=40, pady=10,bg="#AE0A0A",font=30, command=sendEmail,fg="#fff").place(x=130,y=50)

#background color
window.configure(bg="#E67A0B")

window.mainloop()