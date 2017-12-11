#!/usr/bin/python

import random
import quickstart

class Pessoa:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

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
    pessoas = [Pessoa("Alex", "alexsusemihl@gmail.com"),
               Pessoa("Fernanda", "fefesusemihl@gmail.com"),
               Pessoa("Elsa", "esusemihl@gmail.com"),
               Pessoa("Christian", "susemihl@gmail.com"),
               Pessoa("Mathias", "mathiassusemihl@gmail.com"),
               Pessoa("Natalia", "nataliaestima@gmail.com"),
               Pessoa("Cornelia (Corny)", "comercial@concerto.com.br"),
               Pessoa("Nelson (Cito)", "direcao@concerto.com.br"),
               Pessoa("Patricia", "patriciakunze76@gmail.com"),
               Pessoa("Carlos", "carlos.kunze@ig.com.br"),
               Pessoa("Vera", "vera.kunze@ig.com.br"),
               Pessoa("Patrick", "ppkunze@gmail.com"),
               Pessoa("Anthony", "arkunze@hotmail.com"),
               Pessoa("Kurt (Opa)", "kunzetrad@uol.com.br"),
               Pessoa("Edith (Dita)", "kunzetrad@uol.com.br"),
               Pessoa("Vanio", "vno@mandic.com.br"),
               Pessoa("Sara", "sara@saraoleiro.com.br"),
               Pessoa("Sandra", "sandra1@uol.com.br"),
               Pessoa("Fernando", "fernando@proencas.com"),
               Pessoa("Marcelo", "marcelokunze220@gmail.com"),
               Pessoa("Omi", "susemihl@gmail.com")]

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

    random.seed(12347)

    sorteio = jogo.sorteia()
    quickstart.send_mail(pessoas)
