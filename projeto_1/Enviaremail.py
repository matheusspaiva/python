#importa o pandas para leitura de arquivos
#Importa biblioteca para mandar email
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
usuario = "EmaildeExemplo@gmail.com"
senha = "senha"

def enviar(contato, name, nota):
    server = smtplib.SMTP(host,port)#entrar no servidor do gmail
    server.ehlo()
    server.starttls()
    server.login(usuario, senha)#logar na conta
    #informações do mail(remetete, destinatario ,assunto, corpo da mensagem)
    mensagem = "Ola " + name + " sua nota final " + nota
    email_msg = MIMEMultipart()
    email_msg["From"] = usuario
    email_msg["To"] = contato
    email_msg["Subject"] = "Notas finais"
    email_msg.attach(MIMEText(mensagem, "plain"))
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()

#leitura de arquivos
df = pd.read_csv("notas.csv")
for i in range (0,len(df):#faz um corrida pelo tamanho total dos dados obtidos
    nome= str(df.loc[i, "Nome"])
    email = str(df.loc[i, "Email"])
    media = str(df.loc[i, "Media"])
    #salva em variaveis locais os dados do dataframe
    enviar(email, nome, media)
    #chama o metodo que manda email
