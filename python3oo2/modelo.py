class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}'

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Duração: {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Temporadas: {self.temporadas}'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

# Script
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)


# Likes
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

# Polimorfismo
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist(nome="fim de semana", programas=filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tu tá ou não tá? {tmep in playlist_fim_de_semana}')
