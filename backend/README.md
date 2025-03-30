# Backend - Gestión de Pacientes (Valentech)

Este backend implementa una API REST construida con Flask para registrar y consultar pacientes. Está contenida con Docker y usa PostgreSQL como base de datos. Se sigue el patrón MVC con buenas prácticas de Clean Code.

---

##  Tecnologías Usadas

- Python 3.10
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Docker & Docker Compose
- Requests (para consumo de API externa)
- pytest (para pruebas unitarias)

---

## requisitos previos

- Python 3.10 (si lo ejecutas fuera de Docker)
- pip
- Docker y Docker Compose

---

## Ejecución con Docker (recomendado)

```bash
docker-compose up --build
```

Esto levantará el backend, frontend y la base de datos PostgreSQL.

---

## Instalación local (sin Docker)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
python run.py
```

La API estará disponible en:  
👉 http://localhost:5000/api/patients/

---

## Estructura del Proyecto
```
backend/
├── app/
│   ├── controllers/
│   │   ├── patient_controller.py
│   │   └── ping_controller.py
│   ├── models/
│   │   └── patient.py
│   ├── routers/
│   │   ├── patient_routes.py
│   │   └── ping_routes.py
│   ├── services/
│   │   └── patient_service.py
│   ├── __init__.py
│   └── config.py
├── migrations/
├── tests/
│   └── test_patient.py
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```


## 🧪 Pruebas unitarias

```bash
docker-compose exec backend pytest
```

Las pruebas están desacopladas de la base de datos real usando `unittest.mock`.

---