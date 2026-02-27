# principal.py - Aplicación principal

import tkinter as tk
from tkinter import messagebox
from graficos import VentanaJuego
from partida import Partida


class AplicacionJuego:
    def __init__(self, root):
        self.root = root
        self.root.title("El Impostor")
        self.root.geometry("800x600")
        self.root.configure(bg="#0f0f1e")
        
        # Crear marco principal
        self.frame_principal = tk.Frame(self.root, bg="#0f0f1e")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        self.mostrar_pantalla_inicial()
    
    def mostrar_pantalla_inicial(self):
        """Muestra la pantalla inicial de configuración"""
        
        # Limpiar contenido anterior
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        
        # Título
        tk.Label(
            self.frame_principal,
            text="🎭 EL IMPOSTOR",
            font=("Arial", 28, "bold"),
            fg="#e94560",
            bg="#0f0f1e"
        ).pack(pady=30)
        
        # Línea decorativa
        tk.Frame(self.frame_principal, bg="#e94560", height=2).pack(fill=tk.X, padx=50, pady=10)
        
        # Texto de bienvenida
        tk.Label(
            self.frame_principal,
            text="Configura tu partida",
            font=("Arial", 14),
            fg="#ffffff",
            bg="#0f0f1e"
        ).pack(pady=20)
        
        # Campo: Número de jugadores
        tk.Label(
            self.frame_principal,
            text="Número de jugadores (mínimo 3):",
            font=("Arial", 11),
            fg="#ffffff",
            bg="#0f0f1e"
        ).pack(pady=10)
        
        self.entry_jugadores = tk.Entry(
            self.frame_principal,
            font=("Arial", 12),
            width=25,
            bg="#16213e",
            fg="#ffffff",
            relief=tk.SUNKEN,
            bd=2
        )
        self.entry_jugadores.pack(pady=5)
        self.entry_jugadores.insert(0, "3")
        
        # Campo: Palabra secreta
        tk.Label(
            self.frame_principal,
            text="Palabra secreta para los civiles:",
            font=("Arial", 11),
            fg="#ffffff",
            bg="#0f0f1e"
        ).pack(pady=(20, 10))
        
        self.entry_palabra = tk.Entry(
            self.frame_principal,
            font=("Arial", 12),
            width=25,
            bg="#16213e",
            fg="#ffffff",
            relief=tk.SUNKEN,
            bd=2
        )
        self.entry_palabra.pack(pady=5)
        self.entry_palabra.insert(0, "Ejemplo")
        
        # Botón iniciar
        tk.Button(
            self.frame_principal,
            text="🚀 INICIAR JUEGO",
            command=self.iniciar_juego,
            font=("Arial", 12, "bold"),
            bg="#e94560",
            fg="#ffffff",
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=40)
    
    def iniciar_juego(self):
        """Inicia una nueva partida"""
        try:
            num_jugadores = int(self.entry_jugadores.get())
            palabra_secreta = self.entry_palabra.get().strip()
            
            if num_jugadores < 3:
                messagebox.showerror("Error", "Número mínimo de jugadores: 3")
                return
            
            if not palabra_secreta:
                messagebox.showerror("Error", "Introduce una palabra secreta")
                return
            
            # Crear partida
            partida = Partida(num_jugadores, palabra_secreta)
            
            # Mostrar interfaz del juego
            VentanaJuego(
                partida,
                self.root,
                callback_nueva_partida=self.mostrar_pantalla_inicial
            )
        
        except ValueError:
            messagebox.showerror("Error", "El número de jugadores debe ser un número entero")


def main():
    """Función principal"""
    root = tk.Tk()
    app = AplicacionJuego(root)
    root.mainloop()


if __name__ == "__main__":
    main()