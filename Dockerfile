FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Definimos la ruta para evitar errores de módulos
ENV PYTHONPATH=/app

EXPOSE 8001

# Usamos 'python -m' para invocar uvicorn de forma segura
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]