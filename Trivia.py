import tkinter as tk
from tkinter import font as tkFont
import random
from PIL import Image, ImageTk
import os
import sys
import pygame

def resource_path(relative_path):
    """ Obtiene ruta absoluta al recurso para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Constantes ---
COLOR_FONDO = "#2c3e50"
COLOR_TEXTO = "#ecf0f1"
COLOR_BOTON_COMENZAR = "#2ecc71"
COLOR_BOTON_HOVER = "#2980b9"
COLOR_BOTON = "#3498db"
COLOR_CORRECTO = "#2ecc71"
COLOR_INCORRECTO = "#e74c3c"

ARCHIVO_SONIDO_CORRECTO = "martillo.wav"
ARCHIVO_SONIDO_INCORRECTO = "fuego.wav"
ARCHIVO_SONIDO_INICIO_TRIVIA = "explosion.wav"
ARCHIVO_MUSICA_TRIVIA = "music.mp3"
ARCHIVO_MUSICA_MENU = "music.mp3"

def obtener_preguntas():
    preguntas = [
        # --- TEMA: TOPOLOGÍAS ---
        {
            "pregunta": "Según el material, ¿qué topología se caracteriza porque todos los nodos se conectan a un medio de transmisión único y lineal?",
            "opciones": ["Estrella", "Anillo", "Bus", "Malla"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "En la topología de bus, ¿qué dispositivo es necesario en los extremos del cable para evitar rebotes de la señal?",
            "opciones": ["Repetidores", "Concentradores (Hubs)", "Switches", "Terminadores"],
            "respuesta_correcta": 4
        },
        {
            "pregunta": "¿Cuál es la principal desventaja de la topología de anillo mencionada en las diapositivas?",
            "opciones": ["Es muy lenta", "La caída de un solo nodo puede paralizar toda la red", "Usa demasiado cable", "No permite conectar muchos dispositivos"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "En una topología de estrella, ¿cuál es el punto crítico de falla que puede inutilizar toda la red?",
            "opciones": ["Un cable de una estación", "Una estación de trabajo", "El concentrador o nodo central", "El terminador"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "Una ventaja de la topología de estrella es que:",
            "opciones": ["Usa muy poco cableado", "No necesita un nodo central", "El fallo de un nodo no afecta al resto de la red", "Todos los nodos tienen la misma jerarquía"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "La disposición física y lógica de las estaciones de una red se conoce como:",
            "opciones": ["Protocolo", "Arquitectura", "Topología", "Segmento"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué topología física se menciona que, lógicamente, puede funcionar como un bus?",
            "opciones": ["Anillo", "Malla", "Doble Anillo", "Estrella"],
            "respuesta_correcta": 4
        },

        # --- TEMA: MÉTODOS DE ACCESO AL MEDIO ---
        {
            "pregunta": "¿Qué método de acceso al medio utiliza un 'testigo electrónico' que se pasa de un host a otro?",
            "opciones": ["CSMA/CD (Detección de portadora)", "Polling (Sondeo)", "Pase de Testigo (Token Ring)", "Acceso Aleatorio"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "En el método CSMA/CD, ¿qué hace una estación si detecta que el medio está ocupado?",
            "opciones": ["Transmite inmediatamente", "Apaga la red", "Debe esperar hasta que el medio esté libre", "Envía una señal de alerta"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "El método Polling o Sondeo se basa en una relación de tipo:",
            "opciones": ["Cliente-Servidor", "Peer-to-Peer (P2P)", "Maestro-Esclavo", "Anárquica"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "En una topología de anillo, el método de acceso que consiste en que un nodo central dé permiso para transmitir se llama:",
            "opciones": ["Token Ring", "CSMA/CD", "Sondeo (Polling)", "Ethernet"],
            "respuesta_correcta": 3
        },

        # --- TEMA: MODELO OSI ---
        {
            "pregunta": "¿En qué capa del modelo OSI operan los Routers?",
            "opciones": ["Capa de Enlace de Datos (Capa 2)", "Capa de Red (Capa 3)", "Capa de Transporte (Capa 4)", "Capa Física (Capa 1)"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "Según el modelo OSI, ¿cuál es la función de la Capa de Presentación?",
            "opciones": ["Administrar sesiones de comunicación", "Controlar la entrega física de mensajes", "Proporcionar codificación, compresión y encriptación", "Determinar la ruta de los paquetes"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "El direccionamiento lógico del paquete y la determinación de ruta son responsabilidades de la capa:",
            "opciones": ["Capa de Sesión", "Capa de Red", "Capa de Enlace de Datos", "Capa de Transporte"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Qué capa del modelo OSI provee acceso al medio y maneja el direccionamiento físico de la trama?",
            "opciones": ["Capa Física", "Capa de Transporte", "Capa de Red", "Capa de Enlace de Datos"],
            "respuesta_correcta": 4
        },
        {
            "pregunta": "Las capas de Red, Enlace de Datos y Física se conocen como:",
            "opciones": ["Capas de Software", "Capas Superiores", "Capas Inferiores", "Capas de Aplicación"],
            "respuesta_correcta": 3
        },

        # --- TEMA: NORMATIVA IEEE ---
        {
            "pregunta": "¿Qué estándar del IEEE define las redes locales inalámbricas (WLAN)?",
            "opciones": ["IEEE 802.3", "IEEE 802.5", "IEEE 802.11", "IEEE 802.2"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "La normativa IEEE 802.3, que define las redes Ethernet, utiliza como protocolo de acceso al medio:",
            "opciones": ["Token Ring", "Polling", "CSMA/CD", "Token Bus"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué estándar define el protocolo LLC (Logical Link Control)?",
            "opciones": ["IEEE 802.1", "IEEE 802.2", "IEEE 802.3", "IEEE 802.5"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "La tecnología Token Ring, que usa un anillo lógico sobre un anillo físico, está definida por el estándar:",
            "opciones": ["IEEE 802.4 (Token Bus)", "IEEE 802.11 (Wi-Fi)", "IEEE 802.3 (Ethernet)", "IEEE 802.5"],
            "respuesta_correcta": 4
        }
    ]
    random.shuffle(preguntas)
    for pregunta in preguntas:
        pregunta['respuesta_correcta'] = pregunta['opciones'][pregunta['respuesta_correcta'] - 1]
    return preguntas

class TriviaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia de Redes")
        self.root.geometry("800x600")
        self.root.config(bg=COLOR_FONDO)

        pygame.mixer.init()

        # Cargar todos los efectos de sonido
        try:
            ruta_sonido_correcto = resource_path(ARCHIVO_SONIDO_CORRECTO)
            self.sonido_correcto = pygame.mixer.Sound(ruta_sonido_correcto)
        except Exception as e:
            print(f"No se pudo cargar el sonido correcto: {e}")
            self.sonido_correcto = None

        try:
            ruta_sonido_incorrecto = resource_path(ARCHIVO_SONIDO_INCORRECTO)
            self.sonido_incorrecto = pygame.mixer.Sound(ruta_sonido_incorrecto)
        except Exception as e:
            print(f"No se pudo cargar el sonido incorrecto: {e}")
            self.sonido_incorrecto = None

        try:
            ruta_sonido_inicio = resource_path(ARCHIVO_SONIDO_INICIO_TRIVIA)
            self.sonido_inicio_trivia = pygame.mixer.Sound(ruta_sonido_inicio)
        except Exception as e:
            print(f"No se pudo cargar el sonido de inicio trivia: {e}")
            self.sonido_inicio_trivia = None

        # --- Carga de fuentes e imágenes ---
        self.fuente_titulo = tkFont.Font(family="Helvetica", size=32, weight="bold")
        self.fuente_subtitulo = tkFont.Font(family="Helvetica", size=18)
        self.fuente_boton = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.fuente_pregunta = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.fuente_opcion = tkFont.Font(family="Helvetica", size=12)

        self.personajes_imgs = []
        try:
            for img_path in ["morde.png", "pike.png", "frog.png"]:
                ruta_completa = resource_path(img_path)
                imagen = Image.open(ruta_completa)
                imagen = imagen.resize((150, 150), Image.Resampling.LANCZOS)
                self.personajes_imgs.append(ImageTk.PhotoImage(imagen))
        except Exception as e:
            print(f"Ocurrió un error al cargar las imágenes: {e}")

        # --- Variables del juego y contenedor ---
        self.preguntas = obtener_preguntas()
        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        self.frame_contenedor = tk.Frame(root, bg=COLOR_FONDO)
        self.frame_contenedor.pack(fill="both", expand=True)
        
        self.volumen_musica = 0.5
        pygame.mixer.music.set_volume(self.volumen_musica)
        
        ### Creamos la barra de volumen una sola vez y de forma fija ###
        # Se crea sobre self.root para que no se borre
        slider_volumen = tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.01,
                                 orient="horizontal", length=200, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                 command=self.actualizar_volumen, troughcolor="#34495e", relief=tk.FLAT)
        slider_volumen.set(self.volumen_musica)
        slider_volumen.place(x=20, y=550) # Posición fija en la esquina inferior izquierda

        label_volumen = tk.Label(self.root, text="Volumen", font=self.fuente_opcion,
                                 bg=COLOR_FONDO, fg=COLOR_TEXTO)
        label_volumen.place(x=20, y=525) # Posición fija

        self.mostrar_panel_bienvenida()

    def limpiar_frame(self):
        for widget in self.frame_contenedor.winfo_children():
            widget.destroy()

    def reproducir_musica(self, archivo, loop=-1):
        try:
            ruta = resource_path(archivo)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play(loop)
            pygame.mixer.music.set_volume(self.volumen_musica)
        except Exception as e:
            print(f"No se pudo reproducir la música {archivo}: {e}")

    def detener_musica(self):
        pygame.mixer.music.stop()

    def actualizar_volumen(self, valor):
        valor_float = float(valor)
        self.volumen_musica = valor_float
        pygame.mixer.music.set_volume(self.volumen_musica)

    def mostrar_panel_bienvenida(self):
        self.limpiar_frame()
        self.reproducir_musica(ARCHIVO_MUSICA_MENU)

        canvas = tk.Canvas(self.frame_contenedor, borderwidth=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        try:
            ruta_fondo = resource_path("bienvenida.png")
            imagen_pil = Image.open(ruta_fondo).resize((800, 600), Image.Resampling.LANCZOS)
            self.imagen_fondo = ImageTk.PhotoImage(imagen_pil)
            canvas.create_image(0, 0, image=self.imagen_fondo, anchor="nw")
        except Exception:
            canvas.config(bg=COLOR_FONDO)

        canvas.create_text(400, 300, text="Trivia de Redes", font=self.fuente_titulo, fill=COLOR_TEXTO)
        canvas.create_text(400, 350, text="¡Pon a prueba tus conocimientos!", font=self.fuente_subtitulo, fill=COLOR_TEXTO)

        def on_comenzar_click():
            if self.sonido_inicio_trivia:
                self.sonido_inicio_trivia.play()
            self.root.after(300, self.comenzar_juego)

        boton_comenzar = tk.Button(canvas, text="Comenzar", font=self.fuente_boton, bg=COLOR_BOTON_COMENZAR,
                                  fg="#FFFFFF", command=on_comenzar_click, relief=tk.FLAT)
        canvas.create_window(400, 425, anchor="center", window=boton_comenzar, width=200, height=50)
        
    def comenzar_juego(self):
        self.limpiar_frame()
        self.detener_musica()
        self.reproducir_musica(ARCHIVO_MUSICA_TRIVIA)

        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        random.shuffle(self.preguntas)

        # interfaz del juego 
        self.label_avatar = tk.Label(self.frame_contenedor, bg=COLOR_FONDO)
        self.label_avatar.place(x=20, y=20)
        self.label_pregunta = tk.Label(self.frame_contenedor, text="", wraplength=580, justify="left",
                                       font=self.fuente_pregunta, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                       anchor="nw", height=4)
        self.label_pregunta.place(x=190, y=40)
        self.frame_opciones = tk.Frame(self.frame_contenedor, bg=COLOR_FONDO)
        self.frame_opciones.place(x=190, y=200)
        self.label_feedback = tk.Label(self.frame_contenedor, text="", font=self.fuente_pregunta, bg=COLOR_FONDO)
        self.label_feedback.place(x=190, y=450)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()
        self.label_feedback.config(text="")
        self.label_pregunta.config(text="")

        if self.pregunta_actual_idx < len(self.preguntas):
            if self.personajes_imgs:
                personaje_actual = random.choice(self.personajes_imgs)
                self.label_avatar.config(image=personaje_actual)

            pregunta_dic = self.preguntas[self.pregunta_actual_idx]
            texto_completo = pregunta_dic["pregunta"]
            self.animar_texto(texto_completo, 0)
        else:
            self.mostrar_resultado()

    def animar_texto(self, texto, index):
        if index < len(texto):
            self.label_pregunta.config(text=self.label_pregunta.cget("text") + texto[index])
            self.root.after(40, self.animar_texto, texto, index + 1)
        else:
            self.mostrar_opciones()

    def mostrar_opciones(self):
        pregunta_dic = self.preguntas[self.pregunta_actual_idx]
        for opcion in pregunta_dic["opciones"]:
            boton = tk.Button(self.frame_opciones, text=opcion, font=self.fuente_opcion,
                              bg=COLOR_BOTON, fg=COLOR_TEXTO, width=60, pady=10,
                              ### El botón llama directamente a verificar_respuesta ###
                              command=lambda opt=opcion: self.verificar_respuesta(opt))
            boton.pack(fill="x", pady=5)

    def verificar_respuesta(self, respuesta_elegida):
        # Deshabilitamos botones para evitar clics múltiples
        for widget in self.frame_opciones.winfo_children():
            widget.config(state="disabled")

        pregunta_dic = self.preguntas[self.pregunta_actual_idx]
        respuesta_correcta = pregunta_dic["respuesta_correcta"]

        if respuesta_elegida == respuesta_correcta:
            self.puntuacion += 1
            self.label_feedback.config(text="¡Correcto!", fg=COLOR_CORRECTO)
            if self.sonido_correcto:
                self.sonido_correcto.play()
        else:
            self.label_feedback.config(text=f"Incorrecto. La respuesta correcta era:\n{respuesta_correcta}", fg=COLOR_INCORRECTO)
            ### Reproducir sonido de respuesta incorrecta ###
            if self.sonido_incorrecto:
                self.sonido_incorrecto.play()

        # Resaltar la respuesta correcta/incorrecta
        for widget in self.frame_opciones.winfo_children():
            if widget['text'] == respuesta_correcta:
                widget.config(bg=COLOR_CORRECTO)
            elif widget['text'] == respuesta_elegida:
                widget.config(bg=COLOR_INCORRECTO)

        self.pregunta_actual_idx += 1
        self.root.after(2000, self.mostrar_pregunta)

    def mostrar_resultado(self):
        self.limpiar_frame()
        self.detener_musica()
        canvas = tk.Canvas(self.frame_contenedor, borderwidth=0, highlightthickness=0, bg=COLOR_FONDO)
        canvas.pack(fill="both", expand=True)

        canvas.create_text(400, 150, text="¡Fin del Juego!", font=self.fuente_titulo, fill=COLOR_TEXTO)

        total_preguntas = len(self.preguntas)
        puntuacion_final = self.puntuacion
        promedio = 0
        if total_preguntas > 0:
            promedio = (puntuacion_final / total_preguntas) * 100

        texto_puntuacion = f"Puntuación Final: {puntuacion_final} de {total_preguntas}"
        texto_promedio = f"Promedio de Aciertos: {promedio:.2f}%"

        canvas.create_text(400, 250, text=texto_puntuacion, font=self.fuente_subtitulo, fill=COLOR_TEXTO)
        canvas.create_text(400, 300, text=texto_promedio, font=self.fuente_subtitulo, fill=COLOR_TEXTO)

        boton_reintentar = tk.Button(canvas, text="Jugar de Nuevo", font=self.fuente_boton,
                                    bg=COLOR_BOTON_COMENZAR, fg="#FFFFFF",
                                    command=self.mostrar_panel_bienvenida, relief=tk.FLAT)
        canvas.create_window(400, 400, anchor="center", window=boton_reintentar, width=200, height=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaGUI(root)
    root.mainloop()