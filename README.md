
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

## Pasos del Workflow

### 1. Build

- **Se ejecuta en**: `ubuntu-latest`
- **Pasos**:
  - Descarga el código usando `actions/checkout@v4`.
  - Configura Python 3.9 utilizando `actions/setup-python@v4`.
  - Instala las dependencias desde `requirements.txt`.
  - Ejecuta análisis de estilo de código con `flake8` en el directorio `src`.

### 2. Test

- **Se ejecuta en**: `ubuntu-latest`
- **Dependencias**: Este trabajo requiere que el trabajo de `Build` se complete exitosamente.
- **Pasos**:
  - Descarga el código.
  - Configura Python 3.9.
  - Instala las dependencias.
  - Ejecuta las pruebas con `pytest`.

### 3. Empaquetado en Docker

- **Se ejecuta en**: `ubuntu-latest`
- **Dependencias**: Requiere que el trabajo de `pruebas` pase exitosamente.
- **Condiciones**: Solo se ejecuta en la rama `develop`.
- **Pasos**:
  - Inicia sesión en el Registro de Contenedores de GitHub.
  - Construye la imagen de Docker etiquetada como `ghcr.io/<nombre-repositorio>:develop`.
  - Envía la imagen de Docker al Registro de Contenedores de GitHub.

### 4. Despliegue

- **Se ejecuta en**: `ubuntu-latest`
- **Dependencias**: Requiere que el trabajo de `empaquetado en Docker` sea exitoso.
- **Condiciones**: Solo se ejecuta en la rama `develop`.
- **Pasos**:
  - Configura la conexión SSH al servidor remoto usando `webfactory/ssh-agent@v0.9.0` y la clave SSH privada almacenada en los secretos.
  - Agrega la clave de host del servidor SSH a los hosts conocidos.
  - Inicia sesión en el registro de Docker en el servidor remoto.
  - Ejecuta `docker-compose` en el directorio `backend` del servidor para iniciar la aplicación.
  - Elimina las imágenes de Docker no utilizadas para liberar espacio.
  - Cierra sesión del registro de Docker en el servidor remoto.

## Variables de Entorno y Secretos

Las siguientes variables de entorno y secretos se utilizan en este workflow:

- **Variables de Entorno**:
  - `DEVELOP_SSH_HOST`: Nombre de host o dirección IP del servidor de despliegue.
  - `DEVELOP_SSH_USERNAME`: Nombre de usuario para el acceso SSH.
  - `DOCKER_REGISTRY_USER`: Nombre de usuario para el registro de Docker.

- **Secretos**:
  - `DEVELOP_SSH_SECRET`: Clave SSH privada para el acceso al servidor de despliegue.
  - `GITHUB_TOKEN`: Token de GitHub para autenticación en el Registro de Contenedores de GitHub.
  - `DOCKER_REGISTRY_TOKEN`: Token del registro de Docker para iniciar sesión en el registro de contenedores.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
