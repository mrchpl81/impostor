# partida.py

import random

class Partida:
    def __init__(self, num_jugadores, palabra_secreta):
        self.num_jugadores = num_jugadores
        self.palabra_secreta = palabra_secreta
        self.impostor_index = random.randint(0, num_jugadores - 1)
        # 0 es el primer jugador
        self.asignar_roles()
        self.votos = [0] * num_jugadores

    def asignar_roles(self):
        # El impostor no conoce la palabra
        self.roles = []
        for i in range(self.num_jugadores):
            if i == self.impostor_index:
                self.roles.append('impostor')
            else:
                self.roles.append('civil')

    def get_rol(self, jugador):
        return self.roles[jugador]

    def votar(self, jugador_expulsado):
        self.votos[jugador_expulsado] += 1

    def resultado_votacion(self):
        max_votos = max(self.votos)
        expulsados = [i for i, v in enumerate(self.votos) if v == max_votos]
        # Si hay empate entre varios, elige uno al azar
        expulsado = random.choice(expulsados)
        return expulsado, self.roles[expulsado] == 'impostor'