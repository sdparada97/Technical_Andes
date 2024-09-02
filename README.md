# TECHNICAL-ANDES

Microservicio Documentación Pokedex

## Technologies

<div align="center">
 <img width="200" src="https://github.com/sdparada97/Technical_Andes/blob/main/assets/fastapi.png" alt="Fastapi" title="Fastapi"/>
 <img width="80" src="https://github.com/sdparada97/Technical_Andes/blob/main/assets/mongodb.png" alt="Mongo" title="Mongo"/>
 <img width="80" src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" alt="pytest" title="pytest"/>
</div>

### Arquitectura

El diseño que se implementara tendra conceptos relacionados con arquitecturas limpias:

* Patron Repositorio
* Capa de servicio
* Controladores

Estos conceptos estan implmentados en este microservicio donde se enctran en los siguientes directorios:

* VIEWS:
  * En estos ficheros encontraremos las acciones especificas y el manejo de peticiones entrantes, donde se puedan controlar caracteristicas como (Excepciones HTTP, Esquemas Request/Response)

* SERVICES:
  * En estos ficheros tienen la responsabilidad de implmentar la logica del negocio y actua como una zona de abstracción entre la zona de datos y los controladores.

* REPOSITORY:
  * En estos ficheros se encargan de separar la logica del negocio del acceso hacia los datos

Esto hace que haya una mayor independencia de todas las capas y esto nso brinda muchos beneficios como lo es la flexibilidad, mantenibilidad y para realizar pruebas es mucho mas sencillo.

## Pruebas de documentacion:
![image](https://github.com/user-attachments/assets/7ca62ea1-67ad-4c69-bd1b-1cf48c48f41a)

![image](https://github.com/user-attachments/assets/242416a6-7592-49e3-bd33-cd1e14d8d0c0)

![image](https://github.com/user-attachments/assets/badb3d76-1886-48f7-ae52-37c7be60f82f)

![image](https://github.com/user-attachments/assets/83aa5132-8722-4f13-ac15-f749eff11fdf)

## OpenAPI (Swagger)
![image](https://github.com/user-attachments/assets/70978bc5-3539-4b3a-ba02-fcd227dfe3fd)

## Instalación

Este `Makefile` te ayudará a automatizar la construcción, ejecución y limpieza de contenedores Docker para tu proyecto **Technical_Habi**. Sigue los pasos a continuación para utilizar cada comando disponible.

### Comandos Disponibles

| Comando           | Descripción                                      |
|-------------------|--------------------------------------------------|
| `make build-local`      | Construye la imagen Docker del proyecto.         |
| `make up-local`        | Ejecuta el contenedor Docker.                    |
| `make down-local`       | Detiene la ejecución del contenedor Docker.      |
| `make clear`      | Elimina el contenedor Docker.                    |
| `make test`       | Ejecuta los tests dentro del contenedor Docker.  |

## Pasos para Usar el Makefile

### 1. Construir la Imagen Docker

Para construir la imagen Docker de tu proyecto, ejecuta el siguiente comando:

```bash
make build-local
```

Este comando construirá la imagen utilizando el Dockerfile en tu directorio actual..

### 2. Ejecutar el Contenedor Docker

Para iniciar el contenedor, usa:

```bash
make up-local
```

Este comando ejecutará el contenedor y lo expondrá en el puerto 8000.

### 3. Detener el Contenedor

Para detener la ejecución del contenedor, utiliza:

```bash
make down-local
```

Este comando detendrá el contenedor que se está ejecutando.

### 4. Eliminar el Contenedor

Si necesitas eliminar el contenedor, ejecuta:

```bash
make clear
```

<span style="background:#53b418"> DENTRO DEL PROYECTO ESTARA LA COLECCION DE POSTMAN QUE PODRA IMPORTARLA DIRECTAMENTE Y REALIZAR LAS PETICIONES CUANDO TENGA EL PROYECTO ARRIAB CON EL DOCKER </span>
