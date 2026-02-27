# graficos.py - Interfaz gráfica del juego

import tkinter as tk
from tkinter import messagebox


class VentanaJuego:
    def __init__(self, partida, master=None, callback_nueva_partida=None):
        self.partida = partida
        self.master = master
        self.callback_nueva_partida = callback_nueva_partida
        
        self.jugador_actual = 0
        self.palabras = []
        self.votos = [0] * partida.num_jugadores
        
        # Colores
        self.color_fondo = "#0f0f1e"
        self.color_secundario = "#1a1a2e"
        self.color_acento = "#e94560"
        self.color_civil = "#00d4ff"
        self.color_impostor = "#ff4757"
        self.color_texto = "#ffffff"
        
        # Configurar ventana
        self.master.geometry("800x600")
        self.master.configure(bg=self.color_fondo)
        self.master.title("El Impostor")
        
        # Limpiar contenido anterior
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Frame principal
        self.frame = tk.Frame(self.master, bg=self.color_fondo)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.mostrar_pantalla_inicial()
    
    def limpiar_frame(self):
        """Limpia todos los widgets del frame"""
        for widget in self.frame.winfo_children():
            widget.destroy()
    
    def mostrar_pantalla_inicial(self):
        """Pantalla inicial - Presenta al jugador"""
        self.limpiar_frame()
        
        # Encabezado
        frame_encabezado = tk.Frame(self.frame, bg=self.color_secundario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="🎭 TURNO DEL JUEGO",
            font=("Arial", 20, "bold"),
            fg=self.color_acento,
            bg=self.color_secundario
        ).pack(pady=15)
        
        # Contenido
        tk.Frame(self.frame, bg=self.color_fondo, height=30).pack()
        
        tk.Label(
            self.frame,
            text=f"JUGADOR {self.jugador_actual + 1}",
            font=("Arial", 18, "bold"),
            fg=self.color_civil,
            bg=self.color_fondo
        ).pack(pady=20)
        
        tk.Frame(self.frame, bg=self.color_acento, height=2).pack(fill=tk.X, padx=50)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=30).pack()
        
        tk.Label(
            self.frame,
            text="Descubre tu rol secreto",
            font=("Arial", 14),
            fg=self.color_texto,
            bg=self.color_fondo
        ).pack(pady=10)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=30).pack()
        
        tk.Button(
            self.frame,
            text="👁️ Ver mi rol",
            command=self.mostrar_rol,
            font=("Arial", 12, "bold"),
            bg=self.color_civil,
            fg=self.color_fondo,
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=20)
    
    def mostrar_rol(self):
        """Muestra el rol asignado al jugador actual"""
        rol = self.partida.get_rol(self.jugador_actual)
        
        self.limpiar_frame()
        
        # Encabezado
        frame_encabezado = tk.Frame(self.frame, bg=self.color_secundario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="🔐 ROL SECRETO",
            font=("Arial", 20, "bold"),
            fg=self.color_acento,
            bg=self.color_secundario
        ).pack(pady=15)
        
        # Contenido
        tk.Frame(self.frame, bg=self.color_fondo, height=20).pack()
        
        # Determinar rol
        if rol == 'impostor':
            color_rol = self.color_impostor
            titulo = "⚠️ ERES EL IMPOSTOR"
            descripcion = ("Intenta pasar desapercibido\n"
                          "No conoces la palabra secreta\n"
                          "Disimula bien")
        else:
            color_rol = self.color_civil
            titulo = "✓ ERES CIVIL"
            descripcion = f"La palabra secreta es:\n\n'{self.partida.palabra_secreta}'"
        
        # Card de rol
        frame_rol = tk.Frame(self.frame, bg=color_rol, relief=tk.RAISED, bd=3)
        frame_rol.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        tk.Frame(frame_rol, bg=self.color_fondo, height=20).pack()
        
        tk.Label(
            frame_rol,
            text=titulo,
            font=("Arial", 18, "bold"),
            fg=self.color_fondo,
            bg=color_rol
        ).pack(pady=20)
        
        tk.Frame(frame_rol, bg=self.color_fondo, height=2).pack(fill=tk.X, padx=40)
        
        tk.Label(
            frame_rol,
            text=descripcion,
            font=("Arial", 12),
            fg=self.color_fondo,
            bg=color_rol,
            justify=tk.CENTER
        ).pack(pady=25)
        
        tk.Frame(frame_rol, bg=self.color_fondo, height=20).pack()
        
        tk.Frame(self.frame, bg=self.color_fondo, height=20).pack()
        
        tk.Button(
            self.frame,
            text="➜ Siguiente jugador",
            command=self.siguiente_jugador,
            font=("Arial", 12, "bold"),
            bg=self.color_civil,
            fg=self.color_fondo,
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=20)
    
    def siguiente_jugador(self):
        """Avanza al siguiente jugador"""
        self.jugador_actual += 1
        
        if self.jugador_actual < self.partida.num_jugadores:
            self.mostrar_pantalla_inicial()
        else:
            self.jugador_actual = 0
            self.pedir_palabra()
    
    def pedir_palabra(self):
        """Pide una palabra a cada jugador"""
        self.limpiar_frame()
        
        # Encabezado
        frame_encabezado = tk.Frame(self.frame, bg=self.color_secundario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="🗣️ TURNO DE PALABRA",
            font=("Arial", 20, "bold"),
            fg=self.color_acento,
            bg=self.color_secundario
        ).pack(pady=15)
        
        # Contenido
        tk.Frame(self.frame, bg=self.color_fondo, height=20).pack()
        
        tk.Label(
            self.frame,
            text=f"Jugador {self.jugador_actual + 1}",
            font=("Arial", 16, "bold"),
            fg=self.color_civil,
            bg=self.color_fondo
        ).pack(pady=15)
        
        tk.Label(
            self.frame,
            text="Di una palabra relacionada:",
            font=("Arial", 12),
            fg=self.color_texto,
            bg=self.color_fondo
        ).pack(pady=10)
        
        if self.jugador_actual == self.partida.impostor_index:
            tk.Label(
                self.frame,
                text="(¡Eres impostor, disimula! 😉)",
                font=("Arial", 10),
                fg=self.color_impostor,
                bg=self.color_fondo
            ).pack(pady=5)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        # Campo de entrada
        self.entrada = tk.Entry(
            self.frame,
            font=("Arial", 13),
            width=25,
            bg=self.color_secundario,
            fg=self.color_texto,
            relief=tk.SUNKEN,
            bd=2
        )
        self.entrada.pack(pady=15, ipady=8)
        self.entrada.focus()
        self.entrada.bind('<Return>', lambda e: self.guardar_palabra())
        
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        tk.Button(
            self.frame,
            text="✓ Enviar palabra",
            command=self.guardar_palabra,
            font=("Arial", 12, "bold"),
            bg=self.color_civil,
            fg=self.color_fondo,
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=20)
    
    def guardar_palabra(self):
        """Guarda la palabra ingresada"""
        palabra = self.entrada.get().strip()
        
        if not palabra:
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
        """Muestra todas las palabras y permite votar"""
        self.limpiar_frame()
        
        # Encabezado
        frame_encabezado = tk.Frame(self.frame, bg=self.color_secundario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="📊 ANÁLISIS DE PALABRAS",
            font=("Arial", 20, "bold"),
            fg=self.color_acento,
            bg=self.color_secundario
        ).pack(pady=15)
        
        # Contenido
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        tk.Label(
            self.frame,
            text="Palabras dichas:",
            font=("Arial", 12, "bold"),
            fg=self.color_texto,
            bg=self.color_fondo
        ).pack(pady=10)
        
        # Frame con palabras
        frame_palabras = tk.Frame(self.frame, bg=self.color_secundario, relief=tk.SUNKEN, bd=2)
        frame_palabras.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        for jugador, palabra in self.palabras:
            frame_palabra = tk.Frame(frame_palabras, bg=self.color_secundario)
            frame_palabra.pack(fill=tk.X, padx=10, pady=8)
            
            tk.Label(
                frame_palabra,
                text=f"👤 Jugador {jugador + 1}:",
                font=("Arial", 10, "bold"),
                fg=self.color_civil,
                bg=self.color_secundario
            ).pack(side=tk.LEFT, padx=5)
            
            tk.Label(
                frame_palabra,
                text=f'"{palabra}"',
                font=("Arial", 10, "italic"),
                fg=self.color_acento,
                bg=self.color_secundario
            ).pack(side=tk.LEFT, padx=5)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        tk.Label(
            self.frame,
            text="¿A quién expulsas?",
            font=("Arial", 13, "bold"),
            fg=self.color_impostor,
            bg=self.color_fondo
        ).pack(pady=10)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=10).pack()
        
        # Botones de votación
        frame_botones = tk.Frame(self.frame, bg=self.color_fondo)
        frame_botones.pack(fill=tk.BOTH, expand=True, padx=30)
        
        for i in range(self.partida.num_jugadores):
            tk.Button(
                frame_botones,
                text=f"🚫 Jugador {i + 1}",
                command=lambda i=i: self.votar_expulsar(i),
                font=("Arial", 10, "bold"),
                bg=self.color_impostor,
                fg=self.color_texto,
                width=28,
                height=2,
                relief=tk.RAISED,
                bd=2,
                cursor="hand2"
            ).pack(pady=5)
    
    def votar_expulsar(self, indice_expulsado):
        """Registra el voto y avanza"""
        self.votos[indice_expulsado] += 1
        self.jugador_actual += 1
        
        if self.jugador_actual < self.partida.num_jugadores:
            self.mostrar_palabras_para_votar()
        else:
            # Encontrar quién tiene más votos
            max_votos = max(self.votos)
            expulsado = self.votos.index(max_votos)
            es_impostor = self.partida.get_rol(expulsado) == 'impostor'
            
            self.mostrar_resultado(expulsado, es_impostor)
    
    def mostrar_resultado(self, expulsado_idx, es_impostor):
        """Muestra el resultado final de la partida"""
        self.limpiar_frame()
        
        # Encabezado
        frame_encabezado = tk.Frame(self.frame, bg=self.color_secundario)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            frame_encabezado,
            text="🎬 RESULTADO FINAL",
            font=("Arial", 20, "bold"),
            fg=self.color_acento,
            bg=self.color_secundario
        ).pack(pady=15)
        
        # Contenido
        tk.Frame(self.frame, bg=self.color_fondo, height=20).pack()
        
        # Determinar resultado
        if es_impostor:
            color_resultado = self.color_civil
            mensaje = f"¡JUGADOR {expulsado_idx + 1} ERA EL IMPOSTOR!"
            submensaje = "¡CIVILES GANAN! 🎉"
        else:
            color_resultado = self.color_impostor
            mensaje = f"¡JUGADOR {expulsado_idx + 1} NO ERA IMPOSTOR!"
            submensaje = "¡IMPOSTOR GANA! 😈"
        
        # Card de resultado
        frame_resultado = tk.Frame(self.frame, bg=color_resultado, relief=tk.RAISED, bd=3)
        frame_resultado.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        tk.Frame(frame_resultado, bg=self.color_fondo, height=15).pack()
        
        tk.Label(
            frame_resultado,
            text=mensaje,
            font=("Arial", 14, "bold"),
            fg=self.color_fondo,
            bg=color_resultado
        ).pack(pady=15)
        
        tk.Label(
            frame_resultado,
            text=submensaje,
            font=("Arial", 18, "bold"),
            fg=self.color_fondo,
            bg=color_resultado
        ).pack(pady=20)
        
        tk.Frame(frame_resultado, bg=self.color_fondo, height=15).pack()
        
        # Roles revelados
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        tk.Label(
            self.frame,
            text="ROLES REVELADOS",
            font=("Arial", 12, "bold"),
            fg=self.color_acento,
            bg=self.color_fondo
        ).pack(pady=10)
        
        frame_roles = tk.Frame(self.frame, bg=self.color_secundario, relief=tk.SUNKEN, bd=2)
        frame_roles.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        for i in range(self.partida.num_jugadores):
            rol = self.partida.get_rol(i)
            
            if rol == 'impostor':
                rol_texto = "🎭 IMPOSTOR"
                color = self.color_impostor
            else:
                rol_texto = "✓ CIVIL"
                color = self.color_civil
            
            frame_rol = tk.Frame(frame_roles, bg=self.color_secundario)
            frame_rol.pack(fill=tk.X, padx=10, pady=8)
            
            tk.Label(
                frame_rol,
                text=f"Jugador {i + 1}:",
                font=("Arial", 10, "bold"),
                fg=self.color_texto,
                bg=self.color_secundario,
                width=15,
                anchor="w"
            ).pack(side=tk.LEFT, padx=5)
            
            tk.Label(
                frame_rol,
                text=rol_texto,
                font=("Arial", 10, "bold"),
                fg=color,
                bg=self.color_secundario
            ).pack(side=tk.LEFT, padx=5)
        
        tk.Frame(self.frame, bg=self.color_fondo, height=15).pack()
        
        # Botones finales
        frame_botones = tk.Frame(self.frame, bg=self.color_fondo)
        frame_botones.pack(pady=15)
        
        tk.Button(
            frame_botones,
            text="🔄 Nueva Partida",
            command=self.nueva_partida,
            font=("Arial", 11, "bold"),
            bg=self.color_civil,
            fg=self.color_fondo,
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=5)
        
        tk.Button(
            frame_botones,
            text="❌ Salir",
            command=self.master.quit,
            font=("Arial", 11, "bold"),
            bg="#d32f2f",
            fg=self.color_texto,
            width=25,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(pady=5)
    
    def nueva_partida(self):
        """Inicia una nueva partida"""
        if self.callback_nueva_partida:
            self.callback_nueva_partida()