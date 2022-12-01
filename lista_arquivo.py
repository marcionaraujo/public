import os

def listar():
    
    diretorio = os.getcwd()
    arquivos = os.listdir()

    print(f'\nForam encontrados os seguintes arquivos ou diretórios no diretório "{diretorio}":')

    for arquivo in arquivos:
        print(f' {arquivo}')

    return arquivos
