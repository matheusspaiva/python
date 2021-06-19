import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
usuario = "matheusp.silva0302@gmail.com"
senha = "sonea123"

def enviar(contato, name, nota):
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(usuario, senha)
    
    mensagem = "Ola " + name + " sua nota final " + nota
    email_msg = MIMEMultipart()
    email_msg["From"] = usuario
    email_msg["To"] = contato
    email_msg["Subject"] = "Notas finais"
    email_msg.attach(MIMEText(mensagem, "plain"))
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()

df = pd.read_csv("notas.csv")
for i in range (0,3):
    nome= str(df.loc[i, "Nome"])
    email = str(df.loc[i, "Email"])
    media = str(df.loc[i, "Media"])
    
    enviar(email, nome, media)