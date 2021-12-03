import re


class ConversorMoeda:
    @staticmethod
    def converter_moeda(quantidade, moeda_origem):
        if moeda_origem == 'real':
            valor = float(quantidade) / 5.50
        else:
            valor = float(quantidade) * 5.50
        return round(valor, 2)


class ExtratorURL(ConversorMoeda):
    def __init__(self, url):
        self.url = url
        self.valida_url()

    def get_url_parametros(self):
        indice_parametros = self.url.find("?")
        url_parametros = self.url[indice_parametros + 1:]
        return url_parametros

    def get_url_base(self):
        indice_parametros = self.url.find("?")
        url_base = self.url[:indice_parametros]
        return url_base

    def valida_url(self):
        url_padrao = re.compile("(http(s)?://)?bytebank.com(.br)?/cambio?")
        match = url_padrao.match(self.url)
        if not match:
            raise ValueError("URL Inválida")
        else:
            pass  # URL Válida

    def get_valor_parametro(self, parametro):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        valor_parametro_left_sliced = url_parametros[indice_valor:]

        if "&" in valor_parametro_left_sliced:
            valor_parametro = valor_parametro_left_sliced[:valor_parametro_left_sliced.find("&")]
        else:
            valor_parametro = valor_parametro_left_sliced
        return valor_parametro


# Script

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais

extrator_url = ExtratorURL(url)
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

print(extrator_url.converter_moeda(quantidade, moeda_origem))
