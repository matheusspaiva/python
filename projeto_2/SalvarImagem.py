from PIL import Image, ImageFont, ImageDraw
import pandas as pd

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


alunos = pd.read_csv("certificado.csv")
for i in range(0,len(alunos)):
    nome = str(alunos.loc[i, "Nome"])
    diretor = str(alunos.loc[i, "Diretor"])
    professor = str(alunos.loc[i, "Professor"])
    criarImagem(nome,diretor,professor)