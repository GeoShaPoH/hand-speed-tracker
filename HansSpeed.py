import time
import threading
import pyautogui
from tkinter import Tk, Label, Frame, BOTH
from PIL import Image, ImageDraw

class PunteroThread(threading.Thread):
    def __init__(self, width, height):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        self.last_pos = pyautogui.position()
        self.current_pos = pyautogui.position()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.current_pos = pyautogui.position()
            self.calculate_speed()
            self.last_pos = self.current_pos
            time.sleep(0.165)  # Esperar 0.n segundos

    def calculate_speed(self):
        distance = ((self.current_pos[0] - self.last_pos[0]) ** 2 +
                    (self.current_pos[1] - self.last_pos[1]) ** 2) ** 0.5
        mm_per_pixel = 25.4 / self.width  # Conversión de píxeles a milímetros
        speed_mm_s = distance * mm_per_pixel / 0.5  # Velocidad en milímetros por segundo
        speed_mm_s = round(speed_mm_s, 2)  # Redondear a 2 decimales
        speed_label.config(text=f"{speed_mm_s} mm/s")

    def stop(self):
        self.running = False

# Configuración de las dimensiones del área de trabajo
width = 1920  # Ancho en píxeles
height = 1080  # Alto en píxeles

# Crear ventana
root = Tk()
root.title("Hand-Speed")
root.geometry("190x110")
root.configure(bg="black")  # Fondo negro

# Bloquear la maximización de la ventana
root.resizable(False, False)

# Estilos de fuente
font_head = ("Inter Bold", 15)
font_label = ("Inter Bold", 25)

# Crear marco para el borde neón
neon_frame = Frame(root, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness=2)
neon_frame.place(relx=0.5, rely=0.5, anchor="center", width=190, height=110)


# Crear etiqueta para mostrar la velocidad
speed_head = Label(root, text="Hand Speed", font=font_head, fg="white", bg="black")
speed_label = Label(root, text="0 mm/s", font=font_label, fg="white", bg="black")
speed_head.pack(expand=True)
speed_label.pack(expand=True)

# Crear un color de degradado para el marco
def create_gradient(color_start, color_end, width, height):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for i in range(height):
        r = int(color_start[0] + (color_end[0] - color_start[0]) * i / height)
        g = int(color_start[1] + (color_end[1] - color_start[1]) * i / height)
        b = int(color_start[2] + (color_end[2] - color_start[2]) * i / height)
        draw.line((0, i, width, i), fill=(r, g, b))

    return image

# Crear la animcacion para el marco
def animate_neon():
    color_start = (0, 0, 255)  # Azul
    color_end = (0, 255, 255)  # Cian
    transition_duration = 1.0  # Duración de la transición en segundos
    transition_steps = 50  # Cantidad de pasos en la transición

    image_start = create_gradient(color_start, color_end, 300, 100)
    image_end = create_gradient(color_end, color_start, 300, 100)

    while True:
        for i in range(transition_steps):
            r = int(image_start.getpixel((i, 0))[0] + (image_end.getpixel((i, 0))[0] - image_start.getpixel((i, 0))[0]) * i / transition_steps)
            g = int(image_start.getpixel((i, 0))[1] + (image_end.getpixel((i, 0))[1] - image_start.getpixel((i, 0))[1]) * i / transition_steps)
            b = int(image_start.getpixel((i, 0))[2] + (image_end.getpixel((i, 0))[2] - image_start.getpixel((i, 0))[2]) * i / transition_steps)
            neon_frame.config(highlightbackground=f"#{r:02x}{g:02x}{b:02x}", highlightcolor=f"#{r:02x}{g:02x}{b:02x}")
            time.sleep(transition_duration / transition_steps)

        time.sleep(0.5)

# Inicializar el hilo del puntero
puntero_thread = PunteroThread(width, height)
puntero_thread.start()

# Iniciar la animación del borde neón en un hilo aparte
neon_animation_thread = threading.Thread(target=animate_neon)
neon_animation_thread.daemon = True
neon_animation_thread.start()

# Ejecutar la ventana
try:
    root.mainloop()
except KeyboardInterrupt:
    puntero_thread.stop()
    puntero_thread.join()
