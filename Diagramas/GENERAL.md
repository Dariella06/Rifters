sequenceDiagram
    participant ClientView as "Client View"
    participant ClientDAO as "Client DAO"
    participant ServerWebservice as "Server Webservice"
    participant ServerDAO as "Server DAO"

    ClientView->>ClientView: Input username and password
    ClientView->>ClientDAO: Send credentials (requests.post)
    ClientDAO->>ServerWebservice: HTTP POST /login (JSON)
    ServerWebservice->>ServerDAO: getUserByUsernameAndPassword()
    ServerDAO-->>ServerWebservice: Return user data (if exists)
    ServerWebservice-->>ClientDAO: HTTP Response (JSON: 200 OK / 401 Unauthorized)
    ClientDAO->>ClientView: Return processed data (token / user data)
    ClientView->>ClientView: Display user info (main menu)
