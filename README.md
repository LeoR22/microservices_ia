# Microservicio TinyLlama con FastAPI

Bienvenido al **Microservicio TinyLlama**, un servicio RESTful basado en **FastAPI** que expone un modelo de lenguaje natural optimizado llamado **TinyLlama**. Este modelo está diseñado para ofrecer consultas SQL dinámicas utilizando lenguaje natural, con un bajo consumo de recursos de hardware gracias a su integración con **Docker**.

Este microservicio genera consultas SQL a partir de entradas en lenguaje natural y puede interactuar con bases de datos, como Impala, para recuperar información.

# Características

- **Consultas SQL en Lenguaje Natural**: Convierte consultas en lenguaje natural a SQL ejecutable.
- **Optimización de Recursos**: Utiliza Docker para ejecutar el modelo **TinyLlama** de manera eficiente en términos de recursos de hardware.
- **Integración con Bases de Datos**: Conecta con **Impala** para ejecutar las consultas generadas.
- **Microservicio con FastAPI**: Exposición de la funcionalidad como un microservicio RESTful, fácil de integrar con otros sistemas.
  
## Arquitectura

![chat-lz](docs/chat_lz.png)

### Flujo General

**1. Entrada del Usuario**: Se reciben consultas en lenguaje natural a través de la API REST.
**2. Generación de Consultas SQL**: El modelo **TinyLlama** genera la consulta SQL correspondiente a partir de la consulta en lenguaje natural.
**3. Ejecución de la Consulta**: La consulta SQL es ejecutada en la base de datos **Impala**.
**4. Respuesta al Usuario**: Los resultados de la consulta se devuelven en formato amigable para el usuario, junto con la consulta SQL generada.

# Instalación

### Clonar el proyecto

```
https://github.com/lriveraBanco/chat-with-lz.git
```

### Configuración el proyecto

Seleccionar el proyecto : Moverse al directorio principal

```
cd chat-with-lz
```

### Crear entorno virtual

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

### Configurar Docker (si usas Docker para TinyLlama)

Si prefieres ejecutar el modelo en Docker, sigue estos pasos:

1. **Construir la Imagen Docker**:

```
pip install -r requirements.txt
```

2. **Ejecutar el Contenedor Docker**:

```
pip install -r requirements.txt
```

3. **Verifica que el contenedor está funcionando correctamente ejecutando**:

```
pip install -r requirements.txt
```

### Ejecutar el Microservicio FastAPI

Para iniciar el microservicio, ejecuta:

```
pip install -r requirements.txt
```

### Configuración de la API del Microservicio FastAPI

Asegúrate de que el microservicio FastAPI esté corriendo antes de iniciar la aplicación Streamlit. Puedes configurarlo en tu archivo .env o directamente en el código de Streamlit con la URL del microservicio:

```
FASTAPI_URL=http://127.0.0.1:8000/query
```

# USO

### 1. Ejecutar la Aplicación de Streamlit

Inicia la aplicación con el siguiente comando:

```
streamlit run app.py
```

### 2. Interactuar con el Chatbot

Escribe consultas en lenguaje natural, como:

- **"Muestra los registros más recientes para la API X."**
- **"¿Cuál es el esquema de la tabla Y?"**
- **"Obtén el promedio de usuarios por API en los últimos tres meses."**

El chatbot generará consultas SQL, las ejecutará y mostrará los resultados.
Use the sidebar to initialize the connection to the proceso_apis database.

**Estructura básica del proyecto:**

```plaintext
tinyllama-microservicio/
│
├── docs/
│   ├── microservice_architecture.png
├── src/
│   ├── main.py        # Archivo principal con FastAPI
│   ├── model.py       # Lógica del modelo TinyLlama
│   ├── utils.py       # Funciones auxiliares
├── Dockerfile         # Para la construcción del contenedor Docker
├── requirements.txt   # Dependencias del proyecto
├── .env               # Variables de entorno
└── README.md          # Este archivo
```

### Bibliotecas y Herramientas Clave

**FastAPI:** Framework para crear la API RESTful.
**Uvicorn:** Servidor ASGI para ejecutar FastAPI.
**Docker:** Contenedor para ejecutar el modelo TinyLlama de manera eficiente.
**TinyLlama:** El modelo de lenguaje natural que genera consultas SQL.
**Impala:** Base de datos para ejecutar las consultas generadas.

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
