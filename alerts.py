import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import ALERTS

def check_alerts():
    for ticker, thresholds in ALERTS.items():
        data = yf.download(ticker, period="1d", interval="1h")["Adj Close"]
        last_price = data.iloc[-1]

        if last_price >= thresholds["high"]:
            send_email_alert(ticker, last_price, "subió")
        elif last_price <= thresholds["low"]:
            send_email_alert(ticker, last_price, "bajó")

def send_email_alert(ticker, price, direction):
    sender_email = "mbustosvillar@gmail.com"
    receiver_email = "mbustosvillar@gmail.com"
    password = ";*CqE49O18UBP2iu"

    subject = f"📈 ALERTA: {ticker} {direction} a {price}"
    body = f"El activo {ticker} ha {direction} y ahora cuesta {price} USD."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    check_alerts()
