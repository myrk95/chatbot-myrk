# Chatbot Myrk (versión pirata)

Chatbot creado con Streamlit y Google Gemini. Todas las respuestas se dan en tono pirata. Ideal para pruebas, demos o diversión.

## Requisitos

- Python 3.10 o superior
- pip
- API Key de Google Gemini (variable: GOOGLE_API_KEY)
- Streamlit
- langchain-google-genai

## Instalación

## Clonar el repositorio:

git clone https://github.com/tu_usuario/chatbot-myrk.git

cd chatbot-myrk

## Instalar dependencias:

pip install -r requirements.txt

## Configurar la API key:

Linux / macOS:

export GOOGLE_API_KEY="TU_API_KEY"

## Windows PowerShell:

setx GOOGLE_API_KEY "TU_API_KEY"

## Ejecución

Para arrancar la aplicación:

streamlit run streamlit_paso2.py

https://chatbot-myrk-f6yhrrh8zcn4rvv2aifrb9.streamlit.app/

La aplicación se abrirá en el navegador.

## Funcionalidades

- Historial de conversaciones
- Crear nuevas conversaciones
- Eliminar conversaciones
- Limpiar una conversación actual
- Ajustar modelo y temperatura
- Respuestas siempre en tono pirata

## Modo pirata

El efecto pirata se controla en esta parte del código:

respuesta_formateada = (
"Argh, grumete, escucha bien... Las mareas me traen esta respuesta:\n\n"
f"{respuesta.content}"
)


Puedes editar ese texto para cambiar el estilo pirata cuando quieras.


## Estructura del proyecto

- chatbot-myrk/
- streamlit_paso2.py
- requirements.txt
- README.md
