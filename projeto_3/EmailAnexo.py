import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib 

from PIL import Image, ImageFont, ImageDraw

def criarImagem(nome, diretor, professor):
    #cordenação dos textos
    pessoa_cod = (600,500)
    diretor_cod = (300,1010)
    professor_cod = (1250,1010)
    rgb = (201,170,78) #cor das letras 
    
    imagem = Image.open(r"certificadoImagem.png")
    font1 = ImageFont.truetype(r"C:\Windows\Fonts\ARIALN.TTF", 100)
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\ARIALN.TTF", 65)
    desenho = ImageDraw.Draw(imagem)
    desenho.text(pessoa_cod, nome, font=font1, fill= rgb)
    desenho.text(diretor_cod, diretor, font=font2, fill= (0,0,0))
    desenho.text(professor_cod, professor, font=font2, fill= (0,0,0))
    imagem.save(f"{nome}.png")

host = "smtp.gmail.com"
port = 587
usuario = "matheusp.silva0302@gmail.com"
senha = "sonea123"

def enviarEmail(email, nome,diretor, professor):
    criarImagem(nome, diretor, professor)
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(usuario, senha)
    
    mensagem = f"Ola {nome} segue em anexo seu certificado"
    email_msg = MIMEMultipart()
    email_msg["From"] = usuario
    email_msg["To"] = email
    email_msg["Subject"] = "Notas finais"
    email_msg.attach(MIMEText(mensagem, "plain"))
    
    attachment = open(f"{nome}.png", "rb")
    att = MIMEBase("application", "octet-stream")
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
    att.add_header("Content-Disposition", f"attachment; filename= {nome}.png")
    attachment.close()
    email_msg.attach(att)
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()
    
alunos = pd.read_csv("certificado.csv")
for i in range(0,len(alunos)):
    email = str(alunos.loc[i, "Email"])
    nome = str(alunos.loc[i, "Nome"])
    diretor = str(alunos.loc[i, "Diretor"])
    professor = str(alunos.loc[i, "Professor"]) 
    enviarEmail(email, nome, diretor, professor)
   