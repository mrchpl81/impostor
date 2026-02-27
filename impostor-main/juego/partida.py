# partida.py - Lógica del juego El Impostor

import random

class Partida:
    def __init__(self, num_jugadores, palabra_secreta):
        """
        Inicializa una nueva partida
        
        Args:
            num_jugadores: Número de jugadores (mínimo 3)
            palabra_secreta: Palabra que conocen los civiles
        """
        self.num_jugadores = num_jugadores
        self.palabra_secreta = palabra_secreta
        
        # Asignar roles de forma aleatoria
        roles = ['civil'] * (num_jugadores - 1) + ['impostor']
        random.shuffle(roles)
        self.roles = roles
        
        # El índice del impostor
        self.impostor_index = self.roles.index('impostor')
        
        # Variable para almacenar votos
        self.votos = []
    
    def get_rol(self, indice_jugador):
        """
        Obtiene el rol de un jugador específico
        
        Args:
            indice_jugador: Índice del jugador (0 a num_jugadores-1)
            
        Returns:
            'impostor' o 'civil'
        """
        if 0 <= indice_jugador < len(self.roles):
            return self.roles[indice_jugador]
        return None
    
    def resultado_votacion(self):
        """
        Determina el resultado de la votación
        
        Returns:
            Tupla (indice_expulsado, era_impostor)
        """
        # El jugador expulsado es el que recibió más votos
        # Por ahora usamos una lógica simple: el primero votado
        
        max_votos = 0
        expulsado = 0
        
        for i in range(self.num_jugadores):
            # Contar votos para cada jugador
            votos_jugador = 0
            # Esta es una simplificación - en la práctica
            # deberías pasar los votos desde gráficos.py
            votos_jugador = i  # Placeholder
        
        # El expulsado es quien más votos recibió
        expulsado = 0  # Aquí va la lógica real
        era_impostor = self.roles[expulsado] == 'impostor'
        
        return expulsado, era_impostor
    
    def obtener_todos_los_roles(self):
        """
        Retorna todos los roles para mostrar al final
        
        Returns:
            Lista de roles
        """
        return self.roles