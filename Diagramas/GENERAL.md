sequenceDiagram
    participant ClientView as Client View
    participant ClientDAO as Client DAO User
    participant ServerWebservice as Servidor Webservice
    participant ServerDAO as Server DAO User

    ClientView->>ClientView: Input username (login)
    ClientView->>ClientDAO: Envia dades username (requests.post)
    ClientDAO->>ServerWebservice: Petición HTTP POST /login (JSON)
    ServerWebservice->>ServerDAO: getUserByUsernameAndPassword
    ServerDAO-->>ServerWebservice: User data if exists
    ServerWebservice-->>ClientDAO: Resposta HTTP Json (200/401)
    ClientDAO->>ClientView: Dades processades (token/user_data)
    ClientView->>ClientView: Show Info User (menu principal)
