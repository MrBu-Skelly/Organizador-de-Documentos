import os

pasta_origem = r"c:\Users\Mr.Bu\OneDrive\Área de Trabalho\teste"
arquivos = os.listdir(pasta_origem)

for arquivo in arquivos:

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.replace(".", "")

    if not extensao:
        continue
    
    # Criar caminho da pasta da extensão
    pasta_nova = os.path.join(pasta_origem, extensao)
    
    # Criar pasta se não existir
    if not os.path.exists(pasta_nova):
        os.makedirs(pasta_nova)
    
    # Caminho antigo do arquivo
    caminho_antigo = os.path.join(pasta_origem, arquivo)
    
    # Caminho novo 
    caminho_novo = os.path.join(pasta_nova, arquivo)
    
    # Mover
    os.rename(caminho_antigo, caminho_novo)
    print(f"Movido: {arquivo} -> {extensao}/")