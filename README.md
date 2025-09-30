# 🐍 PyTube Downloader

**Projeto de utilitário *desktop***, desenvolvido em Python para download automatizado de conteúdo do YouTube na mais alta resolução disponível. A arquitetura é otimizada para estabilidade e responsividade em ambientes Windows.

## ⚙️ Arquitetura e Especificações Técnicas

| Módulo | Função | Detalhes |
| :---: | :---: | :--- |
| **Interface (GUI)** | CustomTkinter (CTk) | Implementa o *design system* moderno com suporte nativo a **Dark Mode** e widgets *custom* para UX aprimorada. |
| **Performance** | `threading` | Executa a operação I/O (download) em uma *thread* secundária para garantir que a *thread* principal da GUI permaneça desbloqueada (*non-blocking*). |
| **Lógica Core** | `pytubefix` | Gerencia a conexão com a API do YouTube para *stream* e download de mídia. |
| **Distribuição** | PyInstaller | Empacotamento para um único executável (`.exe`). |

## 🚀 Guia de Início Rápido (Quick Start)

Para utilizar o aplicativo sem a necessidade de instalar dependências Python, utilize o arquivo executável.

### Download do Binário

O executável mais recente (`PyTubeDownloader.exe`) está disponível para download na página de **[Releases](https://github.com/leogpava/pytubedownloader/releases)**.

## 🧑‍💻 Configuração para Desenvolvimento

Para executar o projeto a partir do código-fonte e modificar a arquitetura, siga os passos abaixo:

### Pré-requisitos

* Python 3.x
* Git

### Instalação

1.  Clone o repositório e navegue até o diretório:
    ```bash
    git clone [https://github.com/leogpava/pytubedownloader.git](https://github.com/leogpava/pytubedownloader.git)
    cd pytubedownloader
    ```

2.  Crie e ative o ambiente virtual (Recomendado):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate 
    ```
    *(Para Linux/macOS, use `source venv/bin/activate`)*

3.  Instale as dependências:
    ```bash
    pip install customtkinter pytubefix
    ```

4.  Execute a aplicação:
    ```bash
    python main.py
    ```

## 🛠️ Empacotamento e Build

Para gerar uma nova versão do executável, garanta que o `pyinstaller` esteja instalado na sua *venv* e utilize o comando de *build* final, que resolve dependências ocultas e empacota recursos:

```bash
# Comando para geração do executável (Windows, OneFile, NoConsole)
pyinstaller --onefile -w --name="PyTubeDownloader" --icon=pytube.ico --hidden-import=customtkinter --add-data "pytube.ico;." main.py
