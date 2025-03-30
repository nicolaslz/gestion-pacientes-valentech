# Sistema de Gestión de Pacientes 

## Introducción

Este proyecto es una solución de software fullstack diseñada para gestionar el registro y la consulta de pacientes de forma eficiente, moderna y portable.

Incluye un frontend desarrollado en **Angular 15** con diseño responsivo usando **Bootstrap**, y un backend creado con **Flask (Python)** y base de datos **PostgreSQL**, todo orquestado con **Docker**.

El sistema está pensado para ser **fácil de desplegar localmente o en la nube**, e incluye buenas prácticas de desarrollo como:

- Separación de responsabilidades (Frontend, Backend, DB)
- Validaciones externas usando APIs públicas
- Pruebas automatizadas en el backend
- Experiencia de usuario fluida con loaders y toasts
- Arquitectura limpia (MVC)

Nota: Para el proyecto usamos docker lo cual nos facilita la no instalacion de dependencias locales ademas de las dependencias de versiones.

## Tecnologías utilizadas

- Frontend: Angular 15 + Bootstrap
- Backend: Flask + SQLAlchemy (ORM)
- Base de Datos: PostgreSQL
- Orquestación: Docker + Docker Compose
- Extras:
  - Clean Architecture (MVC)
  - Toasts + Loaders
  - Validaciones con API externa
  - Pruebas unitarias del backend con `pytest`

## ¿Cómo ejecutar el proyecto con Docker?

### Requisitos previos

- Tener Docker y Docker Compose instalados

## Paso 1: Clonar el repositorio

```bash
git clone https://github.com/nicolaslz/gestion-pacientes-valentech.git
cd gestion-pacientes-valentech
```

## Paso 2: Instalación de Docker y Docker Compose

Este proyecto requiere Docker y Docker Compose para funcionar correctamente.

### 🔹 Windows 10/11

1. Descargar e instalar Docker Desktop:  
   👉 https://www.docker.com/products/docker-desktop/

2. Asegúrate de tener WSL2 activado (Docker Desktop lo guía si es necesario).

3. Verifica que Docker funciona:

```bash
docker -v
docker-compose -v
```

---

### 🔹 macOS (Intel o Apple Silicon)

1. Descargar Docker Desktop:  
   👉 https://www.docker.com/products/docker-desktop/

2. Instalar y abrir Docker. Asegúrate de aceptar los permisos del sistema.

3. Verificar:

```bash
docker -v
docker-compose -v
```

---

### 🔹 Linux (Ubuntu/Debian)

1. Instalar Docker Engine (guía oficial):  
   👉 https://docs.docker.com/engine/install/

2. Instalar Docker Compose plugin:  
   👉 https://docs.docker.com/compose/install/linux/

3. Agrega tu usuario al grupo docker (opcional):

```bash
sudo usermod -aG docker $USER
newgrp docker
```
---

## 🚀 ¿Cómo ejecutar el proyecto con Docker?

### ▶️ Paso 1: Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestion-pacientes.git
cd gestion-pacientes
```

### ▶️ Paso 2: Ejecutar el entorno completo

```bash
docker-compose up --build
```

> Esto construirá y levantará los 3 servicios: backend, frontend y base de datos.

---

## 🌐 Accesos

| Servicio   | URL                       |
|------------|---------------------------|
| Frontend   | http://localhost:4200     |
| Backend API| http://localhost:5000/api |
| PostgreSQL | localhost:5432 (interno)  |

---

### Ejecución 

Luego de tener instalado docker y docker-compose

```bash
docker-compose up --build
```

## 📁 Estructura del proyecto

```
.
├── backend/            # Backend en Flask
│   ├── app/            # Código fuente del backend
│   ├── tests/          # Pruebas unitarias
│   ├── Dockerfile
│   ├── requirements.txt
│   └── run.py
│
├── frontend/           # Frontend Angular
│   ├── src/            # Componentes, servicios y vistas
│   ├── Dockerfile
│   └── nginx.conf
│
├── docker-compose.yml  # Orquestación de servicios
└── README.md            # Este archivo
```

## Variables de entorno
NOTA: En producción podrías usar .env y definir:

DATABASE_URL=postgresql://postgres:password@db:5432/valentechdb
Actualmente están embebidas en docker-compose.yml para simplicidad en desarrollo.

## 👨‍💻 Autor
Tu Nombre: Nicolas Garcia
Tu GitHub: @nicolaslz

