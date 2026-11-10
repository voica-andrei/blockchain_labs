from aiosmtpd.controller import Controller
import smtplib
from email.message import EmailMessage

IP_ADDRESS = "127.0.0.1"
PORT = 2525
OTHER_SERVER_IP = "127.0.0.1"
OTHER_PORT = 2525

# handle incoming emails ----------------------------------
class MailHandler:
    async def handle_DATA(self, server, session, envelope):
        print("\n=== NEW EMAIL ===")
        print("From:", envelope.mail_from)
        print("To:", envelope.rcpt_tos)
        print("Message:")
        print(envelope.content.decode(errors="replace"))
        print("=================\n")
        return "250 OK"

controller = Controller(
    MailHandler(),
    hostname=IP_ADDRESS,
    port=PORT
)

# send emails ----------------------------------
def send_email():
    print("Send default email? (y/n): ", end="")
    choice = input().strip().lower()
    if choice == "y":
        msg = EmailMessage()
        msg["From"] = "andrei@lab.test"
        msg["To"] = "ligia@lab.test"
        msg["Subject"] = "Email Test"
        msg.set_content("Hello! Send me 100 BTC or your computer explodes!")
    elif choice == "n":
        msg = EmailMessage()
        print("From: ", end="")
        msg["From"] = input()
        print("To: ", end="")
        msg["To"] = input()
        print("Subject: ", end="")
        msg["Subject"] = input()
        print("Content: ", end="")
        msg.set_content(input())
    else:
        print("Invalid choice. Exiting.")
        return

    server_ip = input("Enter destination server IP (default: 127.0.0.1): ") or IP_ADDRESS
    server_port = input("Enter destination server port (default: 2525): ") or PORT

    with smtplib.SMTP(server_ip, server_port) as smtp:
        smtp.send_message(msg)

    print("Email sent successfully!")

# start server ----------------------------------
controller.start()
print("SMTP server running on port 2525")

try:
    while True:
        print("\n===== Email Menu =====")
        print("Choose an option:")
        print("1. Send an email")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            send_email()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Exiting.")
finally:
    controller.stop()
