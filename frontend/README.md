#  Frontend - Gestión de Pacientes

Este proyecto es el **frontend** de la aplicación de gestión de pacientes, desarrollado en **Angular 15** con **Bootstrap** para un diseño limpio y responsivo.

---

##  Tecnologías utilizadas

- [Angular 15](https://angular.io/)
- [Bootstrap 5](https://getbootstrap.com/)
- HTML + SCSS
- Consumo de API REST

---

## ▶ Requisitos previos

NOTA: Si desea ejecutar el docker puede usar el archivo DockerFile (Posterior encuentra su uso)

- [Node.js](https://nodejs.org/) (v16 o superior recomendado)
- [Angular CLI](https://angular.io/cli)


---

## Instalación local

```bash
cd frontend
npm install
```

---

## Ejecutar en modo desarrollo

```bash
ng serve
```

Accede en tu navegador a:  
- http://localhost:4200

---

## Configuración de entorno

Modificar la URL de la API backend en:

```ts
# src/environments/environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:5000/api/patients/'
};
```

En producción (Docker), se usa:

```ts
apiUrl: 'http://backend:5000/api/patients/'
```

---

## Build de producción

```bash
ng build
```

El contenido compilado se genera en `dist/frontend` y es servido con Nginx mediante Docker.

---

## Docker (modo integrado)
Este proyecto requiere Docker y Docker Compose para funcionar correctamente.

"En la carpeta main de este proyecto puede ver la instalacion de docker y docker-compose."

El frontend se construye automáticamente cuando ejecutas:

```bash
docker-compose up --build
```

Y se expone en:  
👉 http://localhost:4200

---

## Funcionalidades

- Formulario para registrar pacientes
- Validación externa usando Random User API
- Listado dinámico de pacientes
- Búsqueda por nombre y enfermedad
- Toasts y loaders visuales
- Routing entre componentes

---

## Estructura relevante

```
src/
├── app/
│   ├── pages/
│   │   ├── patient-form/      # Formulario de registro
│   │   └── patient-list/      # Listado de pacientes
│   ├── services/              # Servicio API
│   ├── models/                # Interfaces
│   └── components/navbar/     # Menú de navegación
├── environments/              # Configuración de entorno
```

---
