import os

def criar():

    print(f'\nCriação dos diretórios:')
    
    if os.path.exists('documentos') == False:
        os.mkdir('documentos')
        print(f' Foi criado o diretório documentos.')
    else:
        print(f' O diretório documentos já existia.')
        

    if os.path.exists('planilhas') == False:
        os.mkdir('planilhas')
        print(f' Foi criado o diretório planilhas.')
    else:
        print(f' O diretório planilhas já existia.')
