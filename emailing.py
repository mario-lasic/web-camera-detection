from passwords import email_password
import smtplib
from PIL import Image
from email.message import EmailMessage

PASSWORD = email_password
SENDER = "mariotest856@gmail.com"
RECEIVER = "mariotest856@gmail.com"
def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, 'rb') as file: 
        content = file.read()
        img = Image.open(file) 
        image_format = img.format

    email_message.add_attachment(content, maintype="image", subtype=image_format)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")
if __name__ == "__main__":
    send_email("images/10.png")