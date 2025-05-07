# Rifters

## Descripción

**Rifters** será un juego de cartas por turnos, inspirado en títulos como *Hearthstone*. El objetivo principal es permitir que dos jugadores se enfrenten en línea, cada uno utilizando su propio mazo de cartas.

Los jugadores podrán:
- Iniciar sesión en la plataforma.
- Visualizar y modificar sus cartas y mazos.
- Crear o unirse a una partida.

Una vez que ambos estén conectados, la partida comenzará y se desarrollará por turnos, permitiendo a cada jugador usar sus cartas de manera estratégica para derrotar al oponente.

Nuestro proyecto estará dividido en tres secciones principales:

**Cliente:** Interfaaz donde los jugadores interactúan con el juego.

**Servidor:** Lógica del juego, gestión de turnos, partidas y conexión con la base de datos.

**Bases de Datos:** Base de datos MySQL que se administrara mediante con phpMyAdmin, donde se almacenan usuarios, cartas, mazos, partidas, etc.

## Requerimientos tecnicos

### Backend (Servidor y Gestión de Datos)

### a. Requisitos del servidor
- **Alojamiento**: Hosting compartido
- **Base de datos**: MySQL con PhpMyAdmin
- **Sistema operativo del servidor**: Windows, con Visual Studio Code como editor

### b. Lenguaje de programación
- Utilizaremos **Python** con el framework **Flask**.

### c. Seguridad
- **Autenticación del Token**: Utilizamos JWT (JSON Web Token) para gestionar la autenticación de los usuarios en la aplicación.

### Frontend

### a. Tipos de Clientes
- Aplicación de consola en escritorio
- Lenguaje de programación: **Python (consola)**


## Requisitos Generales
### a. Gestión de Usuarios y Autenticación
- **Roles de usuario**: Players (jugadores)
- **Base de datos**: MySQL gestionada con PhpMyAdmin en el servidor
- **Autenticación**: Inicio de sesión mediante usuario y contraseña con generación de **Token JWT**
- **Seguridad**: Validación de cada petición protegida con el token. Expiración del token para mayor seguridad.

### b. Almacenamiento Local y Sincronización
- Aunque los datos principales se almacenan en la base de datos del servidor, algunos datos se guardan localmente para mejorar la experiencia del usuario:
  - **Token JWT**
  - **Nombre de usuario (nickname)**
  - **Password**
- Estos datos permiten mantener la sesión activa y validar acciones sin necesidad de múltiples peticiones de autenticación.
- **Seguridad**: La validación de todas las acciones se hace a través del token para asegurar la identidad del usuario.

## Requisitos de Infraestructura
- **Red**: Conexión a Internet
- **Conexión**: Comunicación entre cliente, daos y servidor, con acceso a la base de datos
- **Estructura necesaria**:
  - **Servidor** (API REST en Flask)
  - **Cliente** (aplicación de consola en Python)
  - **DAOs** (objetos de acceso a datos para gestionar usuarios, mazos, cartas y partidas)

## Requisitos del Proceso de Desarrollo

### IDEs y Entorno de Desarrollo
- **Visual Studio Code** como editor principal

### Extensiones recomendadas para VSCode
- **Python**: soporte completo para desarrollo en Python

### Control de Versiones
- **GitHub** como repositorio remoto para trabajo colaborativo y seguimiento del proyecto

### Metodología de Desarrollo
- Se sigue una **metodología ágil**, como **Scrum**, para desarrollar el proyecto en iteraciones cortas, permitiendo validar y ajustar funcionalidades continuamente en base a retroalimentación de usuarios reales.

### Calidad y Pruebas (QA)
- Se implementan **pruebas unitarias** para asegurar la calidad del código y verificar que cada módulo funcione correctamente de forma aislada.
