# Usa una imagen de Python
FROM python:3.11-slim

# Define el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto del servidor Flask
EXPOSE 5000

# Ejecuta la aplicación
CMD ["python", "app.py"]

