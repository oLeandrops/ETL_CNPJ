from requests import get
from bs4 import BeautifulSoup
import os
from shutil import move
from zipfile import ZipFile


url_base =  'http://200.152.38.155/CNPJ/'

rfb = get(url_base).content
soup = BeautifulSoup(rfb,'html.parser')


links = soup.find_all('a')

arquivos = [link.get('href') for link in links if '.zip' in str(link)]

for arquivo in arquivos:
    download = get(url_base+arquivo)
    with open(arquivo,'wb') as novo_arquivo:
        novo_arquivo.write(download.content)

pastas = ['EMPRESAS','ESTABELECIMENTO',
'SOCIOS','SIMPLES','MUNICIPIOS',
'CNAES','QUALIFICACOES','MOTIVOS','NATUREZA','PAISES']

[os.mkdir(pasta) for pasta in pastas]
[move(arquivo,'EMPRESAS') for arquivo in os.listdir() if 'Empresa' in arquivo]
[move(arquivo,'ESTABELECIMENTO') for arquivo in os.listdir() if 'Estabeleci' in arquivo]
[move(arquivo,'SOCIOS') for arquivo in os.listdir() if 'Socios' in arquivo]
[move(arquivo,'SIMPLES') for arquivo in os.listdir() if 'Simples' in arquivo]
[move(arquivo,'CNAES') for arquivo in os.listdir() if 'Cnaes' in arquivo]
[move(arquivo,'MOTIVOS') for arquivo in os.listdir() if 'Motivos' in arquivo]
[move(arquivo,'NATUREZA') for arquivo in os.listdir() if 'Naturezas' in arquivo]
[move(arquivo,'PAISES') for arquivo in os.listdir() if 'Paises' in arquivo]
[move(arquivo,'QUALIFICACOES') for arquivo in os.listdir() if 'Qualificacoes' in arquivo]
[move(arquivo,'MUNICIPIOS') for arquivo in os.listdir() if 'Municipios' in arquivo]


for arquivo in os.listdir('EMPRESAS'):
    if '.zip' in arquivo:
        with ZipFile(f'EMPRESAS/{arquivo}') as zip:
            zip.extractall('EMPRESAS/')
        os.remove(f'EMPRESAS/{arquivo}')

for arquivo in os.listdir('ESTABELECIMENTO/'):
    if '.zip' in arquivo:
        with ZipFile(f'ESTABELECIMENTO/{arquivo}') as zip:
            zip.extractall('ESTABELECIMENTO/')
        os.remove(f'ESTABELECIMENTO/{arquivo}')

for arquivo in os.listdir('MOTIVOS/'):
    if '.zip' in arquivo:
        with ZipFile(f'MOTIVOS/{arquivo}') as zip:
            zip.extractall('MOTIVOS/')
        os.remove(f'MOTIVOS/{arquivo}')

for arquivo in os.listdir('MUNICIPIOS/'):
    if '.zip' in arquivo:
        with ZipFile(f'MUNICIPIOS/{arquivo}') as zip:
            zip.extractall('MUNICIPIOS/')
        os.remove(f'MUNICIPIOS/{arquivo}')


for arquivo in os.listdir('NATUREZA/'):
    if '.zip' in arquivo:
        with ZipFile(f'NATUREZA/{arquivo}') as zip:
            zip.extractall('NATUREZA/')
        os.remove(f'NATUREZA/{arquivo}')

for arquivo in os.listdir('PAISES/'):
    if '.zip' in arquivo:
        with ZipFile(f'PAISES/{arquivo}') as zip:
            zip.extractall('PAISES/')
        os.remove(f'PAISES/{arquivo}')

for arquivo in os.listdir('QUALIFICACOES/'):
    if '.zip' in arquivo:
        with ZipFile(f'QUALIFICACOES/{arquivo}') as zip:
            zip.extractall('QUALIFICACOES/')
        os.remove(f'QUALIFICACOES/{arquivo}')

for arquivo in os.listdir('SIMPLES/'):
    if '.zip' in arquivo:
        with ZipFile(f'SIMPLES/{arquivo}') as zip:
            zip.extractall('SIMPLES/')
        os.remove(f'SIMPLES/{arquivo}')

for arquivo in os.listdir('SOCIOS/'):
    if '.zip' in arquivo:
        with ZipFile(f'SOCIOS/{arquivo}') as zip:
            zip.extractall('SOCIOS/')
        os.remove(f'SOCIOS/{arquivo}')





