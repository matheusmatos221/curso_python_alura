class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return print("{:02d}/{:02d}/{}".format(self.dia, self.mes, self.ano))

