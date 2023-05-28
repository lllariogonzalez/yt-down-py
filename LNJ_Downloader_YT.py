from tkinter import *
from tkinter import ttk
from scripts import *
import threading
import webbrowser
import sys
import os


# rutas relativas para las imagenes, asi pyinstaller las puede empaquetar
# _MEIPASS permite saber si estamos en desarrollo o no
def resolver_ruta(ruta_relativa):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)


# Solución para el executable con pyinstaller,
# ya que moviepy requeria una salida y necesitaba la consola
output = open("output.txt", "wt")
sys.stdout = output
sys.stderr = output


def download_video(links):
    progress_bar.start(250)
    response = descargar_video(links, check_var.get())
    descargar_btn.config(state=NORMAL)
    if response == "Todas las descargas completadas":
        progress_bar.stop()
        progress_bar.step(99.9)
        notificaciones.config(text=response)
    else:
        notificaciones.config(text=response)
        progress_bar.stop()


def download():
    links = video_url.get(1.0, END).split("\n")
    links = list(filter(lambda yt: len(yt) > 0, links))
    hilo = threading.Thread(target=download_video, args=(links,))
    hilo.start()
    descargar_btn.config(state=DISABLED)
    notificaciones.config(text="Descargando...")


def abrir_enlace():
    webbrowser.open("https://lanuevajerusalenamorysalvacion.com")


def enlace_hover(event):
    web.config(fg="red", cursor="hand2")


def enlace_no_hover(event):
    web.config(fg="black", cursor="")


# UI tkinter

ventana = Tk()
ventana.title("LNJ DownloaderYT")
ventana.geometry("400x550")
ventana.iconbitmap(resolver_ruta("lnj.ico"))

title = Label(
    text="Añade tus URL en líneas distintas", font=("Segoe UI Variable", 11, "bold")
)
title.pack(padx=10, pady=10)

video_url = Text(
    ventana,
    width=90,
    height=10,
    borderwidth=1,
    font=("Segoe UI Variable", 10, "normal"),
)
video_url.pack(padx=20, pady=5)

check_var = BooleanVar()

# Crear el Checkbutton
check_button = Checkbutton(text="MP3", variable=check_var)
check_button.pack()

descargar_btn = Button(
    ventana,
    width=20,
    text="Descargar",
    foreground="white",
    background="black",
    font=("Segoe UI Variable", 10, "bold"),
    command=lambda: download(),
)
descargar_btn.pack(padx=10, pady=30)


progress_bar = ttk.Progressbar(length=360)
progress_bar.place(x=100, y=100, width=100)
progress_bar.pack()

notificaciones = Label(
    text="Todos los derechos de autor la tiene nuestro Creador ☀",
    font=("Segoe UI Variable", 10, "normal"),
)
notificaciones.pack(padx=10, pady=20)

web = Label(
    text="https://lanuevajerusalenamorysalvacion.com",
    font=("Segoe UI Variable", 10, "bold"),
)
web.pack(padx=10, pady=5)


web.bind("<Button-1>", lambda e: abrir_enlace())
web.bind("<Enter>", enlace_hover)
web.bind("<Leave>", enlace_no_hover)

image = PhotoImage(file=resolver_ruta("logo.png"))
label = ttk.Label(image=image)
label.pack()

ventana.mainloop()
