# Imagen de python
FROM python:3.9 AS base

# Directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la app
COPY . .

# Instalamos las dependencias de python
RUN pip install --no-cache-dir -r requirements.txt

# Imagen de node para manejar las dependencias de Node.js y npm
FROM node:14 AS node

# Directorio de trabajo
WORKDIR /app

# Copiamos solo los archivos relacionados con Node.js y npm
COPY package*.json ./

# Instalamos las dependencias de npm
RUN npm install

# Copiamos los archivos de vuelta a la imagen base
FROM base
COPY --from=node /app /app

# Exponemos el puerto
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python3", "app.py"]
