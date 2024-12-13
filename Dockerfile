# Usar imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos requeridos
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
