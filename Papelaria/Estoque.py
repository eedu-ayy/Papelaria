import csv
import os

ARQUIVO = "dados/produtos.csv"
CAMPOS = ["codigo", "nome""preço","quantidade"]

def eh_numero(texto):
    texto = texto.strip().replace(",", ".", 1)
    return texto.replace(".", "", 1).isdigit()