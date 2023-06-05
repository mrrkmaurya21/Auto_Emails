# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import smtplib
import csv
from email.message import EmailMessage

def send_email(subject, message, sender_email, sender_password, recipient_emails,attachment_path):
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email to each recipient
    for recipient_email in recipient_emails:
        # Create the email message
        email_message = EmailMessage()
        email_message['Subject'] = subject
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message.set_content(message)

        # Attach the file
        with open(attachment_path, 'rb') as file:
            attachment_data = file.read()
            attachment_name = attachment_path.split('/')[-1]  # Extract the filename from the path
            email_message.add_attachment(attachment_data, maintype='application', subtype='octet-stream', filename=attachment_name)

        # Send the email
        server.send_message(email_message)

    # Disconnect from the server
    server.quit()


def main():
    # Email settings
    subject = "just for check "
    message = "Hello Mr. How are you"
    sender_email = "Your Email id"
    sender_password = "mezyntdnkqxsnkji"
    attachment_path="E:/datafile/emails.csv"

    # Read recipient emails from CSV file
    recipient_emails = []
    with open('emails.csv', 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            recipient_emails.append(row[0])

    # Send the email
    send_email(subject, message, sender_email, sender_password, recipient_emails,attachment_path)

if __name__ == "__main__":
    main()
