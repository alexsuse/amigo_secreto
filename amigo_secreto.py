#!/usr/bin/python

import random

class Pessoa:
    def __init__(self, nome, email, numero):
        self._nome = nome
        self._email = email
        self._numero = numero

class Restricao:
    def __init__(self, pessoa1, pessoa2):
        self._pessoa1 = pessoa1
        self._pessoa2 = pessoa2

    def verifica(self, pessoas):
        for i in range(len(pessoas)):
            if (self._pessoa1 == pessoas[i]._nome) and (self._pessoa2 == pessoas[(i+1)%len(pessoas)]._nome):
                return False
            if (self._pessoa1 == pessoas[(i+1)%len(pessoas)]._nome) and (self._pessoa2 == pessoas[i]._nome):
                return False
        return True


class Jogo:
    def __init__(self, pessoas):
        self._pessoas = pessoas
        self._restricoes = []

    def verifica(self, sorteio):
        for rest in self._restricoes:
            if not rest.verifica(sorteio):
                return False
        return True

    def sorteia(self):
        random.shuffle(self._pessoas)
        while not self.verifica(self._pessoas):
            random.shuffle(self._pessoas)
        return self._pessoas

    def adiciona_restricao(self, restricao):
        self._restricoes.append(restricao)


if __name__ == "__main__":
    pessoas = [Pessoa("Alex", "alexsusemihl@gmail.com", "031975572505"),
               Pessoa("Fernanda", "fefesusemihl@gmail.com", "031993501307"),
               Pessoa("Elsa", "esusemihl@gmail.com", "011982939956"),
               Pessoa("Christian", "susemihl@gmail.com", "011982332543"),
               Pessoa("Mathias", "mathiassusemihl@gmail.com", ""),
               Pessoa("Natalia", "nathaliaestima@gmail.com", ""),
               Pessoa("Corny", "comercial@concerto.com.br", ""),
               Pessoa("Cito", "comercial@concerto.com.br", ""),
               Pessoa("Pathy", "pathy@gmail.com", ""),
               Pessoa("Carlos", "carloskunze@gmail.com", ""),
               Pessoa("Vera", "verakunze@gmail.com", ""),
               Pessoa("Patrick", "patrickkunze@gmail.com", ""),
               Pessoa("Anthony", "anthony@gmail.com", ""),
               Pessoa("Kurt (Opa)", "kunzetrad@uol.com.br", ""),
               Pessoa("Edith (Dita)", "kunzetrad@uol.com.br", ""),
               Pessoa("Vanio", "vanioestima@gmail.com", ""),
               Pessoa("Sara", "saraoleiro@gmail.com", ""),
               Pessoa("Sandra", "sandraproenca@gmail.com", ""),
               Pessoa("Fernando Proenca", "fernando@proencas.com", "011999113777"),
               Pessoa("Marcelo", "marcelokunze@gmail.com", "")]

    jogo = Jogo(pessoas)

    jogo.adiciona_restricao(Restricao("Sara", "Patrick"))
    jogo.adiciona_restricao(Restricao("Vanio", "Patrick"))
    jogo.adiciona_restricao(Restricao("Sandra", "Patrick"))
    jogo.adiciona_restricao(Restricao("Fernando", "Patrick"))
    jogo.adiciona_restricao(Restricao("Sara", "Marcelo"))
    jogo.adiciona_restricao(Restricao("Vanio", "Marcelo"))
    jogo.adiciona_restricao(Restricao("Sandra", "Marcelo"))
    jogo.adiciona_restricao(Restricao("Fernando", "Marcelo"))
    jogo.adiciona_restricao(Restricao("Sara", "Anthony"))
    jogo.adiciona_restricao(Restricao("Vanio", "Anthony"))
    jogo.adiciona_restricao(Restricao("Sandra", "Anthony"))
    jogo.adiciona_restricao(Restricao("Fernando", "Anthony"))

    sorteio = jogo.sorteia()
    for i, pessoa in enumerate(sorteio):
        print "{}, seu amig@ secret@ e: {}".format(sorteio[i]._nome, sorteio[(i+1)%len(sorteio)]._nome)
