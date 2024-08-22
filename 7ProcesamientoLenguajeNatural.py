# Preprocesamiento BASICO de texto....
# Acciones en Mineria de Texto
# AMPLIAR: https://python.recursocreativo.es/guia-completa-nltk-en-python-procesamiento-de-lenguaje-natural-paso-a-paso/
import nltk
nltk.download('all') 
#nltk.download() #utilizar para descargar e instalar nuevos paquetes. 
nltk.download('punkt')  # módulo que divide un texto en frases mediante un algoritmo no supervisado.
nltk.download('popular')
nltk.download('stopwords')
#!pip install --upgrade nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#texto = "tennis Nick likes to play football and tennis, however he is not too fond of tennis."
texto="Este es el curso de Inteligencia Artificial de la Universidad Nacional de Colombia. La inteligencia colectiva es un patrimonio de todos."
# cargando texto


#STOP WORDS
text_tokens = word_tokenize(texto)
tokens_without_sw = [
    word for word in text_tokens if not word in stopwords.words('spanish')]

print(tokens_without_sw)
texto=tokens_without_sw

textoA = ""
for i in range(0, len(texto)):
    textoA = textoA + " " + texto[i]
texto=textoA
print(texto)