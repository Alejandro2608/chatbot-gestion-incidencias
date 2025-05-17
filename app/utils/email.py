import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")  # A quién le llegan los "tickets"


def enviar_ticket_por_correo(pregunta: str, correo_usuario: str = "anonimo@chatbot.com"):
    try:
        msg = EmailMessage()
        msg['Subject'] = '🛠️ Nueva Pregunta No Resuelta'
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER

        contenido = f"""
        Se ha generado un nuevo "ticket" desde el chatbot.

        🧑‍💻 Usuario: {correo_usuario}
        ❓ Pregunta: {pregunta}

        Por favor, revisar y dar respuesta.
        """

        msg.set_content(contenido)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("✅ Ticket enviado correctamente.")
        return True

    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
        return False
