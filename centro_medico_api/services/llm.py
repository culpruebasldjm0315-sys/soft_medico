import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def consultar_llm(mensaje: str) -> str:
    prompt = f"""<|system|>
Eres un asistente médico. Ayuda al paciente a describir sus síntomas y brinda un posible diagnóstico general. Siempre recomienda consultar a un médico.
</s>
<|user|>
{mensaje}
</s>
<|assistant|>"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result[0]["generated_text"].strip()
    except Exception as e:
        return f"Error al consultar el modelo: {str(e)}"