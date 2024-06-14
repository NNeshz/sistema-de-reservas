# Documentación Frontend

## Instalación

Para instalar las dependencias del proyecto, necesitas tener instalado [Node.js](https://nodejs.org/). Luego, ejecuta el siguiente comando en la terminal:

```bash
npm install
```
Este comando instalará todas las dependencias necesarias para el proyecto.

## Ejecución

Para ejecutar el proyecto, ejecuta el siguiente comando en la terminal:

```bash
npm run dev // Para ejecutar en modo desarrollo
npm run build // Para compilar el proyecto
npm run start // Para ejecutar en modo producción
```

## Estructura de archivos

La estructura de archivos del proyecto es la siguiente:

### Carpeta `app`

En esta carpeta se encuentran los archivos que tienen que ver con el rutado de la aplicación así como su funcionalidad con diferentes archivos como lo son "actions.ts" y "auth.ts",

### Carpeta `components`

En esta carpeta se encuentran los componentes de la aplicación, los cuales se dividen en dos carpetas, "pages" y "ui && magicui". Estos vienen por parted de [shadcn](https://ui.shadcn.com/) y [magicui](https://magicui.design/). Todos los componentes estan estilado con [TailwindCSS](https://tailwindcss.com/).