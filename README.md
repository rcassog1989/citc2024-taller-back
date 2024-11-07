
# FastAPI Application with Docker

Este proyecto es una aplicación API construida con FastAPI y Docker. La estructura de carpetas es `core`, `infrastructure`, `presentation`, para mantener la arquitectura limpia y modular.

## Estructura de Archivos

El proyecto sigue la siguiente estructura de carpetas:

```
.
├── main.py                    # Archivo principal para iniciar la aplicación FastAPI
├── Dockerfile                 # Archivo Docker para crear una imagen de la aplicación
├── requirements.txt           # Lista de dependencias de Python
├── src/                       # Carpeta principal del código fuente
│   ├── core/                  # Módulos centrales, abstracciones y servicios
│   ├── infrastructure/        # Implementación de dependencias y repositorios
│   ├── presentation/          # Controladores para manejar las rutas de la API
```

## Configuración

1. **Crea un fork de este repositorio**:

   ```bash
   https://github.com/samuelloza/citc2024-taller-back
   ```

2. **Clone este repositorio**

   ```bash
   git clone url
   cd citc2024-taller-back
   ```

3. **Crea un entorno virtual**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows `venv\Scripts\activate`
   ```

4. **Instala las dependencias del archivo `requirements.txt`**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta el proyecto**:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
   ```

   Esto levantará el servidor en `http://localhost:8000`.  
   Para ver la documentación interactiva, abre `http://localhost:8000/docs` en tu navegador.

## Configuración con Docker

Para construir la imagen de Docker de la aplicación, ejecuta el siguiente comando en el directorio raíz del proyecto:

```bash
docker build -t citc2024-taller-back:develop .
```

Este comando construirá una imagen de Docker llamada `citc2024-taller-back:develop` usando el `Dockerfile`

## Ejecutar el Contenedor Docker

Para ejecutar el contenedor de Docker una vez que la imagen se haya creado, usa el siguiente comando:

```bash
docker run -it -p 8000:8000 citc2024-taller-back:develop
```

Esto iniciará el servidor de FastAPI y estará disponible en `http://localhost:8000`.

## Uso

- Para verificar que el servidor está en ejecución, abre tu navegador y navega a `http://localhost:8000/docs` para acceder a la interfaz de documentación Swagger.

## Ejemplo de Dockerfile

```Dockerfile
# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requirements y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos
COPY . .

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
```

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
