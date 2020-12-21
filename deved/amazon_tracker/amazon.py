import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/dp/B082YGVGQL/?coliid=I24HKNBYZ8DIQP&colid=18L4QYFAKDIXX&psc=1&ref_=lv_ov_lig_dp_it_im'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[5:8])
    print(converted_price)

    if(converted_price < 422):
        send_mail()

# print(title.strip())
# print(price.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('drobb2011@gmail.com', 'kvemdqkffjtkjsnr')

    subject = 'Price Drop'
    body = 'Check the Samsung SSD drive here: https://www.amazon.ca/dp/B082YGVGQL/?coliid=I24HKNBYZ8DIQP&colid=18L4QYFAKDIXX&psc=1&ref_=lv_ov_lig_dp_it_im'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('david@excession.org',
                    'drobb2011@gmail.com',
                    msg)
    print("Price drop email sent!")
    server.quit()

check_price()
