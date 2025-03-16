import tkinter as tk
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Descargar los datos de NLTK (Solo la primera vez)
nltk.download('vader_lexicon')
nltk.download('punkt')

# Inicializar el analizador de sentimientos
analyzer = SentimentIntensityAnalyzer()

# Respuestas según el sentimiento
RESPUESTAS_POSITIVAS = ["¡Eso suena genial! 😊", "Me alegra escuchar eso. 😃", "¡Sigue así! 💪"]
RESPUESTAS_NEGATIVAS = ["Lo siento mucho. 😞", "Espero que las cosas mejoren. 💙", "Estoy aquí para escucharte. 🤗"]
RESPUESTAS_NEUTRAS = ["Interesante. 😐", "Cuéntame más. 🤔", "Eso suena bien. 👍"]

def analizar_sentimiento(texto):
    sentimiento = analyzer.polarity_scores(texto)
    
    if sentimiento['compound'] >= 0.05:
        return RESPUESTAS_POSITIVAS
    elif sentimiento['compound'] <= -0.05:
        return RESPUESTAS_NEGATIVAS
    else:
        return RESPUESTAS_NEUTRAS

def enviar_mensaje():
    mensaje_usuario = entrada_texto.get()
    if mensaje_usuario:
        respuestas = analizar_sentimiento(mensaje_usuario)
        respuesta_bot = respuestas[0]  # Seleccionamos la primera respuesta

        historial_texto.insert(tk.END, "Tú: " + mensaje_usuario + "\n", "usuario")
        historial_texto.insert(tk.END, "Bot: " + respuesta_bot + "\n", "bot")
        entrada_texto.delete(0, tk.END)

# Configuración de la ventana de chat
ventana = tk.Tk()
ventana.title("Chatbot con NLTK y Análisis de Sentimiento")

historial_texto = tk.Text(ventana, height=20, width=50)
historial_texto.tag_config("usuario", foreground="blue")
historial_texto.tag_config("bot", foreground="green")
historial_texto.pack()

entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

ventana.mainloop()
