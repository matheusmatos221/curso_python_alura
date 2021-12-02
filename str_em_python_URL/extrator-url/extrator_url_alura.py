class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = url
        self.sanitiza_url()
        self.valida_url()

    def sanitiza_url(self):
        """Retorna a url removendo espaços em branco."""
        if type(self.url) == str:
            self.url = self.url.strip()
        else:
            self.url = ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("URL vazia")
        else:
            pass

    def get_url_base(self):
        """Retorna a base da url."""
        indice_parametros = self.url.find("?")
        return self.url[:indice_parametros]

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_parametros = self.url.find("?")
        return self.url[indice_parametros + 1:]

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        valor = url_parametros[indice_valor:]

        if valor.find("&") == -1:
            return valor
        else:
            return valor[:valor.find("&")]

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)