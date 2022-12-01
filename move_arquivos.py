import shutil

def mover(arquivos):    

# 1. Inicializa listagens auxiliares
    planilhas = []
    documentos = []
    outros = []


# 2. Move arquivos

    for arquivo in arquivos:
        
        if '.xls' in arquivo:
            planilhas.append(arquivo)
            shutil.move(arquivo, f"./planilhas/{arquivo}")
            
        elif '.doc' in arquivo:
            documentos.append(arquivo)
            shutil.move(arquivo, f"./documentos/{arquivo}")

        else:
            outros.append(arquivo)

                
# 3. Apresenta o resultado
    
    print(f'\nOs seguintes arquivos no foram movidos para o diretóro de planilhas:')

    for planilha in planilhas:
        print(f' {planilha}')

    print(f'\nOs seguintes arquivos no foram movidos para o diretóro de documentos:')

    for documento in documentos:
        print(f' {documento}')

    print(f'\nOs seguintes arquivos ou diretórios não foram movidos:')

    for outro in outros:
        print(f' {outro}')
