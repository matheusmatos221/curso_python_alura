class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, value):
        self.__nome = value
