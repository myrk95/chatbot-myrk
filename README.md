# chatbot-myrk

Chatbot Myrk (versión pirata)

Este es un chatbot hecho con Streamlit y Google Gemini. Todo lo que responde lo hace en tono de pirata, como si estuviera en un barco a punto de saquear una isla. Sirve para pruebas, demos y para reírse un rato.

Requisitos

Python 3.10 o superior

pip

Una API key de Google Gemini (variable GOOGLE_API_KEY)

Streamlit

langchain-google-genai

Instalación

Clonar el repositorio:

git clone https://github.com/tu_usuario/chatbot-myrk.git
cd chatbot-myrk


Instalar dependencias:

pip install -r requirements.txt


Configurar la API key:

Linux / macOS:

export GOOGLE_API_KEY="TU_API_KEY"


Windows PowerShell:

setx GOOGLE_API_KEY "TU_API_KEY"

Ejecutar

Para arrancar el chatbot:

streamlit run streamlit_paso2.py


Se abrirá la aplicación en el navegador y podrás chatear con Myrk hablando como un pirata.

Qué hace

Guarda historial de conversaciones

Permite crear y borrar conversaciones

Cambia temperatura y modelo

Muestra mensajes del usuario y del asistente con estilos diferenciados

El asistente siempre responde en tono pirata

Parte importante del modo pirata

Esta línea controla el formato final de la respuesta:

respuesta_formateada = (
    "Argh, grumete, escucha bien... Las mareas me traen esta respuesta:\n\n"
    f"{respuesta.content}"
)


Aquí puedes cambiar el estilo pirata cuando quieras.

Estructura del proyecto
chatbot-myrk/
  streamlit_paso2.py
  requirements.txt
  README.md


Si quieres otro estilo de README (más simple aún, más largo, más corto o 100% pirata), te lo preparo.
