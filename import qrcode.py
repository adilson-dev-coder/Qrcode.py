#O intuito do código abaixo é gerar de maneira simples e com poucas linhas um QRcode baseado na biblioteca Qrcode do Python#

import qrcode

#(pip install qrcode) Biblioteca utilizada para fazer a importação do gerador de QRcode.#
#Para instalar a mesma, abrir novo terminal e colar o "pip install qrcode"

img = qrcode.make("Url da pagina")
#refere-se ao tipo de imagem criada e o endereço da pagina propriamente dita#

img.save("nome do arquivo.jpg")
#Nome de como o arquivo de imagem gerado, será salvo# 
