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
COLOR_BOTON = "#3498db"
COLOR_CORRECTO = "#2ecc71"
COLOR_INCORRECTO = "#e74c3c"
COLOR_INDICADOR_BASE = "#95a5a6"

ARCHIVO_SONIDO_CORRECTO = "martillo.wav"
ARCHIVO_SONIDO_INCORRECTO = "fuego.wav"
ARCHIVO_SONIDO_INICIO_TRIVIA = "explosion.wav"
ARCHIVO_MUSICA_TRIVIA = "music.mp3"
ARCHIVO_MUSICA_MENU = "music.mp3"

pygame.init()
pygame.mixer.init()

def obtener_preguntas():
    preguntas = [
    {
        "pregunta": "¿Qué organización creó el modelo TCP/IP?",
        "opciones": [
            "Organización Internacional de Estandarización (ISO)",
            "Agencia de Proyectos de Investigación Avanzada para la Defensa (DARPA)",
            "Instituto de Ingenieros Eléctricos y Electrónicos (IEEE)",
            "Unión Internacional de Telecomunicaciones (ITU)"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Para qué tipo de redes es apropiado el modelo TCP/IP?",
        "opciones": [
            "Solo para redes LAN",
            "Solo para redes WAN",
            "Tanto para redes LAN como WAN",
            "Solo para redes inalámbricas"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué dispositivo utiliza el modelo TCP/IP como herramienta de configuración según la presentación?",
        "opciones": [
            "Switch",
            "Firewall",
            "Router",
            "Hub"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué se agrega a los datos en cada capa durante la encapsulación en el modelo TCP/IP?",
        "opciones": [
            "Solo los datos originales",
            "Sistema de encriptación",
            "Información de control para el envío correcto",
            "Contenido multimedia adicional"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué capa del modelo TCP/IP incluye los protocolos TCP y UDP?",
        "opciones": [
            "Capa de Aplicación",
            "Capa de Transporte",
            "Capa de Internet",
            "Capa de Acceso a la Red"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué función realiza TCP mediante 'ventanas deslizantes'?",
        "opciones": [
            "Encriptación de datos",
            "Control de flujo",
            "Traducción de direcciones",
            "Compresión de archivos"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué proporciona la confiabilidad en las transmisiones TCP?",
        "opciones": [
            "Firmas digitales",
            "Números de secuencia y acuses de recibo",
            "Encriptación AES",
            "Balanceo de carga"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿De qué es independiente el modelo TCP/IP según la presentación?",
        "opciones": [
            "Solo del hardware",
            "Solo del software",
            "Del hardware, software, medio de comunicación y tipo de enlace",
            "Solo del tipo de enlace"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué protocolo opera en la capa de Internet del modelo TCP/IP?",
        "opciones": [
            "HTTP",
            "FTP",
            "IP",
            "SMTP"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué característica hace que TCP/IP esté disponible universalmente?",
        "opciones": [
            "Es propietario de Microsoft",
            "Solo funciona con equipos específicos",
            "Es un estándar abierto e independiente de plataforma",
            "Requiere licencia costosa"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "Durante la encapsulación, ¿qué sucede con los datos al pasar por cada capa?",
        "opciones": [
            "Se comprimen automáticamente",
            "Se dividen en paquetes más pequeños",
            "Se les agrega información de control específica",
            "Se convierten a formato binario"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué tipo de control implementa TCP para gestionar la transmisión de datos?",
        "opciones": [
            "Control de acceso al medio",
            "Control de congestión mediante tokens",
            "Control de flujo con ventanas deslizantes",
            "Control de errores con paridad"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué elemento se menciona como fundamental para la confiabilidad en TCP?",
        "opciones": [
            "Cifrado de extremo a extremo",
            "Números de secuencia y acuses de recibo",
            "Redundancia de paquetes",
            "Verificación de integridad CRC"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué capa del modelo TCP/IP corresponde a la capa de Aplicación?",
        "opciones": [
            "Capa 1",
            "Capa 2",
            "Capa 3",
            "Capa 4"
        ],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué protocolo de transporte NO se menciona en la presentación?",
        "opciones": [
            "TCP",
            "UDP",
            "FTP",
            "Ambos TCP y UDP se mencionan"
        ],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Cuál es el propósito principal de la información de control agregada durante la encapsulación?",
        "opciones": [
            "Aumentar el tamaño de los datos",
            "Garantizar que el envío sea correcto",
            "Mejorar la velocidad de transmisión",
            "Agregar capacidades multimedia"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué característica permite al modelo TCP/IP funcionar en diversos entornos?",
        "opciones": [
            "Dependencia de hardware específico",
            "Independencia de plataforma y medios",
            "Uso exclusivo de fibra óptica",
            "Compatibilidad solo con routers Cisco"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "En el contexto de TCP, ¿qué son los 'acuses de recibo'?",
        "opciones": [
            "Confirmaciones de entrega de paquetes",
            "Sistemas de encriptación",
            "Protocolos de enrutamiento",
            "Mecanismos de compresión"
        ],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué capa procesa los números de secuencia y acuses de recibo en TCP?",
        "opciones": [
            "Capa de Aplicación",
            "Capa de Transporte",
            "Capa de Internet",
            "Capa de Enlace de Datos"
        ],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué elemento de red se menciona específicamente como usuario del modelo TCP/IP?",
        "opciones": [
            "Switch",
            "Firewall",
            "Router",
            "Access Point"
        ],
        "respuesta_correcta": 3
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

        # Carga de sonidos
        try:
            self.sonido_correcto = pygame.mixer.Sound(resource_path(ARCHIVO_SONIDO_CORRECTO))
            self.sonido_incorrecto = pygame.mixer.Sound(resource_path(ARCHIVO_SONIDO_INCORRECTO))
            self.sonido_inicio_trivia = pygame.mixer.Sound(resource_path(ARCHIVO_SONIDO_INICIO_TRIVIA))
        except Exception as e:
            print(f"Error al cargar sonidos: {e}")

        # Carga de fuentes e imágenes
        self.fuente_titulo = tkFont.Font(family="Helvetica", size=32, weight="bold")
        self.fuente_subtitulo = tkFont.Font(family="Helvetica", size=18)
        self.fuente_boton = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.fuente_pregunta = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.fuente_opcion = tkFont.Font(family="Helvetica", size=12)

        self.personajes_imgs = []
        try:
            for img_path in ["morde.png", "pike.png", "frog.png"]:
                imagen = Image.open(resource_path(img_path)).resize((150, 150), Image.Resampling.LANCZOS)
                self.personajes_imgs.append(ImageTk.PhotoImage(imagen))
        except Exception as e:
            print(f"Ocurrió un error al cargar las imágenes de personajes: {e}")
        
        # Carga de fondos
        self.fondos_preguntas_pil = []
        try:
            for i in range(1, 12):
                img = Image.open(resource_path(f"fondo{i}.png")).resize((800, 600), Image.Resampling.LANCZOS)
                self.fondos_preguntas_pil.append(img)
        except Exception as e:
            print(f"No se pudieron cargar los fondos: {e}")
        self.imagen_resultado_path = "final.png" 

        # --- Variables del juego y contenedor ---
        self.num_preguntas = 20
        self.preguntas = obtener_preguntas()
        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        self.frame_contenedor = tk.Frame(root, bg=COLOR_FONDO)
        self.frame_contenedor.pack(fill="both", expand=True)
        self.volumen_musica = 0.5
        pygame.mixer.music.set_volume(self.volumen_musica)
        self.nombre_jugador = ""
        self.indicadores_preguntas_ids = []
        
        ### Se añade una lista para guardar los widgets de los botones de opción ###
        self.opciones_widgets = []

        # Barra de volumen fija
        slider_volumen = tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.01,
                                  orient="horizontal", length=200, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                  command=self.actualizar_volumen, troughcolor="#34495e", relief=tk.FLAT)
        slider_volumen.set(self.volumen_musica)
        slider_volumen.place(x=20, y=550)
        label_volumen = tk.Label(self.root, text="Volumen", font=self.fuente_opcion, bg=COLOR_FONDO, fg=COLOR_TEXTO)
        label_volumen.place(x=20, y=525)

        self.mostrar_panel_bienvenida()

    def limpiar_frame(self):
        for widget in self.frame_contenedor.winfo_children():
            widget.destroy()

    def reproducir_musica(self, archivo, loop=-1):
        try:
            pygame.mixer.music.load(resource_path(archivo))
            pygame.mixer.music.play(loop)
            pygame.mixer.music.set_volume(self.volumen_musica)
        except Exception as e:
            print(f"No se pudo reproducir la música {archivo}: {e}")

    def detener_musica(self):
        pygame.mixer.music.stop()

    def actualizar_volumen(self, valor):
        self.volumen_musica = float(valor)
        pygame.mixer.music.set_volume(self.volumen_musica)

    def mostrar_panel_bienvenida(self):
        self.limpiar_frame()
        self.reproducir_musica(ARCHIVO_MUSICA_MENU)
        canvas = tk.Canvas(self.frame_contenedor, borderwidth=0, highlightthickness=0, bg=COLOR_FONDO)
        canvas.pack(fill="both", expand=True)
        try:
            imagen_pil = Image.open(resource_path("bienvenida.png")).resize((800, 600), Image.Resampling.LANCZOS)
            self.imagen_fondo = ImageTk.PhotoImage(imagen_pil)
            canvas.create_image(0, 0, image=self.imagen_fondo, anchor="nw")
        except Exception:
            pass

        canvas.create_text(400, 200, text="Trivia de Redes", font=self.fuente_titulo, fill=COLOR_TEXTO)
        canvas.create_text(400, 250, text="¡Pon a prueba tus conocimientos!", font=self.fuente_subtitulo, fill=COLOR_TEXTO)
        canvas.create_text(400, 320, text="Dime tu nombre, pequeño:", font=self.fuente_subtitulo, fill=COLOR_TEXTO)
        self.entrada_nombre = tk.Entry(self.frame_contenedor, font=self.fuente_subtitulo, bg="#34495e", fg=COLOR_TEXTO, justify="center")
        canvas.create_window(400, 360, window=self.entrada_nombre, width=300, height=40)

        def iniciar_con(n):
            self.nombre_jugador = self.entrada_nombre.get() or "Jugador"
            self.num_preguntas = n
            if self.sonido_inicio_trivia: self.sonido_inicio_trivia.play()
            self.root.after(300, self.comenzar_juego)

        boton_10 = tk.Button(canvas, text="Jugar 10 Preguntas", font=self.fuente_boton, bg=COLOR_BOTON_COMENZAR, fg="#FFFFFF", command=lambda: iniciar_con(10), relief=tk.FLAT)
        canvas.create_window(400, 430, anchor="center", window=boton_10, width=220, height=50)
        boton_20 = tk.Button(canvas, text="Jugar 20 Preguntas", font=self.fuente_boton, bg=COLOR_BOTON, fg="#FFFFFF", command=lambda: iniciar_con(20), relief=tk.FLAT)
        canvas.create_window(400, 490, anchor="center", window=boton_20, width=220, height=50)

    def comenzar_juego(self):
        self.limpiar_frame()
        self.detener_musica()
        self.reproducir_musica(ARCHIVO_MUSICA_TRIVIA)

        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        self.indicadores_preguntas_ids = []
        todas = obtener_preguntas()
        self.preguntas = todas[:self.num_preguntas]

        self.canvas_juego = tk.Canvas(self.frame_contenedor, borderwidth=0, highlightthickness=0, bg=COLOR_FONDO)
        self.canvas_juego.pack(fill="both", expand=True)
        
        self.canvas_image_id = None
        self.avatar_id = self.canvas_juego.create_image(20, 20, anchor="nw")
        self.avatar_error_text_id = self.canvas_juego.create_text(95, 95, text="", font=self.fuente_opcion, fill=COLOR_INCORRECTO, justify="center")
        self.pregunta_text_id = self.canvas_juego.create_text(190, 40, text="", font=self.fuente_pregunta, fill=COLOR_TEXTO, anchor="nw", width=580, justify="left")
        self.feedback_text_id = self.canvas_juego.create_text(190, 450, text="", font=self.fuente_pregunta, fill=COLOR_CORRECTO, anchor="nw", justify="left")
        self.crear_indicadores()
        self.mostrar_pregunta()

    def crear_indicadores(self):
        # funcion de creación de indicadores de preguntas
        for i in range(self.num_preguntas):
            x = 30; y = 200 + i * 25
            if self.num_preguntas == 20 and i >= 10:
                x = 60; y = 200 + (i - 10) * 25
            indicador_id = self.canvas_juego.create_oval(x, y, x + 15, y + 15, fill=COLOR_INDICADOR_BASE, outline=COLOR_TEXTO, width=2)
            self.indicadores_preguntas_ids.append(indicador_id)

    def animar_texto(self, texto, index):
        if index < len(texto):
            current_text = self.canvas_juego.itemcget(self.pregunta_text_id, "text")
            self.canvas_juego.itemconfig(self.pregunta_text_id, text=current_text + texto[index])
            self.root.after(20, self.animar_texto, texto, index + 1)
        else:
            self.mostrar_opciones()

    def mostrar_pregunta(self):
        ### limpiamos la lista de widgets de opción ###
        
        for boton_widget, window_id in self.opciones_widgets:
            boton_widget.destroy()
            self.canvas_juego.delete(window_id)
        self.opciones_widgets.clear()
        
        self.canvas_juego.itemconfig(self.feedback_text_id, text="")
        self.canvas_juego.itemconfig(self.pregunta_text_id, text="")
        
        if self.fondos_preguntas_pil:
            self.fondo_actual_pil = random.choice(self.fondos_preguntas_pil)
            self.fondo_actual_tk = ImageTk.PhotoImage(self.fondo_actual_pil)
            if self.canvas_image_id: self.canvas_juego.delete(self.canvas_image_id)
            self.canvas_image_id = self.canvas_juego.create_image(0, 0, image=self.fondo_actual_tk, anchor="nw")
            self.canvas_juego.tag_lower(self.canvas_image_id)

        if self.pregunta_actual_idx < len(self.preguntas):
            if self.personajes_imgs:
                personaje_actual = random.choice(self.personajes_imgs)
                self.canvas_juego.itemconfig(self.avatar_id, image=personaje_actual)
                self.canvas_juego.itemconfig(self.avatar_error_text_id, text="")
            else:
                self.canvas_juego.itemconfig(self.avatar_id, image="")
                self.canvas_juego.itemconfig(self.avatar_error_text_id, text="¡Avatares no encontrados!")

            pregunta_dic = self.preguntas[self.pregunta_actual_idx]
            texto_completo = pregunta_dic["pregunta"]
            self.animar_texto(texto_completo, 0)
        else:
            self.mostrar_resultado()

    ### Función para colocar botones directamente en el canvas ###
    def mostrar_opciones(self):
        pregunta_dic = self.preguntas[self.pregunta_actual_idx]
        
        # Coordenadas iniciales para el primer botón
        start_x = 190 + (580 // 2) # Centrado en el área de la pregunta
        start_y = 220
        y_offset = 60 # Espacio vertical entre botones

        for i, opcion in enumerate(pregunta_dic["opciones"]):
            # Creacion el botón
            boton = tk.Button(self.canvas_juego, text=opcion, font=self.fuente_opcion,
                              bg=COLOR_BOTON, fg=COLOR_TEXTO, pady=10, relief=tk.FLAT,
                              wraplength=550, # Permite que el texto del botón se ajuste
                              command=lambda opt=opcion: self.verificar_respuesta(opt))
            
            # Lo colocamos en el canvas
            current_y = start_y + (i * y_offset)
            window_id = self.canvas_juego.create_window(start_x, current_y, anchor="center", window=boton, width=580)
            
            # Guardamos el widget del botón y el ID de su ventana para poder borrarlo después
            self.opciones_widgets.append((boton, window_id))


    def verificar_respuesta(self, respuesta_elegida):
        ### itera sobre la lista de widgets guardados ###
        for boton_widget, _ in self.opciones_widgets:
            boton_widget.config(state="disabled")

        pregunta_dic = self.preguntas[self.pregunta_actual_idx]
        respuesta_correcta = pregunta_dic["respuesta_correcta"]

        if respuesta_elegida == respuesta_correcta:
            self.puntuacion += 1
            self.canvas_juego.itemconfig(self.feedback_text_id, text="¡Correcto!", fill=COLOR_CORRECTO)
            if self.sonido_correcto: self.sonido_correcto.play()
            self.cambiar_indicador(self.pregunta_actual_idx, COLOR_CORRECTO)
        else:
            self.canvas_juego.itemconfig(self.feedback_text_id, text=f"Incorrecto. La respuesta correcta era:\n{respuesta_correcta}", fill=COLOR_INCORRECTO)
            if self.sonido_incorrecto: self.sonido_incorrecto.play()
            self.cambiar_indicador(self.pregunta_actual_idx, COLOR_INCORRECTO)

        ### itera sobre la lista de widgets guardados ###
        for boton_widget, _ in self.opciones_widgets:
            if boton_widget['text'] == respuesta_correcta:
                boton_widget.config(bg=COLOR_CORRECTO)
            elif boton_widget['text'] == respuesta_elegida:
                boton_widget.config(bg=COLOR_INCORRECTO)

        self.pregunta_actual_idx += 1
        self.root.after(2000, self.mostrar_pregunta)

    def cambiar_indicador(self, index, color):
        if 0 <= index < len(self.indicadores_preguntas_ids):
            indicador_id = self.indicadores_preguntas_ids[index]
            self.canvas_juego.itemconfig(indicador_id, fill=color)

    def mostrar_resultado(self):
        self.limpiar_frame()
        self.detener_musica()
        canvas = tk.Canvas(self.frame_contenedor, borderwidth=0, highlightthickness=0, bg=COLOR_FONDO)
        canvas.pack(fill="both", expand=True)

        try:
            imagen_pil = Image.open(resource_path(self.imagen_resultado_path)).resize((800, 600), Image.Resampling.LANCZOS)
            self.imagen_resultado_tk = ImageTk.PhotoImage(imagen_pil)
            canvas.create_image(0, 0, image=self.imagen_resultado_tk, anchor="nw")
        except Exception as e:
            print(f"No se pudo cargar la imagen de resultado: {e}")

        canvas.create_text(400, 150, text="¡Fin del Juego!", font=self.fuente_titulo, fill=COLOR_TEXTO)
        texto_nombre = f"¡Largo de mi palacio, pequeño, {self.nombre_jugador}!"
        canvas.create_text(400, 200, text=texto_nombre, font=self.fuente_subtitulo, fill=COLOR_TEXTO)

        total_preguntas = len(self.preguntas)
        puntuacion_final = self.puntuacion
        promedio = (puntuacion_final / total_preguntas) * 100 if total_preguntas > 0 else 0

        texto_puntuacion = f"Puntuación Final: {puntuacion_final} de {total_preguntas}"
        texto_promedio = f"Promedio de Aciertos: {promedio:.2f}%"

        canvas.create_text(400, 250, text=texto_puntuacion, font=self.fuente_subtitulo, fill=COLOR_TEXTO)
        canvas.create_text(400, 300, text=texto_promedio, font=self.fuente_subtitulo, fill=COLOR_TEXTO)

        boton_reintentar = tk.Button(canvas, text="Jugar de Nuevo", font=self.fuente_boton, bg=COLOR_BOTON_COMENZAR, fg="#FFFFFF", command=self.mostrar_panel_bienvenida, relief=tk.FLAT)
        canvas.create_window(400, 400, anchor="center", window=boton_reintentar, width=200, height=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaGUI(root)
    root.mainloop()