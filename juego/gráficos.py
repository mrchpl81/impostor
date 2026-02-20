# gráficos.py

import tkinter as tk
from tkinter import messagebox

class VentanaJuego:
    def __init__(self, partida, master=None, callback_nueva_partida=None):
        self.partida = partida
        self.master = master or tk.Tk()
        self.jugador_actual = 0
        self.palabras = []
        self.votos = [0] * self.partida.num_jugadores
        self.callback_nueva_partida = callback_nueva_partida

        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.iniciar_pantalla()

    def iniciar_pantalla(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(self.frame, text=f"Jugador {self.jugador_actual + 1}, haz clic para ver tu rol", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.frame, text="Ver rol", command=self.mostrar_rol, font=("Arial", 12), width=20).pack(pady=10)

    def mostrar_rol(self):
        rol = self.partida.get_rol(self.jugador_actual)
        if rol == 'impostor':
            texto = "¡Eres el impostor! Intenta pasar desapercibido."
        else:
            texto = f"Eres civil. La palabra secreta es: '{self.partida.palabra_secreta}'"
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(self.frame, text=texto, font=("Arial", 12), wraplength=400, justify=tk.CENTER).pack(pady=20)
        tk.Button(self.frame, text="Siguiente", command=self.siguiente_jugador_rol, font=("Arial", 12), width=20).pack(pady=10)

    def siguiente_jugador_rol(self):
        self.jugador_actual += 1
        if self.jugador_actual < self.partida.num_jugadores:
            self.iniciar_pantalla()
        else:
            self.jugador_actual = 0
            self.pedir_palabra()

    def pedir_palabra(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(self.frame, text=f"Jugador {self.jugador_actual + 1}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame, text="Escribe una palabra relacionada (o disimula si eres impostor):", font=("Arial", 11)).pack(pady=10)
        self.entrada = tk.Entry(self.frame, font=("Arial", 12), width=25)
        self.entrada.pack(pady=10)
        tk.Button(self.frame, text="Enviar", command=self.guardar_palabra, font=("Arial", 12), width=20).pack(pady=10)

    def guardar_palabra(self):
        palabra = self.entrada.get()
        if not palabra.strip():
            messagebox.showwarning("Error", "¡Debes ingresar una palabra!")
            return
        self.palabras.append((self.jugador_actual, palabra))
        self.jugador_actual += 1
        if self.jugador_actual < self.partida.num_jugadores:
            self.pedir_palabra()
        else:
            self.jugador_actual = 0
            self.mostrar_palabras_para_votar()

    def mostrar_palabras_para_votar(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(self.frame, text="Palabras dichas:", font=("Arial", 14)).pack(pady=10)
        
        for idx, (jugador, palabra) in enumerate(self.palabras):
            tk.Label(self.frame, text=f"Jugador {jugador + 1}: {palabra}", font=("Arial", 11)).pack(pady=5)
        
        tk.Label(self.frame, text="¿A quién quieres expulsar?", font=("Arial", 12)).pack(pady=15)
        
        for i in range(self.partida.num_jugadores):
            tk.Button(self.frame, text=f"Jugador {i + 1}", command=lambda i=i: self.votar_expulsar(i), font=("Arial", 11), width=20).pack(pady=5)

    def votar_expulsar(self, expulsado):
        self.votos[expulsado] += 1
        self.jugador_actual += 1
        if self.jugador_actual < self.partida.num_jugadores:
            self.mostrar_palabras_para_votar()
        else:
            # Final de ronda: contar votos
            expulsado_idx, es_impostor = self.partida.resultado_votacion()
            self.mostrar_resultado(expulsado_idx, es_impostor)

    def mostrar_resultado(self, expulsado_idx, es_impostor):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Mostrar resultado de votación
        if es_impostor:
            mensaje = f"¡El jugador {expulsado_idx + 1} era el impostor! ¡Ganasteis!"
            color_texto = "green"
        else:
            mensaje = f"El jugador {expulsado_idx + 1} no era el impostor. ¡El impostor ha ganado!"
            color_texto = "red"
        
        tk.Label(self.frame, text=mensaje, font=("Arial", 14, "bold"), fg=color_texto).pack(pady=20)
        
        # Mostrar quién era quién
        tk.Label(self.frame, text="REVELACIÓN DE ROLES:", font=("Arial", 12, "bold")).pack(pady=10)
        
        for i in range(self.partida.num_jugadores):
            rol = self.partida.get_rol(i)
            if rol == 'impostor':
                rol_texto = "IMPOSTOR 🎭"
                color = "red"
            else:
                rol_texto = "CIVIL ✓"
                color = "blue"
            tk.Label(self.frame, text=f"Jugador {i + 1}: {rol_texto}", font=("Arial", 11), fg=color).pack(pady=5)
        
        # Botones para nueva partida
        tk.Label(self.frame, text="", font=("Arial", 5)).pack()
        tk.Button(self.frame, text="Nueva Partida", command=self.nueva_partida, font=("Arial", 12), width=20, bg="green", fg="white").pack(pady=10)
        tk.Button(self.frame, text="Salir", command=self.master.quit, font=("Arial", 12), width=20, bg="red", fg="white").pack(pady=5)

    def nueva_partida(self):
        if self.callback_nueva_partida:
            self.callback_nueva_partida()