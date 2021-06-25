#importa biblioteca para = mexer com arquivos, mexer com imagens, com email, anexar arquivos  de email, codificar a imagem
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
    
    #realiza uma alteração nas imagens
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
usuario = "EmaildeExemplo@gmail.com"
senha = "senha"

def enviarEmail(email, nome,diretor, professor):
    criarImagem(nome, diretor, professor)
    #chama função para criar a função
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(usuario, senha)
    
    #corpo da mensagem
    mensagem = f"Ola {nome} segue em anexo seu certificado"
    email_msg = MIMEMultipart()
    email_msg["From"] = usuario
    email_msg["To"] = email
    email_msg["Subject"] = "Notas finais"
    email_msg.attach(MIMEText(mensagem, "plain"))
    
    #tratamento da imagem na mensagem
    attachment = open(f"{nome}.png", "rb")#abre o arquivo de imagem 
    att = MIMEBase("application", "octet-stream") #instrui o metodo que a imagem vai ser incorporado
    att.set_payload(attachment.read()) #ler a imagem 
    encoders.encode_base64(att) #codifica a imagem para base64
    att.add_header("Content-Disposition", f"attachment; filename= {nome}.png")#adiciona nos anexos
    attachment.close()
    email_msg.attach(att)#de fato adiciona as informações da imagem ao resto do email
    #envia o email
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()
    
#salvar o arquivo em um dataframe
alunos = pd.read_csv("certificado.csv")
for i in range(0,len(alunos)): #busca por todos os dados
    email = str(alunos.loc[i, "Email"])
    nome = str(alunos.loc[i, "Nome"])
    diretor = str(alunos.loc[i, "Diretor"])
    professor = str(alunos.loc[i, "Professor"]) 
    #Salva as informações em variaveis locais
    enviarEmail(email, nome, diretor, professor)
    #chama a função que envia email
   
