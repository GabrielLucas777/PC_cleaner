


# Limpador de Arquivos Temporários (Windows)

Este projeto é um utilitário em Python desenvolvido para analisar, registrar e limpar arquivos temporários no Windows.
Ele percorre a pasta Temp do usuário, verifica o estado dos arquivos (tamanho, permissões e possibilidade de leitura) e registra tudo no arquivo `log.txt`.

É útil para:

* Manter o sistema limpo
* Recuperar espaço em disco
* Automatizar parte de serviços de manutenção e formatação de PCs

---

## Funcionalidades

* Lista todos os arquivos e subpastas dentro da pasta Temp
* Verifica se cada arquivo pode ser aberto (ou está em uso)
* Gera um log claro e legível em `log.txt`
* Calcula o tamanho total analisado
* Calcula o tamanho que pode ser limpo
* Remove automaticamente arquivos desbloqueados
* Exibe um resumo final da limpeza

---

## Estrutura do Log

O arquivo `log.txt` registra:

```
caminho do arquivo | tamanho | status
```

Exemplos de status:

* OK → arquivo pôde ser aberto
* EM USO → arquivo travado por outro processo
* REMOVIDO → arquivo apagado com sucesso

---

## Como funciona

1. A função `limpar_arquivos()` percorre todos os itens da pasta Temp usando `Path.rglob()`.
2. Para cada arquivo encontrado:

   * Verifica se realmente é um arquivo
   * Testa se é possível abrir em modo leitura
   * Caso seja possível, considera seguro para exclusão
   * Caso contrário, assume que está em uso
3. Todas as informações são registradas no log.
4. Os arquivos seguros são removidos.
5. Um resumo final é exibido com o total analisado e total liberado.

---

## Como usar

1. Instale o Python 3.x no Windows.
2. Baixe o projeto ou clone este repositório.
3. Execute o script com o comando:

```
python limpar.py
```

O programa automaticamente:

* Localiza a pasta Temp do usuário
* Analisa os arquivos
* Gera o log
* Remove o que estiver desbloqueado

---

## Aviso

Alguns arquivos temporários podem estar sendo usados por processos ativos.
O script remove apenas arquivos que não estão travados, evitando problemas no sistema.

---

## Melhorias Futuras

* Interface gráfica com Tkinter ou CustomTkinter
* Barra de progresso
* Logs organizados por data
* Modo somente relatório (sem excluir)
* Limpeza de outras pastas temporárias do Windows

---

## Autor

Projeto desenvolvido por Gabriel, com foco em automação prática para serviços de manutenção de computadores.
