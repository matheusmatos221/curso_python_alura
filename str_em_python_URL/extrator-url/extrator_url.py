class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = url
        self.sanitiza_url()
        self.valida_url()

    def __str__(self):
        """String de exibição da classe"""
        return self.url

    def sanitiza_url(self):
        """Retorna a url removendo espaços em branco."""
        if type(self.url) == str:
            self.url = self.url.strip()
        else:
            self.url = ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        return self.url[self.url.find("?")+1:]

    def valida_parametro(self, parametro):
        """Valida se existe o parâmetro buscado"""
        if self.get_url_parametros().find(parametro + "=") == -1:
            raise AttributeError("Parâmetro inválido")
        else:
            pass


    def get_valor_parametro(self, parametro):
        """Retorna o valor do parametro `parametro_busca`."""
        self.valida_parametro(parametro)
        indice_valor = self.get_url_parametros().find(parametro) + len(parametro) + 1
        valor_left_sliced = self.get_url_parametros()[indice_valor:]  # "100&moedaOrigem=real" or "100" or "real"

        if valor_left_sliced.find("&") != -1:  # "100&moedaOrigem=real"
            valor_sliced = valor_left_sliced[:valor_left_sliced.find("&")]
        else:  # "real"
            valor_sliced = valor_left_sliced
        return valor_sliced


# Script

extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
# extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
