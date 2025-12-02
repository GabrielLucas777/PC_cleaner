O primeiro passo do programa vai ser medir as pastas temporárias do usuário e do sistema, medir e registrar antes. limpar as pastas de forma segura dos arquivos que não estiverem em lock(já em processo de execução pelo sistema) e do cache dos navegadores.
- Pular os arquivos que estiverem em lock e passar pro proximo sem forçar a remoção.
 - Medir e registrar dps quanto espaço tem, os arquivos removidos e os arquivos que foram pulados por estarem em lock.
  - Gerar o relatório em TXT ou CSV.
  - Vou começar primeiro pela pasta temporária de usuário.

                    NA PRATICA  
 - A pratica funciona do seguinte modo:
 - Listar o caminho da pasta (seja a tem do usuário ou sistema - posso ver o caminho dps)
 - listar os arquivos 
 - tento deletar
 - se estiver em lock eu pulo.
 - conto quantos arquivos foram deletados e o espaço que foi liberado
 - o relatório tem que ter os caminhois que foram feitos, os arquivos apagados e o quanto de espaço foi liberado.