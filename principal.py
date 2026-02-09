# principal.py

import tkinter as tk
from tkinter import messagebox
from gráficos import VentanaJuego
from partida import Partida

class AplicacionJuego:
    def __init__(self, root):
        self.root = root
        self.root.title("El Impostor - Juego en Local")
        self.root.geometry("500x400")
        self.num_jugadores = 0
        self.palabra_secreta = ""
        self.mostrar_pantalla_inicial()

    def mostrar_pantalla_inicial(self):
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="EL IMPOSTOR", font=("Arial", 18, "bold")).pack(pady=20)
        
        tk.Label(self.root, text="Nº de jugadores (mínimo 3):", font=("Arial", 11)).pack(pady=5)
        self.entry_jugadores = tk.Entry(self.root, font=("Arial", 12), width=20)
        self.entry_jugadores.pack(pady=5)
        
        tk.Label(self.root, text="Palabra secreta para los civiles:", font=("Arial", 11)).pack(pady=5)
        self.entry_palabra = tk.Entry(self.root, font=("Arial", 12), width=20)
        self.entry_palabra.pack(pady=5)
        
        tk.Button(self.root, text="Iniciar juego", command=self.iniciar_juego, font=("Arial", 12), width=20, bg="green", fg="white").pack(pady=20)

    def iniciar_juego(self):
        try:
            self.num_jugadores = int(self.entry_jugadores.get())
            self.palabra_secreta = self.entry_palabra.get().strip()
            
            if self.num_jugadores < 3:
                messagebox.showerror("Error", "Número mínimo de jugadores: 3")
                return
            if not self.palabra_secreta:
                messagebox.showerror("Error", "Introduce una palabra secreta.")
                return
            
            # Crear partida y mostrar juego
            partida = Partida(self.num_jugadores, self.palabra_secreta)
            VentanaJuego(partida, self.root, callback_nueva_partida=self.mostrar_pantalla_inicial)
        
        except ValueError:
            messagebox.showerror("Error", "El número de jugadores debe ser un número entero.")

def main():
    root = tk.Tk()
    app = AplicacionJuego(root)
    root.mainloop()

if __name__ == "__main__":
    main()