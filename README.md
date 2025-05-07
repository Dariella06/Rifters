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




