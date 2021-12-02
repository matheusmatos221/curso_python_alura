# Fatiamento (slicing)

# URL
url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Separa a URL em URL Base e URL Parâmetros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Indices do parâmetro de busca e do valor do parâmetro
parametro_busca = "moedaDestino"
indice_parametro_busca = url_parametros.find(parametro_busca)
indice_valor = indice_parametro_busca + len(parametro_busca) + 1

# Left slice
valor = url_parametros[indice_valor:]

# Right slice
if valor.find("&") == -1:
    pass
else:
    valor = valor[:valor.find("&")]

# Print valor
print(f'O valor do parâmetro ¨{parametro_busca}¨ é: {valor}')