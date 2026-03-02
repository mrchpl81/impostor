# partida.py - Lógica del juego El Impostor

import random

class Partida:
    def __init__(self, num_jugadores, palabra_secreta, num_impostores=1):
        """
        Inicializa una nueva partida
        
        Args:
            num_jugadores: Número de jugadores (mínimo 3)
            palabra_secreta: Palabra que conocen los civiles
            num_impostores: Número de impostores (mínimo 1)
        """
        self.num_jugadores = num_jugadores
        self.palabra_secreta = palabra_secreta
        self.num_impostores = min(num_impostores, num_jugadores - 1)  # Máximo n-1
        
        # Asignar roles de forma aleatoria
        roles = ['civil'] * (num_jugadores - self.num_impostores) + ['impostor'] * self.num_impostores
        random.shuffle(roles)
        self.roles = roles
        
        # Los índices de los impostores
        self.impostores_index = [i for i, rol in enumerate(roles) if rol == 'impostor']
        
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
    
    def es_impostor(self, indice_jugador):
        """Verifica si un jugador es impostor"""
        return self.roles[indice_jugador] == 'impostor'
    
    def resultado_votacion(self):
        """
        Determina el resultado de la votación
        
        Returns:
            Tupla (indice_expulsado, civiles_ganan)
        """
        # El jugador expulsado es el que recibió más votos
        max_votos = 0
        expulsado = 0
        
        for i in range(self.num_jugadores):
            votos_jugador = 0
        
        expulsado = 0
        
        # Los civiles ganan si expulsan a UN impostor y quedan más civiles que impostores
        # Los impostores ganan si quedan igual o más impostores que civiles
        
        if self.roles[expulsado] == 'impostor':
            # Se expulsó a un impostor
            impostores_restantes = self.num_impostores - 1
            civiles_restantes = (self.num_jugadores - self.num_impostores)
            civiles_ganan = impostores_restantes == 0  # Civiles ganan si no quedan impostores
        else:
            civiles_ganan = False
        
        return expulsado, civiles_ganan
    
    def obtener_todos_los_roles(self):
        """
        Retorna todos los roles para mostrar al final
        
        Returns:
            Lista de roles
        """
        return self.roles