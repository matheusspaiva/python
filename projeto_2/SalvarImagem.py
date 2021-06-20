#importa biblioteca que trabalha com imagens pillow (PIL)
#importa biblioteca que trabalha com arquivos
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

def criarImagem(nome, diretor, professor):
    #cordenação dos textos
    pessoa_cod = (600,500)
    diretor_cod = (300,1010)
    professor_cod = (1250,1010)
    rgb = (201,170,78) #cor das letras 
    
    #salva a imagem em uma variavel
    imagem = Image.open(r"certificadoImagem.png")
    font1 = ImageFont.truetype(r"C:\Windows\Fonts\ARIALN.TTF", 100)#fonte e tamanho do texto
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\ARIALN.TTF", 65)
    desenho = ImageDraw.Draw(imagem)#cria variavel que permite fazer alteração na imagem
    desenho.text(pessoa_cod, nome, font=font1, fill= rgb) #inseri o texto com as informações que veio dos argumentos
    desenho.text(diretor_cod, diretor, font=font2, fill= (0,0,0))
    desenho.text(professor_cod, professor, font=font2, fill= (0,0,0))
    imagem.save(f"{nome}.png") #salva a nova imagem alterada com o nome escolhido

#salva as informações em um dataframe
alunos = pd.read_csv("certificado.csv")
for i in range(0,len(alunos)): #busca por todo data frame
    nome = str(alunos.loc[i, "Nome"])
    diretor = str(alunos.loc[i, "Diretor"])
    professor = str(alunos.loc[i, "Professor"])
    #salva as informações em variaveis locais
    criarImagem(nome,diretor,professor)
    #chama a função que muda a foto passando parametros obtidos no dataframe