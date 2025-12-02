#lógica de limpeza fica aqui - a limpeza vai ocorrer daqui e as funções ficarão aqui 

from pathlib import Path

# Uma função que vai receber um parametro  - Essa é a função de limpeza. 
def limpar_arquivos(caminho):

    # variáveis para cálculos
    tamanho_total_antes = 0
    tamanho_total_depois = 0
    arquivos_removidos = 0

    caminho = Path(caminho)
    arquivos = caminho.rglob('*') # - isso aqui vai percorrer todas as pastas e subpastas. É o iterador

    for arquivo in arquivos:
        if arquivo.is_file():
            print(arquivo)

        # soma o tamanho antes
        try:
            tamanho_total_antes += arquivo.stat().st_size
        except:
            pass

        status = abrir_arquivo(arquivo)  # testa se pode abrir
        log(f"{arquivo} | {arquivo.stat().st_size} bytes | {status}")  # registra no log

        # Se está desbloqueado, pode remover
        if status == "ABERTO":
            try:
                arquivo.unlink()
                arquivos_removidos += 1
                log(f"[REMOVIDO] {arquivo}")
            except Exception as e:
                log(f"[ERRO AO REMOVER] {arquivo} - {e}")
        else:
            log(f"[EM USO / LOCK] {arquivo}")

    # Depois da limpeza, calcular tamanho restante
    for arquivo in caminho.rglob('*'):
        if arquivo.is_file():
            try:
                tamanho_total_depois += arquivo.stat().st_size
            except:
                pass

    # resumo final
    log("========== RESUMO ==========")
    log(f"Tamanho antes: {bytes_para_mb(tamanho_total_antes)} MB")
    log(f"Tamanho depois: {bytes_para_mb(tamanho_total_depois)} MB")
    log(f"Total removido: {bytes_para_mb(tamanho_total_antes - tamanho_total_depois)} MB")
    log(f"Arquivos removidos: {arquivos_removidos}")
    log("============================")


# Função que vai abrir o arquivo achado dentro do caminho
def abrir_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:  # tenta abrir o arquivo
            f.read()  # apenas lê para testar se consegue abrir
        return "ABERTO"
    except Exception as e:
        print(f"Não foi possível abrir {arquivo}: {e}") # - se não consegue abrir, segue em frente.
        return "EM USO / LOCK"


def log(texto): #Função do log. Aqui ela vai gerar um texto
    with open("log.txt", "a") as arquivo:
        arquivo.write(texto + "\n")


# conversão bonita para MB
def bytes_para_mb(valor):
    return round(valor / (1024 * 1024), 2)


limpar_arquivos('C:/Users/Administrator/AppData/Local/Temp')
