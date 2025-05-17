# Rifters

## Descripción del Proyecto Rifters

**Rifters** será un juego de cartas por turnos, inspirado en títulos como *Hearthstone*. El objetivo principal es permitir que dos jugadores se enfrenten en línea, cada uno utilizando su propio mazo de cartas.

Los jugadores podrán:
- Iniciar sesión en la plataforma.
- Visualizar y modificar sus cartas y mazos.
- Crear o unirse a una partida.

Una vez que ambos estén conectados, la partida comenzará y se desarrollará por turnos, permitiendo a cada jugador usar sus cartas de manera estratégica para derrotar al oponente.

Nuestro proyecto estará dividido en tres secciones principales:

**Cliente:** Interfaz donde los jugadores interactúan con el juego.

**Servidor:** Lógica del juego, gestión de turnos, partidas y conexión con la base de datos.

**Bases de Datos:** Base de datos MySQL que se administrará mediante phpMyAdmin, donde se almacenan usuarios, cartas, mazos, partidas, etc.

## Requisitos Técnicos del Proyecto

En este apartado describimos todos los requerimientos técnicos necesarios para el desarrollo de nuestro juego y ejecución del proyecto. Aquí detallamos tanto los aspectos del backend (servidor y lógica de negocio), como del frontend (cliente), infraestructura, herramientas de desarrollo y consideraciones de seguridad.

Enlace para ver los requerimientos:  
[Requerimientos Técnicos](https://github.com/Dariella06/Rifters/blob/main/Requerimientos_tecnicos.md)

## Modelo E/R

En este apartado se muestra el Modelo E/R de nuestro proyecto, donde se puede ver la estructura de la base de datos. El diagrama representa la relación entre las distintas entidades involucradas, así como sus atributos y las conexiones lógicas que existen entre ellas.

![Modelo E/R](imagenes/image.png)

## Diagramas de Arquitectura Cliente / Servidor

Aquí se presentan diagramas que describen la arquitectura del sistema desde dos perspectivas: cliente y servidor. Estos diagramas muestran los principales componentes y el flujo de información entre ellos, facilitando la comprensión de cómo se conectan ambos lados del juego.

### Arquitectura del Cliente

El siguiente diagrama muestra cómo organizamos la lógica de los dos clientes, desde la interfaz de usuario hasta la gestión de peticiones al servidor.

[Ver archivo Mermaid del Cliente](Diagramas/Cliente.mermaid)

<img src="imagenes/cliente.png" alt="Diagrama del cliente" width="850" height="430"/>

### Arquitectura del Servidor

El siguiente diagrama muestra la estructura interna del servidor, incluida la API, la lógica empresarial y el acceso a la base de datos.

[Ver archivo Mermaid del Servidor](Diagramas/Servidor.mermaid)

<img src="imagenes/server.png" alt="Diagrama del servidor" width="850" height="370"/>

## Descripción de los Endpoints del WebService

En nuestro proyecto, los endpoints nos permiten registrarnos y acceder al juego mediante `/register` y `/login`, obteniendo un token para utilizar el resto de funcionalidades. Consultamos las cartas disponibles con `/cards` y gestionamos nuestros mazos con `/decks`: podemos verlos, crearlos, editar su contenido o eliminarlos. Para jugar, usamos `/matches` para ver, crear o unirnos a partidas. Durante una partida, utilizamos `/matches/current` para ver el estado, `/matches/action` para jugar cartas o pasar turno, y `/matches/<id>/surrender` si decidimos rendirnos.

### Host

`http://127.0.0.1:5000`

| Descripción                  | End-point                          | Método | Tipo de petición     | Parámetros                                                                                   |
|-----------------------------|------------------------------------|--------|----------------------|----------------------------------------------------------------------------------------------|
| Registrar usuario           | `/register`                        | POST   | `application/json`   | `username` (string), `password` (string), `email` (string)                                   |
| Iniciar sesión              | `/login`                           | POST   | `application/json`   | `username` (string), `password` (string)                                                     |
| Consultar cartas            | `/cards`                           | GET    | Token en header      | Token JWT en header `Authorization: Bearer <token>`                                         |
| Consultar mazos             | `/decks`                           | GET    | Token en header      | Token JWT                                                                                    |
| Crear mazo                  | `/decks`                           | POST   | `application/json`   | `name` (string), Token JWT                                                                   |
| Eliminar mazo               | `/decks/<deck_id>`                 | DELETE | Token en header      | Token JWT                                                                                    |
| Añadir carta a mazo         | `/decks/<deck_id>/cards`           | POST   | `application/json`   | `card_id` (int), `quantity` (int, opcional), Token JWT                                       |
| Ver partidas                | `/matches`                         | GET    | Token en header      | Token JWT                                                                                    |
| Crear partida               | `/matches`                         | POST   | `application/json`   | `deck_id` (int), Token JWT                                                                   |
| Unirse a partida            | `/matches/<match_id>/join`         | POST   | `application/json`   | `deck_id` (int), Token JWT                                                                   |
| Estado partida actual       | `/matches/current`                 | GET    | Token en header      | Token JWT                                                                                    |
| Realizar acción en partida  | `/matches/action`                  | POST   | `application/json`   | `action` (string: "play_card" o "end_turn"), `card_id` (int, si action es "play_card"), Token JWT |
| Rendirse en partida         | `/matches/<match_id>/surrender`    | POST   | Token en header      | Token JWT                                                                                    |

## Ejemplos de Respuestas

### `/register`

**201 Created**
```json
{
  "message": "Usuario registrado exitosamente",
  "user_id": 1
}
```

**400 Bad Request**

```json
{
  "error": "Todos los campos son requeridos"
}
```

### `/login`
**200 OK**

```json
{
  "token": "<jwt_token>",
  "user_id": 1,
  "username": "usuario",
  "message": "Sesión iniciada exitosamente"
}
```

**401 Unauthorized**

```json
{
  "error": "Credenciales incorrectas"
}
```

## Diagrama de Clases del Backend

La siguiente imagen muestra cómo está configurado el servidor del juego de cartas. Se utiliza un servidor web encargado de gestionar múltiples funciones, como el registro de usuarios, la administración de cartas y mazos, y la coordinación de las partidas.

Para el correcto funcionamiento del sistema, se han definido varias clases DAO (Data Access Object) encargadas de interactuar con la base de datos. Estas clases almacenan información relacionada con los usuarios, las cartas, los mazos y las partidas. Cada DAO está asociada a un módulo específico (Usuario, Carta, Baraja, Partida), lo cual permite separar la lógica de negocio de la lógica de acceso a datos.

[Ver archivo del Diagrama del Backend](Diagramas/DiagramaBackend.mermaid)


## Diagrama de Secuencia del Login

El siguiente diagrama ilustra el flujo de autenticación en el juego. El proceso inicia en el menú principal, donde el usuario puede registrarse o iniciar sesión. Una vez autenticado, se accede al menú principal desde el cual se puede gestionar mazos o participar en partidas. Al finalizar la sesión, el usuario puede volver al menú de inicio.

[Ver archivo de Mermaid del Diagrama de Secuencia de Login](Diagramas/Diagrama_Sequencia_login.mermaid)

<img src="imagenes/Secuencia_Login.png" alt="Diagrama del Login" width="850" height="470"/>


## Wireframes del Login y Pantallas Posteriores

En los wireframes diseñados para el sistema, el flujo comienza en una pantalla inicial que ofrece las opciones de iniciar sesión, registrarse o salir. Al ingresar correctamente, el usuario accede al menú principal, desde donde puede gestionar sus mazos, unirse o crear partidas, o cerrar sesión.

En la sección de gestión de mazos, el usuario puede crear nuevos mazos, editar su contenido o eliminarlos. En la sección de partidas, puede crear una nueva partida o unirse a una existente eligiendo el mazo con el que desea jugar.

Durante una partida, se recorren las distintas fases del juego: robar, jugar, atacar y finalizar turno. Al concluir la partida, se muestran los resultados y se ofrece la opción de solicitar una revancha o regresar al menú principal.

[Ver archivo de Wireframes de Login](Diagramas/Wireframes_Login.mermaid)

### Ejemplo del Login o Crear un nuevo usuario

