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

COLOR_FONDO = "#2c3e50"
COLOR_TEXTO = "#ecf0f1"
COLOR_BOTON_COMENZAR = "#2ecc71"
COLOR_BOTON_HOVER = "#2980b9"
COLOR_BOTON = "#3498db"
COLOR_CORRECTO = "#2ecc71"
COLOR_INCORRECTO = "#e74c3c"

ARCHIVO_SONIDO_INICIO_TRIVIA = "sound2.wav"
ARCHIVO_MUSICA_TRIVIA = "music.mp3"
ARCHIVO_SONIDO_CLICK = "sound.wav"
ARCHIVO_MUSICA_MENU = "music.mp3"  # Cambia aquí el archivo mp3 que quieras usar

def obtener_preguntas():
    preguntas = [
        {
            "pregunta": "¿Qué significa LAN?",
            "opciones": ["Red de Área Lejana", "Red de Acceso Local", "Red de Área Local", "Red de Ancho Limitado"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuál es una característica principal de una red WAN?",
            "opciones": ["Cubre un área geográfica pequeña", "Conecta dispositivos en una misma habitación", "Cubre un área geográfica extensa", "Utiliza solo fibra óptica"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "Internet es el ejemplo más grande de una red...",
            "opciones": ["LAN", "WAN", "MAN", "PAN"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Qué tipo de red conecta un smartphone y un smartwatch?",
            "opciones": ["WAN", "LAN", "PAN (Red de Área Personal)", "MAN"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "En la topología de red en estrella...",
            "opciones": ["Todos los dispositivos se conectan en línea.", "Cada dispositivo está conectado a todos los demás.", "Todos se conectan a un punto central (switch).", "Los datos viajan en un círculo."],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué significa la 'M' en MAN?",
            "opciones": ["Mundial", "Móvil", "Metropolitana", "Múltiple"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuál de estos es un ejemplo de un dispositivo de red utilizado en una LAN?",
            "opciones": ["Satélite de comunicaciones", "Módem DSL", "Switch", "Antena de telefonía móvil"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "Las redes que utilizan ondas de radio en lugar de cables para transmitir datos se conocen como:",
            "opciones": ["WLAN (Red de Área Local Inalámbrica)", "WAN", "Redes de fibra óptica", "Redes satelitales"],
            "respuesta_correcta": 1
        },
        {
            "pregunta": "¿Qué dispositivo se usa comúnmente para conectar una red LAN a Internet?",
            "opciones": ["Switch", "Router", "Hub", "Tarjeta de Red"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "El término 'Wi-Fi' es una marca comercial para un conjunto de tecnologías basadas en el estándar...",
            "opciones": ["Bluetooth", "Ethernet", "IEEE 802.11", "LTE"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué es una dirección IP?",
            "opciones": ["La dirección física de una casa", "Un identificador único para un dispositivo en una red", "El nombre de un sitio web", "Una contraseña de Wi-Fi"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Cuál de los siguientes es un ejemplo de una red PAN (Personal Area Network)?",
            "opciones": ["La red de una universidad", "Internet", "La conexión entre tu móvil y tus auriculares Bluetooth", "La red de una ciudad"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "HTTP son las siglas de...",
            "opciones": ["Protocolo de Transferencia de Hipertexto", "Programa de Traducción de Host", "Protocolo de Texto de Alta Tensión", "Herramienta de Traspaso de Páginas"],
            "respuesta_correcta": 1
        },
        {
            "pregunta": "Un cable de Ethernet se utiliza principalmente para crear redes...",
            "opciones": ["Inalámbricas (WLAN)", "Satelitales", "Cableadas (LAN)", "Móviles (4G/5G)"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué función principal tiene un 'Firewall' o Cortafuegos?",
            "opciones": ["Aumentar la velocidad de Internet", "Conectar varios ordenadores", "Bloquear el acceso no autorizado a una red", "Almacenar archivos en la nube"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "En una red, un 'servidor' es un ordenador que...",
            "opciones": ["Solo recibe información", "Provee servicios o datos a otros ordenadores (clientes)", "Siempre está apagado", "No necesita conexión a la red"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "¿Qué protocolo es responsable de asignar direcciones IP dinámicamente a los dispositivos en una red?",
            "opciones": ["DNS", "HTTP", "FTP", "DHCP"],
            "respuesta_correcta": 4
        },
        {
            "pregunta": "En el modelo OSI, ¿en qué capa operan los Routers principalmente?",
            "opciones": ["Capa 1 (Física)", "Capa 2 (Enlace de Datos)", "Capa 3 (Red)", "Capa 7 (Aplicación)"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuál es la función del DNS (Domain Name System)?",
            "opciones": ["Asignar IPs automáticamente", "Traducir nombres de dominio (ej: google.com) a direcciones IP", "Asegurar la conexión con encriptación", "Transferir archivos grandes"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "Una dirección MAC es...",
            "opciones": ["Un tipo de dirección IP", "Una contraseña para redes de Apple", "Un identificador de hardware único asignado a la tarjeta de red", "La dirección de una red metropolitana"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué desventaja principal tiene la topología en bus?",
            "opciones": ["Es muy cara de implementar", "Si el cable principal (bus) falla, toda la red se cae", "Necesita un dispositivo central para funcionar", "Es extremadamente lenta para pocos dispositivos"],
            "respuesta_correcta": 2
        },
        {
            "pregunta": "El protocolo FTP (File Transfer Protocol) se usa específicamente para...",
            "opciones": ["Navegar por páginas web", "Enviar correos electrónicos", "Transferir archivos entre un cliente y un servidor", "Ver videos en streaming"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "Una VPN (Virtual Private Network) se utiliza principalmente para...",
            "opciones": ["Crear una conexión segura y encriptada a través de una red pública", "Acelerar la descarga de archivos", "Conectar un monitor a un ordenador", "Bloquear anuncios en sitios web"],
            "respuesta_correcta": 1
        },
        {
            "pregunta": "En el modelo OSI, ¿qué capa se encarga de la representación de datos, compresión y encriptación?",
            "opciones": ["Capa de Sesión", "Capa de Transporte", "Capa de Presentación", "Capa de Aplicación"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Cuál es el propósito de una máscara de subred (Subnet Mask) como 255.255.255.0?",
            "opciones": ["Identificar el fabricante del dispositivo", "Ocultar la dirección IP pública", "Diferenciar la porción de red de la porción de host en una IP", "Asignar un nombre al equipo"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "El protocolo SSH (Secure Shell) utiliza por defecto el puerto TCP número...",
            "opciones": ["80", "443", "22", "25"],
            "respuesta_correcta": 3
        },
        {
            "pregunta": "¿Qué tecnología permite crear múltiples redes lógicas y aisladas sobre una única red física LAN?",
            "opciones": ["VLAN", "NAT", "WAN", "DHCP"],
            "respuesta_correcta": 1
        },
        {
            "pregunta": "Un Switch opera en la Capa 2 (Enlace de Datos) del modelo OSI, mientras que un Hub opera en la...",
            "opciones": ["Capa 1 (Física)", "Capa 3 (Red)", "También en la Capa 2", "Capa 4 (Transporte)"],
            "respuesta_correcta": 1
        },
        {
            "pregunta": "El protocolo para enviar correos electrónicos (email) es SMTP y utiliza el puerto...",
            "opciones": ["110 (POP3)", "143 (IMAP)", "80 (HTTP)", "25"],
            "respuesta_correcta": 4
        },
        {
            "pregunta": "HTTPS, la versión segura de HTTP, utiliza el puerto TCP por defecto...",
            "opciones": ["80", "8080", "21", "443"],
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

        try:
            ruta_sonido_click = resource_path(ARCHIVO_SONIDO_CLICK)
            self.sonido_click = pygame.mixer.Sound(ruta_sonido_click)
        except Exception as e:
            print(f"No se pudo cargar el sonido click: {e}")
            self.sonido_click = None

        try:
            ruta_sonido_inicio = resource_path(ARCHIVO_SONIDO_INICIO_TRIVIA)
            self.sonido_inicio_trivia = pygame.mixer.Sound(ruta_sonido_inicio)
        except Exception as e:
            print(f"No se pudo cargar el sonido de inicio trivia: {e}")
            self.sonido_inicio_trivia = None

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

        self.preguntas = obtener_preguntas()
        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        self.frame_contenedor = tk.Frame(root, bg=COLOR_FONDO)
        self.frame_contenedor.pack(fill="both", expand=True)

        # Volumen (de 0.0 a 1.0)
        self.volumen_musica = 0.2  # volumen inicial más bajo para no ser tan fuerte
        pygame.mixer.music.set_volume(self.volumen_musica)

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
            self.root.after(300, self.comenzar_juego)  # espera para que suene

        boton_comenzar = tk.Button(canvas, text="Comenzar", font=self.fuente_boton, bg=COLOR_BOTON_COMENZAR,
                                  fg="#FFFFFF", command=on_comenzar_click, relief=tk.FLAT)
        canvas.create_window(400, 425, anchor="center", window=boton_comenzar, width=200, height=50)

        # Slider volumen menú
        slider_volumen = tk.Scale(canvas, from_=0.0, to=1.0, resolution=0.01, orient="horizontal",
                                 length=200, bg=COLOR_FONDO, fg=COLOR_TEXTO, command=self.actualizar_volumen)
        slider_volumen.set(self.volumen_musica)
        canvas.create_window(400, 475, anchor="center", window=slider_volumen)
        canvas.create_text(400, 460, text="Volumen Música", font=self.fuente_opcion, fill=COLOR_TEXTO)

    def comenzar_juego(self):
        self.limpiar_frame()
        self.detener_musica()
        self.reproducir_musica(ARCHIVO_MUSICA_TRIVIA)

        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        random.shuffle(self.preguntas)

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

        # Slider volumen trivia
        slider_volumen = tk.Scale(self.frame_contenedor, from_=0.0, to=1.0, resolution=0.01,
                                 orient="horizontal", length=200, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                 command=self.actualizar_volumen)
        slider_volumen.set(self.volumen_musica)
        slider_volumen.place(x=10, y=570)
        label_volumen = tk.Label(self.frame_contenedor, text="Volumen Música", font=self.fuente_opcion,
                                 bg=COLOR_FONDO, fg=COLOR_TEXTO)
        label_volumen.place(x=10, y=550)

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
                              command=lambda opt=opcion: self.click_y_verificar(opt))
            boton.pack(fill="x", pady=5)

    def click_y_verificar(self, opcion):
        if self.sonido_click:
            self.sonido_click.play()
        self.verificar_respuesta(opcion)

    def verificar_respuesta(self, respuesta_elegida):
        for widget in self.frame_opciones.winfo_children():
            widget.config(state="disabled")

        pregunta_dic = self.preguntas[self.pregunta_actual_idx]
        respuesta_correcta = pregunta_dic["respuesta_correcta"]

        if respuesta_elegida == respuesta_correcta:
            self.puntuacion += 1
            self.label_feedback.config(text="¡Correcto!", fg=COLOR_CORRECTO)
        else:
            self.label_feedback.config(text=f"Incorrecto. La respuesta correcta era:\n{respuesta_correcta}", fg=COLOR_INCORRECTO)

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