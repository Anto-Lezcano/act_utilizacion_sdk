# Consumo de la API de Gemini con Python (Google AI Studio)

Este proyecto muestra cómo configurar un entorno en Python para consumir la API de Gemini, incluyendo ejemplos con `generate_content` y `generate_content_stream`.

---

## 📌 Elección: Gemini vs Vertex AI (Resumen)

Para una startup que necesita resultados rápidos y con bajo presupuesto, **la API de Gemini es la mejor opción**, ya que permite integrar IA sin infraestructura compleja ni costos elevados. **Vertex AI** se recomienda más adelante, cuando el proyecto requiera mayor seguridad, monitoreo y escalabilidad en Google Cloud.

---

## ✅ Requisitos Previos

- Python 3.10+
- Una API Key de **Google AI Studio** → https://aistudio.google.com
- `pip` instalado

---

## ⚙️ Configuración del Entorno

### 1. Crear entorno virtual

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install google-genai python-dotenv
```

### 3. 🔑Configura tu APIkey

En un archivo _.env_
API_KEY=TU_API_KEY_AQUI

### 4. Probar

### 📌 generate_content (respuesta completa)

```bash
python act3.py
```

- Respuesta completa en un solo output

### 📌 generate_content_stream (respuesta más rápida en tiempo real)

```bash
python act4.py
```

- Respuesta más rápida, ideal para textos largos o tiempo real

### 📌 generate_content_stream (analisis de imagen)

```bash
python act5.py
```
