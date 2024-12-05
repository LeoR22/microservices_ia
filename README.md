# Microservicio TinyLlama con FastAPI

Bienvenido al **Microservicio TinyLlama**, un servicio RESTful basado en **FastAPI** que expone un modelo de lenguaje natural optimizado llamado **TinyLlama**. Este modelo está diseñado para ofrecer consultas SQL dinámicas utilizando lenguaje natural, con un bajo consumo de recursos de hardware gracias a su integración con **Docker**.

Este microservicio permite a partir de entradas en lenguaje natural y puede interactuar, para recuperar información.

# Características

- **Optimización de Recursos**: Utiliza Docker para ejecutar el modelo **TinyLlama** de manera eficiente en términos de recursos de hardware.
- **Microservicio con FastAPI**: Exposición de la funcionalidad como un microservicio RESTful, fácil de integrar con otros sistemas.
  
## Arquitectura

![chatbot](img/Tinyllama.png)

### Flujo General

- **1. Entrada del Usuario**: Se reciben consultas en lenguaje natural a través de la API REST.
- **2. Generación de Consultas**: El modelo **TinyLlama** genera la respuesta correspondiente a partir de la consulta en lenguaje natural.
- **3. Respuesta al Usuario**: Los resultados de la consulta se devuelven en formato amigable para el usuario.

# Instalación

### Clonar el proyecto

```
https://github.com/lriveraBanco/chat-with-lz.git
```

### Configuración el proyecto

Seleccionar el proyecto : Moverse al directorio principal

```
cd microservices_ia
```

### Crear entorno virtual si tienes recursos CPU o GPU para ejecutar este proyecto

```
python3 -m venv venv
```

### Activar entorno virtual

**Para Linux/MacOS**

```
source venv/bin/activate
```

**En Windows:**

```
venv\Scripts\activate
```

### Instalar dependencias

```
pip install -r requirements.txt
```

### ejecutar microservicio de manera local

```
uvicorn main:app --host 0.0.0.0 --port 80 --reload
```

## Dockerizado
### Configurar Docker (si usas Docker para TinyLlama)

Si prefieres ejecutar el modelo en Docker, sigue estos pasos:

1. **Construir la Imagen Docker**:

```
docker build -t nombre_imagen .
```

2. **Ejecutar el Contenedor Docker**:

```
docker run --name nombre_contenedor -d -p 8080:80 nombre_imagen
```

### Configuración de la API del Microservicio FastAPI y USO

Asegúrate de que el microservicio FastAPI esté corriendo antes de consumir el API:
![chatbot](img/postman.png)

```
http://127.0.0.1:8000/ai/chatbot/tinyllama
```



### 2. Interactuar con el Chatbot

Escribe consultas en lenguaje natural, como:

- **"Que es LLMs"**
- **"¿que es tinyllama?"**
- **"Capital de Colombia"**

El chatbot generará respuestas, a tus multiples preguntas.


**Estructura básica del proyecto:**

```plaintext
tinyllama-microservicio/
│
├── api_v1/
│   ├── logic
|       ├──tinyllama.py
│   ├── routes
|       ├──tinyllama.py
|   ├──api.py
|   ├──events.py
├── img/
│   ├── Tinyllama.png            
├── Dockerfile         # Para la construcción del contenedor Docker
├── docs.py
├── requirements.txt   # Dependencias del proyecto
├── main.py            
└── README.md          # Este archivo
```

### Bibliotecas y Herramientas Clave

**FastAPI:** Framework para crear la API RESTful.
**Uvicorn:** Servidor ASGI para ejecutar FastAPI.
**Docker:** Contenedor para ejecutar el modelo TinyLlama de manera eficiente.
**TinyLlama:** El modelo de lenguaje natural que genera respuesta a tus consultas.


## Contribuciones

**Si deseas contribuir a este proyecto, sigue estos pasos:**

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube los cambios a la rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

Leandro Rivera: <lrivera@bancolombia.com.co>

### ¡Feliz Codificación! 🚀

Si encuentras útil este proyecto, ¡dale una ⭐ en GitHub! 😊
