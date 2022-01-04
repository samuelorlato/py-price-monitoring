from bs4 import BeautifulSoup
import requests
import smtplib
import email.message as email

URL = str(input("Coloque a URL do produto do Mercado Livre: "))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0 X-Middleton/1"}

site = requests.get(URL, headers = headers)

soup = BeautifulSoup(site.content, "html.parser")

product_title = soup.find("h1", class_ = "ui-pdp-title").get_text()

product_price = float(soup.find("span", class_ = "price-tag-fraction").get_text().strip().replace(".", ""))

def send_email():
    email_content = URL

    msg = email.Message()

    msg["Subject"] = "Preço de " + str(product_title) + " abaixou!"

    msg["From"] = "emailfrom"
    msg["To"] = str(input("Digite seu email: "))
    
    password = "passwordfrom"

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_content)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())

    print("Email enviado!")

limit = float(input("Digite o preço mínimo para receber notificações: R$"))

if product_price <= limit:
    send_email()