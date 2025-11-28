import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage

# ---------------------------
# ESTILO DE FONDO PRINCIPAL
# ---------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #7ec8e3, #4aa3c0); /* Azul oceánico */
        color: #001f2e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------
st.set_page_config(page_title="Chatbot Myrk")
st.title("Chatbot Myrk  El Bucanero del Ciber-Mar ")
st.markdown("Argh, grumete… soy **Myrk**, capitán de estas aguas digitales. Habla si te atreves.")

# ---------------------------
# INICIALIZAR HISTORIALES
# ---------------------------
if "conversaciones" not in st.session_state:
    st.session_state.conversaciones = [[]]
if "conversacion_activa" not in st.session_state:
    st.session_state.conversacion_activa = 0

# ---------------------------
# MENÚ LATERAL
# ---------------------------
with st.sidebar:
    st.header("Ajustes del Navío")
    temperatura = st.slider("Temperatura (bravura del mar)", 0.0, 1.5, 0.7, 0.1)
    modelo = st.selectbox(
        "Modelo del Oráculo del Kraken",
        ["gemini-2.5-flash", "gemini-1.5-flash"],
        index=0
    )

    st.header("Herramientas del Capitán")

    if st.button("Nueva travesía"):
        st.session_state.conversaciones.append([])
        st.session_state.conversacion_activa = len(st.session_state.conversaciones) - 1

    if st.button("Hundir travesía actual"):
        if st.session_state.conversaciones:
            st.session_state.conversaciones.pop(st.session_state.conversacion_activa)
            if len(st.session_state.conversaciones) == 0:
                st.session_state.conversaciones = [[]]
            st.session_state.conversacion_activa = min(
                st.session_state.conversacion_activa,
                len(st.session_state.conversaciones) - 1
            )

    if st.button("Limpiar bitácora"):
        st.session_state.conversaciones[st.session_state.conversacion_activa] = []

    st.header("Bitácoras del Barco")
    if st.session_state.conversaciones:
        conv_index = st.radio(
            "Selecciona tu bitácora",
            options=list(range(len(st.session_state.conversaciones))),
            format_func=lambda i: f"Travesía {i+1}",
            index=st.session_state.conversacion_activa
        )
        st.session_state.conversacion_activa = conv_index

    # Historial coloreado
    st.header("Registros del Viaje")
    for msg in st.session_state.conversaciones[st.session_state.conversacion_activa]:
        if isinstance(msg, HumanMessage):
            st.markdown(
                f"<div style='background-color:#b6e3f3; padding:8px; border-radius:10px; margin-bottom:5px;'>"
                f"<b>Grumete:</b> {msg.content}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='background-color:#ffe7c2; padding:8px; border-radius:10px; margin-bottom:5px;'>"
                f"<b>Myrk:</b> {msg.content}</div>",
                unsafe_allow_html=True
            )

# ---------------------------
# CREAR INSTANCIA DEL MODELO
# ---------------------------
chat_model = ChatGoogleGenerativeAI(
    model=modelo,
    temperature=temperatura
)

# ---------------------------
# INPUT DEL USUARIO
# ---------------------------
pregunta = st.chat_input("¡Habla, grumete!")

if pregunta:
    # Guardar mensaje del usuario
    st.session_state.conversaciones[st.session_state.conversacion_activa].append(
        HumanMessage(content=pregunta)
    )

    with st.chat_message("user"):
        st.markdown(
            f"<div style='background-color:#b6e3f3; padding:8px; border-radius:10px;'>{pregunta}</div>",
            unsafe_allow_html=True
        )

    # Preparar historial
    historial_formateado = [
        {"role": "user", "content": m.content} if isinstance(m, HumanMessage)
        else {"role": "assistant", "content": m.content}
        for m in st.session_state.conversaciones[st.session_state.conversacion_activa]
    ]

    # Obtener respuesta
    respuesta = chat_model.invoke(historial_formateado)

    # ----------- ESTILO PIRATA TOTAL -----------
    respuesta_formateada = (
        "🏴‍☠️ **Argh, escucha bien grumete…**<br>"
        "Los vientos del mar, el canto del Kraken y el ron del capitán traen esta respuesta pa’ tus oídos:<br><br>"
        f"🦜 {respuesta.content}"
    )
    # --------------------------------------------

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.markdown(
            f"<div style='background-color:#ffe7c2; padding:8px; border-radius:10px;'>{respuesta_formateada}</div>",
            unsafe_allow_html=True
        )

    # Guardar respuesta
    st.session_state.conversaciones[st.session_state.conversacion_activa].append(
        AIMessage(content=respuesta_formateada)
    )
