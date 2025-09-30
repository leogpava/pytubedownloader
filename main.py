import os
import threading
import tkinter as tk
import customtkinter as ctk
import sys
from   tkinter import filedialog, END
from   tkinter import ttk
from   pytubefix import YouTube 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def update_status(mensagem):
    status_label.configure(text=mensagem)

def ytDownload():
    url = campo_url.get()
    destino = campo_saida.get() 

    try:
        if url:
            janela.after(0, lambda: update_status("Buscando vídeo..."))

            yt = YouTube(url)

            janela.after(0, lambda: update_status(f"Baixando: {yt.title}..."))
            janela.update()

            ys = yt.streams.get_highest_resolution()
            ys.download(output_path=destino)

            janela.after(0, lambda: update_status("✅ Download CONCLUÍDO!"))
        else:
            janela.after(0, lambda: update_status("❌ Insira uma URL válida"))
    except Exception as e:
        janela.after(0, lambda: update_status(f"❌ ERRO: {e}"))

def threadDownload(): 
    thread_download = threading.Thread(target=ytDownload)
    thread_download.daemon = True
    thread_download.start()

def selecionarPasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        campo_saida.delete(0, END)
        campo_saida.insert(0, pasta_selecionada)

def centralizaJanela(janela, largura_janela, altura_janela):
    janela.update_idletasks()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    pos_x = int((largura_tela / 2) - (largura_janela / 2))
    pos_y = int((altura_tela / 2) - (altura_janela / 2))

    janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

LARGURA_JANELA = 500
ALTURA_JANELA = 350

janela = ctk.CTk()
janela.title("PyTube")
janela.iconbitmap(resource_path("pytube.ico"))
janela.configure(padx=20, pady=20)
janela.columnconfigure(0, weight=1) 

texto_title = ctk.CTkLabel(janela, text="PyTube Downloader", font=("Arial", 18, "bold"))
texto_title.grid(column=0, row=0, pady=10)

texto_p = ctk.CTkLabel(janela, text="Digite a URL do vídeo a ser baixado")
texto_p.grid(column=0, row=1, pady=5, sticky='w', padx=48)

campo_url = ctk.CTkEntry(janela, width=50)
campo_url.grid(column=0, row=2, sticky='we', padx=48, ipady=4) 

saida_txt = ctk.CTkLabel(janela, text="Salvar em:")
saida_txt.grid(column=0, row=3, sticky='w', padx=50)

frame_saida = ctk.CTkFrame(janela)
frame_saida.grid(column=0, row=4, sticky='we', padx=50)
frame_saida.columnconfigure(0, weight=1)

campo_saida = ctk.CTkEntry(frame_saida)
campo_saida.insert(0, os.path.join(os.getcwd(), "downloads"))
campo_saida.grid(column=0, row=0, sticky='we', ipady=4, padx=(0, 5))

botao_navegar = ctk.CTkButton(frame_saida, text="...", command=selecionarPasta, fg_color="#E50914", hover_color="#86181D", width=30)
botao_navegar.grid(column=1, row=0)

down_button = ctk.CTkButton(janela, text="Baixar Vídeo", command=threadDownload, font=("Arial", 12, "bold"), fg_color="#E50914", hover_color="#86181D")
down_button.grid(column=0, row=5, pady=20, sticky='we', padx=50, ipady=5)

status_label = ctk.CTkLabel(janela, text="Status: Aguardando...", anchor='w')
status_label.grid(column=0, row=7, sticky='we', padx=50, ipady=4) 

centralizaJanela(janela, LARGURA_JANELA, ALTURA_JANELA)
janela.mainloop()
