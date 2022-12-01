# Sua tarefa ´e organizar tais arquivos nas pastas planilhas e documentos de acordo com a extens˜ao do arquivo.
# Use os pacotes OS e SHUTILS da biblioteca padr˜ao do Python para lhe ajudar nesta tarefa.

import os
import shutil

import lista_arquivo
import cria_pastas
import move_arquivos

def main():
    arquivos = lista_arquivo.listar()
    cria_pastas.criar()
    move_arquivos.mover(arquivos)

if __name__ == "__main__":
    main()
