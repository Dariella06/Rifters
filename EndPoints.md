# WebService – Definición de EndPoints

**Host Base:**  
`http://192.168.144.199:10050`


## 1. Obtener datos de un usuario

| Descripción              | End-point              | Método | Tipo de petición   | Parámetros           |
|--------------------------|------------------------|--------|---------------------|-----------------------|
| Obtener datos de usuario | `/prototip1/getuser`   | GET    | `application/json`  | `username` (string)   |

**URL de prueba:**  
`http://192.168.144.199:10050/prototip1/getuser?username=usuari1`

### Respuestas

**200 OK – Usuario encontrado**
```json
{
  "email": "prova@gmail.com",
  "id": 1,
  "password": "12345",
  "username": "usuari1"
}
```

**400 Bad Request – Usuario no encontrado**
```json
{
  "description": "Usuari no trobat",
  "code": 1
}
```

**400 Bad Request – Falta parámetro**
```json
{
  "description": "Falta paràmetre Username",
  "code": 2
}
```

**400 Bad Request – Error de servidor**
```json
{
  "description": "Server Error",
  "code": 3
}
```


## 2. Registrar nuevo usuario

| Descripción        | End-point   | Método | Tipo de petición   | Parámetros                          |
|--------------------|-------------|--------|---------------------|--------------------------------------|
| Registrar usuario  | `/register` | POST   | `application/json`  | `username`, `password`, `email`     |

### Respuestas

**201 Created – Registro exitoso**
```json
{
  "message": "Usuario registrado exitosamente",
  "user_id": 5
}
```

**400 Bad Request – Campos faltantes**
```json
{
  "error": "Todos los campos son requeridos"
}
```

**400 Bad Request – Error al registrar**
```json
{
  "error": "Error al registrar usuario"
}
```

**500 Internal Server Error**
```json
{
  "error": "Error en el registro: [mensaje de error]"
}
```


## 3. Inicio de sesión

| Descripción       | End-point | Método | Tipo de petición   | Parámetros                    |
|-------------------|-----------|--------|---------------------|-------------------------------|
| Iniciar sesión    | `/login`  | POST   | `application/json`  | `username`, `password`        |

### Respuestas

**200 OK – Inicio exitoso**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user_id": 1,
  "username": "usuari1",
  "message": "Sesión iniciada exitosamente"
}
```

**400 Bad Request – Campos requeridos**
```json
{
  "error": "Usuario y contraseña requeridos"
}
```

**401 Unauthorized – Credenciales incorrectas**
```json
{
  "error": "Credenciales incorrectas"
}
```

**500 Internal Server Error**
```json
{
  "error": "Error en el servidor: [mensaje de error]"
}
```


## 4. Obtener cartas disponibles

| Descripción               | End-point  | Método | Tipo de petición   | Headers                          |
|---------------------------|------------|--------|---------------------|----------------------------------|
| Listar cartas disponibles | `/cards`   | GET    | `application/json`  | `Authorization: Bearer <token>` |

### Respuestas

**200 OK**
```json
[
  {
    "id": 1,
    "name": "Dragón",
    "type": "criatura",
    "cost": 5,
    "attack": 7,
    "defense": 6
  }
]
```

**401 Unauthorized – Token inválido**

**404 Not Found**
```json
{
  "message": "No hay cartas disponibles"
}
```

**500 Internal Server Error**
```json
{
  "error": "Error obteniendo cartas: [mensaje de error]"
}
```



## 5. Gestión de mazos

| Acción                | End-point                        | Método  | Tipo de petición   | Headers / Body                             |
|-----------------------|----------------------------------|---------|---------------------|---------------------------------------------|
| Obtener mazos         | `/decks`                         | GET     | `application/json`  | Header: `Authorization: Bearer <token>`     |
| Crear nuevo mazo      | `/decks`                         | POST    | `application/json`  | Body: `{ "name": "Mi nuevo mazo" }`         |
| Eliminar mazo         | `/decks/<deck_id>`               | DELETE  | `application/json`  | Header: `Authorization: Bearer <token>`     |
| Añadir carta a mazo   | `/decks/<deck_id>/cards`         | POST    | `application/json`  | Body: `{ "card_id": 5, "quantity": 2 }`     |



## 6. Gestión de partidas

| Acción                  | End-point                            | Método  | Tipo de petición   | Headers / Body                                |
|-------------------------|---------------------------------------|---------|---------------------|------------------------------------------------|
| Obtener partidas        | `/matches`                            | GET     | `application/json`  | Header: `Authorization: Bearer <token>`       |
| Crear nueva partida     | `/matches`                            | POST    | `application/json`  | Body: `{ "deck_id": 3 }`                      |
| Unirse a partida        | `/matches/<match_id>/join`            | POST    | `application/json`  | Body: `{ "deck_id": 3 }`                      |
| Obtener estado actual   | `/matches/current`                    | GET     | `application/json`  | Header: `Authorization: Bearer <token>`       |
| Realizar acción         | `/matches/action`                     | POST    | `application/json`  | Ver ejemplos abajo                            |

### Cuerpos de ejemplo para acciones

**Pasar turno**
```json
{
  "action": "end_turn"
}
```

**Jugar carta**
```json
{
  "action": "play_card",
  "card_id": 12
}
```
