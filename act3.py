# Dependencias de des
import google.genai as genai
from dotenv import load_dotenv 
import os


"""
Cargamos las variables de entorno
"""

load_dotenv()
API_KEY= os.getenv("API_KEY") 

"""
Instanciamos el cliente y hacemos la petición
"""

client = genai.Client(api_key=API_KEY)


response = client.models.generate_content(
model= "gemini-2.5-flash",
contents="Por que es importante hacer chequeos de seguridad?"
)
print("--------------------------RESPUESTA--------------------------")
print(response.text)