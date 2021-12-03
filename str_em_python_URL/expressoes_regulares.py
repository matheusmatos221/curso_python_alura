# Exemplos de URLs válidas:
#     bytebank.com/cambio
#     bytebank.com.br/cambio
#     www.bytebank.com/cambio
#     www.bytebank.com.br/cambio
#     http://www.bytebank.com/cambio
#     http://www.bytebank.com.br/cambio
#     https://www.bytebank.com/cambio
#     https://www.bytebank.com.br/cambio
#
# Exemplos de URL inválidas:
#     https://bytebank/cambio
#     http://bytebank.naoexiste/cambio
#     ht:bytebank.naoexiste/cambio

import re

url = "bytebank.com.br/cambio"
padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao.match(url)

if not match:
    raise ValueError("URL Inválida")
else:
    print("URL Válida")