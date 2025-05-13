## Definición de EndPoints del WebService
En este apartado, detallamos los endpoints del servicio web basado en el código proporcionado:

**Host Base**
http://192.168.144.199:10050

## Endpoints
1. Obtener datos de un usuario
Descripción: Obtiene información de un usuario específico

Endpoint: /prototip1/getuser

Método: GET

Tipo de petición: application/json

Parámetros:

username (string): Nombre de usuario a buscar

Respuestas posibles:
Usuario encontrado (200 OK):

```json
{
  "email": "prova@gmail.com",
  "id": 1,
  "password": "12345",
  "username": "usuari1"
}
```

Errores:

400 Bad Request:

Usuario no encontrado:

```json
{
  "description": "Usuari no trobat",
  "code": 1
}
```

Falta parámetro username:

```json
{
  "description": "Falta paràmetre Username",
  "code": 2
}
```

Error del servidor:

```json
{
  "description": "Server Error",
  "code": 3
}
```

URL de prueba:
http://192.168.144.199:10050/prototip1/getuser?username=usuari1
2. Registro de usuario
Descripción: Crea un nuevo usuario en el sistema

Endpoint: /register

Método: POST

Tipo de petición: application/json

Parámetros:

username (string): Nombre de usuario

password (string): Contraseña

email (string): Correo electrónico

Respuestas posibles:
Registro exitoso (201 Created):

```json
{
  "message": "Usuario registrado exitosamente",
  "user_id": 5
}
```
Errores:

400 Bad Request:

Campos faltantes:

```json
{
  "error": "Todos los campos son requeridos"
}
```

Error al registrar:

```json
{
  "error": "Error al registrar usuario"
}
```

500 Internal Server Error:

```json
{
  "error": "Error en el registro: [mensaje de error]"
}
```

3. Inicio de sesión
Descripción: Autentica a un usuario y devuelve un token JWT

Endpoint: /login

Método: POST

Tipo de petición: application/json

Parámetros:

username (string): Nombre de usuario

password (string): Contraseña

Respuestas posibles:
Login exitoso (200 OK):

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user_id": 1,
  "username": "usuari1",
  "message": "Sesión iniciada exitosamente"
}
```

Errores:

400 Bad Request:

Campos faltantes:

```json
{
  "error": "Usuario y contraseña requeridos"
}
```

401 Unauthorized:

Credenciales incorrectas:

```json
{
  "error": "Credenciales incorrectas"
}
```

500 Internal Server Error:

```json
{
  "error": "Error en el servidor: [mensaje de error]"
}
```

4. Obtener cartas disponibles
Descripción: Lista todas las cartas disponibles en el juego

Endpoint: /cards

Método: GET

Tipo de petición: application/json

Headers:

Authorization: Bearer <token>

Respuestas posibles:
Éxito (200 OK):

```json
[
  {
    "id": 1,
    "name": "Dragón",
    "type": "criatura",
    "cost": 5,
    "attack": 7,
    "defense": 6
  },
  ...
]
```

Errores:

401 Unauthorized: Token inválido o faltante

404 Not Found:

```json
{
  "message": "No hay cartas disponibles"
}
```

500 Internal Server Error:

```json
{
  "error": "Error obteniendo cartas: [mensaje de error]"
}
```

5. Gestión de mazos
5.1 Obtener mazos del usuario
Endpoint: /decks

Método: GET

Headers:

Authorization: Bearer <token>

5.2 Crear nuevo mazo
Endpoint: /decks

Método: POST

Headers:

Authorization: Bearer <token>

Body:

```json
{
  "name": "Mi nuevo mazo"
}
```

5.3 Eliminar mazo
Endpoint: /decks/<int:deck_id>

Método: DELETE

Headers:

Authorization: Bearer <token>

5.4 Añadir carta a mazo
Endpoint: /decks/<int:deck_id>/cards

Método: POST

Headers:

Authorization: Bearer <token>

Body:

```json
{
  "card_id": 5,
  "quantity": 2
}
```

6. Gestión de partidas
6.1 Obtener partidas disponibles
Endpoint: /matches

Método: GET

Headers:

Authorization: Bearer <token>

6.2 Crear nueva partida
Endpoint: /matches

Método: POST

Headers:

Authorization: Bearer <token>

Body:

```json
{
  "deck_id": 3
}
```

6.3 Unirse a partida
Endpoint: /matches/<int:match_id>/join

Método: POST

Headers:

Authorization: Bearer <token>

Body:

```json
{
  "deck_id": 3
}
```

6.4 Obtener estado de partida actual
Endpoint: /matches/current

Método: GET

Headers:

Authorization: Bearer <token>

6.5 Realizar acción en partida
Endpoint: /matches/action

Método: POST

Headers:

Authorization: Bearer <token>

Body (ejemplos):

Pasar turno:

```json
{
  "action": "end_turn"
}
```

Jugar carta:

```json
{
  "action": "play_card",
  "card_id": 12
}
```
