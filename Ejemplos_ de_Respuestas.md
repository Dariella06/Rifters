
### `POST /register`
Registra un nuevo usuario

**Request Body:**
```json
{
  "username": "string",
  "password": "string",
  "email": "string"
}
```
Respuestas:

201 Created:

```json
{"message": "Usuario registrado exitosamente", "user_id": 1}
```
400 Bad Request:

```json
{"error": "Todos los campos son requeridos"}
```
500 Internal Server Error:

```json
{"error": "Error en el registro: [detalle]"}
```
POST /login
Inicia sesión y obtén token JWT

Request Body:

```json
{
  "username": "string",
  "password": "string"
}
```
Respuestas:

200 OK:

```json
{
  "token": "jwt.token.here",
  "user_id": 1,
  "username": "usuario",
  "message": "Sesión iniciada exitosamente"
}
```
400 Bad Request:

```json
{"error": "Usuario y contraseña requeridos"}
401 Unauthorized:
```
```json
{"error": "Credenciales incorrectas"}
```
Cartas
GET /cards 
Obtiene todas las cartas disponibles

Respuestas:

200 OK:

```json
[{"id": 1, "name": "Carta 1"}, ...]
```
404 Not Found:

```json
{"message": "No hay cartas disponibles"}
```
Mazos
GET /decks 
Obtiene todos los mazos del usuario

Respuestas:

200 OK:

```json
[{"id": 1, "name": "Mazo 1", "cards": []},]
```

404 Not Found:

```json
{"message": "No tienes mazos creados"}
```

POST /decks
Crea un nuevo mazo

Request Body:

```json
{"name": "Nombre del mazo"}
```

Respuestas:

201 Created:

```json
{"message": "Mazo creado exitosamente", "deck_id": 1}
```
400 Bad Request:

```json
{"error": "Nombre del mazo requerido"}
```

DELETE /decks/<int:deck_id> 
Elimina un mazo

Respuestas:

200 OK:

```json
{"message": "Mazo eliminado exitosamente"}
```
400 Bad Request:

```json
{"error": "Error al eliminar mazo"}
```
POST /decks/<int:deck_id>/cards 
Añade carta a un mazo

Request Body:

```json
{"card_id": 1, "quantity": 1}
```
Respuestas:

200 OK:

```json
{"message": "Carta añadida al mazo exitosamente"}
```

400 Bad Request:

```json
{"error": "ID de carta requerido"}
```

Partidas
GET /matches 
Obtiene partidas disponibles y propias

Respuestas:

200 OK:

```json
{
  "waiting_matches": [],
  "player_matches": []
}
```
POST /matches 
Crea una nueva partida

Request Body:

```json
{"deck_id": 1}
```
Respuestas:

201 Created:

```json
{"message": "Partida creada exitosamente", "match_id": 1}
```
400 Bad Request:

```json
{"error": "ID de mazo requerido"}
```
POST /matches/<int:match_id>/join 
Únete a una partida

Request Body:

```json
{"deck_id": 1}
```
Respuestas:

200 OK:

```json
{"message": "Te has unido a la partida exitosamente"}
```
400 Bad Request:

```json
{"error": "ID de mazo requerido"}
```
GET /matches/current
Obtiene partida actual

Respuestas:

200 OK:

```json
{"match_data": "..."}
```

404 Not Found:

```json
{"message": "No estás en ninguna partida activa"}
```
POST /matches/action
Realiza acción en partida

Request Body:

```json
{"action": "end_turn"}
```
o
```json
{"action": "play_card", "card_id": 1}
```
Respuestas:

200 OK:

```json
{"message": "Turno pasado exitosamente"}
```
400 Bad Request:

```json
{"error": "Acción requerida"}
```

POST /matches/<int:match_id>/surrender 
Ríndete en una partida

Respuestas:

200 OK:

```json
{"message": "Te has rendido correctamente", "match_id": 1, "status": "finished"}
```
403 Forbidden:

```json
{"error": "No estás en esta partida o no está activa"}
```
