import requests
import smtplib
import time
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Song-Ice-Fire-Thrones-Complete/dp/0007477155/ref=sr_1_1?crid=3ILLV1VL7EKH8&keywords=a+song+of+ice+and+fire&qid=1568283272&s=gateway&sprefix=a+song%2Caps%2C278&sr=8-1'

#use "my user agent" to find the info about the browser
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    #To retrieve data from the website
    page = requests.get(URL, headers = headers)
    #To get content of the page
    soupy = BeautifulSoup(page.content, 'html.parser')
    #To extract the product name (Find the id by clicking F12 if ya using Chrome)
    name = soupy.find(id="productTitle").getText()
    #To extract the product price
    price = soupy.find(id="soldByThirdParty").getText()
    #To gain only values and removing ₹ and , while converting it to float value
    price_value = float(price[3:4]+price[5:8])
    #To check if values are gained properly, try printing it:
    #print(name.strip())
    #print(price_value)

    #check for conditions
    if(price_value == 2312.0):
        nochange_mail()
    if(price_value < 2312.0):
        lessprice_mail()
    if(price_value > 2312.0):
        moreprice_mail()

def nochange_mail():
    #To connect with gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #To establish connection
    server.ehlo()
    #To encrypt connection
    server.starttls()
    #Doing again. Because I have to!
    server.ehlo()
    #To login: 'username', 'password' (password can be generated using App passwords)
    server.login('priyansh.16beceg082@gmail.com', 'qvvtfbzzxmzcnyti') #No need to try my password!!!
    #Adding Subject
    subject = 'No Change in Price.'
    #Adding Body
    body = 'The Price for the product remains unchanged.'
    #Mixing the two
    email = f"Subject: {subject}\n{body}"
    #Sending mail: 'From', 'To', mixing
    server.sendmail(
        'priyansh.16beceg082@gmail.com',
        'priyanshthakar@gmail.com',
        email
    )
    #Acknowledgement
    print("Your E-mail is sent.")
    #Quiting
    server.quit()

def lessprice_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('priyansh.16beceg082@gmail.com', 'qvvtfbzzxmzcnyti')
    
    subject = 'Price Reduced!'
    body = 'The Price for the product has decreased. Check Amazon!'
    email = f"Subject: {subject}\n{body}"
    server.sendmail(
        'priyansh.16beceg082@gmail.com',
        'priyanshthakar@gmail.com',
        email
    )
    
    print("Your E-mail is sent.")
    server.quit()

def moreprice_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('priyansh.16beceg082@gmail.com', 'qvvtfbzzxmzcnyti')
    
    subject = 'Price Increased!'
    body = 'The Price for the product has increased. Check Amazon!'
    email = f"Subject: {subject}\n{body}"
    server.sendmail(
        'priyansh.16beceg082@gmail.com',
        'priyanshthakar@gmail.com',
        email
    )
    
    print("Your E-mail is sent.")
    server.quit()

while(1):
    #calling function
    check_price()
    #To add a timestamp of one day
    time.sleep(60*60*24)