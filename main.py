from bs4 import BeautifulSoup
import requests
import smtplib
import email.message as email

import typer

app = typer.Typer()

def send_email(URL, product_title, to_email, price, from_email, from_email_password):
    email_content = URL

    msg = email.Message()

    msg["Subject"] = "Preço de " + str(product_title) + " chegou a R$"+str(price)+"!"

    msg["From"] = from_email
    msg["To"] = to_email
    
    password = from_email_password

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_content)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())

    typer.echo(typer.style(f"Email enviado para {to_email}!", fg=typer.colors.GREEN, bold=True))

@app.command()
def track(to_email: str = typer.Option(...), product_url: str = typer.Option(...), target_price: float = typer.Option(...), from_email: str = typer.Option(...), from_email_password: str = typer.Option(...)):
    to_email = to_email

    URL = product_url

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0 X-Middleton/1"}

    site = requests.get(URL, headers = headers)

    soup = BeautifulSoup(site.content, "html.parser")

    product_title = soup.find("h1", class_ = "ui-pdp-title").get_text()

    product_price = float(soup.find("span", class_ = "price-tag-fraction").get_text().strip().replace(".", ""))

    limit = target_price

    if product_price <= limit:
        send_email(URL=URL, product_title=product_title, to_email=to_email, price=product_price, from_email=from_email, from_email_password=from_email_password)

if __name__ == "__main__":
    app()