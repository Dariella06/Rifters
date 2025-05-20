import requests
import json
import time

# Configuración
BASE_URL = "http://127.0.0.1:5000"
USUARIOS = [
    {"username": "Denis", "password": "1234"},
    {"username": "Dariella", "password": "4321"}
]

# Funciones auxiliares
def print_test(title):
    print(f"\n{'='*50}")
    print(f"TEST: {title}")
    print(f"{'='*50}")

def print_result(success, message=None, response=None):
    if success:
        print(f"[✓] ÉXITO: {message}")
    else:
        print(f"[X] FALLO: {message}")
        if response:
            print(f"Respuesta del servidor: {response.status_code}")
            try:
                print(f"Contenido: {response.json()}")
            except:
                print(f"Contenido: {response.text}")

def get_auth_header(token):
    return {'Authorization': f'Bearer {token}'}

# Funciones de prueba
def test_registro():
    print_test("Pruebas de Registro de Usuarios")
    
    # Caso 1: Registro exitoso
    data = {"username": "test_user", "password": "test123", "email": "test@example.com"}
    response = requests.post(f"{BASE_URL}/register", json=data)
    success = response.status_code == 201
    print_result(success, "Registro de nuevo usuario", response)
    
    # Caso 2: Registro con datos faltantes
    data = {"username": "test_user2", "password": "test123"}
    response = requests.post(f"{BASE_URL}/register", json=data)
    success = response.status_code == 400
    print_result(success, "Registro con datos faltantes (debe fallar)", response)
    
    # Caso 3: Registro con username existente
    data = {"username": "Denis", "password": "test123", "email": "denis@example.com"}
    response = requests.post(f"{BASE_URL}/register", json=data)
    success = response.status_code != 201
    print_result(success, "Registro con username existente (debe fallar)", response)

def test_login():
    print_test("Pruebas de Inicio de Sesión")
    
    # Caso 1: Login exitoso
    for user in USUARIOS:
        response = requests.post(f"{BASE_URL}/login", json=user)
        success = response.status_code == 200
        print_result(success, f"Inicio de sesión exitoso para {user['username']}", response)
        if success:
            USUARIOS[USUARIOS.index(user)]['token'] = response.json()['token']
    
    # Caso 2: Login con usuario inexistente
    data = {"username": "no_existo", "password": "1234"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    success = response.status_code == 401
    print_result(success, "Inicio de sesión con usuario inexistente (debe fallar)", response)
    
    # Caso 3: Login con contraseña incorrecta
    data = {"username": "Denis", "password": "wrongpass"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    success = response.status_code == 401
    print_result(success, "Inicio de sesión con contraseña incorrecta (debe fallar)", response)

def test_cartas():
    print_test("Pruebas de Gestión de Cartas")
    
    # Necesitamos un token válido
    if 'token' not in USUARIOS[0]:
        print("[!] No hay token disponible, omitiendo pruebas de cartas")
        return
    
    headers = get_auth_header(USUARIOS[0]['token'])
    
    # Caso 1: Obtener cartas disponibles
    response = requests.get(f"{BASE_URL}/cards", headers=headers)
    success = response.status_code == 200 and len(response.json()) > 0
    print_result(success, "Obtener cartas disponibles", response)
    
    # Guardar algunas cartas para pruebas posteriores
    cartas = response.json()
    if cartas:
        USUARIOS[0]['carta_id'] = cartas[0]['id']

def test_mazos():
    print_test("Pruebas de Gestión de Mazos")
    
    # Necesitamos un token válido
    if 'token' not in USUARIOS[0]:
        print("[!] No hay token disponible, omitiendo pruebas de mazos")
        return
    
    headers = get_auth_header(USUARIOS[0]['token'])
    
    # Caso 1: Crear mazo
    data = {"name": "Mazo de prueba"}
    response = requests.post(f"{BASE_URL}/decks", headers=headers, json=data)
    success = response.status_code == 201
    print_result(success, "Crear nuevo mazo", response)
    
    if success:
        deck_id = response.json()['deck_id']
        USUARIOS[0]['deck_id'] = deck_id
        
        # Caso 2: Añadir carta al mazo
        if 'carta_id' in USUARIOS[0]:
            data = {"card_id": USUARIOS[0]['carta_id'], "quantity": 1}
            response = requests.post(f"{BASE_URL}/decks/{deck_id}/cards", headers=headers, json=data)
            success = response.status_code == 200
            print_result(success, "Añadir carta al mazo", response)
        
        # Caso 3: Obtener mazos del usuario
        response = requests.get(f"{BASE_URL}/decks", headers=headers)
        success = response.status_code == 200 and len(response.json()) > 0
        print_result(success, "Obtener mazos del usuario", response)
        
        # Caso 4: Eliminar mazo
        confirm = input("¿Desea probar la eliminación de mazo? (s/n): ").strip().lower()
        if confirm == 's':
            response = requests.delete(f"{BASE_URL}/decks/{deck_id}", headers=headers)
            success = response.status_code == 200
            print_result(success, "Eliminar mazo", response)
            if success:
                del USUARIOS[0]['deck_id']

def test_partidas():
    print_test("Pruebas de Gestión de Partidas")
    
    # Necesitamos tokens y mazos válidos
    if 'token' not in USUARIOS[0] or 'token' not in USUARIOS[1]:
        print("[!] No hay tokens disponibles para ambos usuarios, omitiendo pruebas de partidas")
        return
    
    # Crear mazos si no existen
    headers_denis = get_auth_header(USUARIOS[0]['token'])
    headers_dariella = get_auth_header(USUARIOS[1]['token'])
    
    if 'deck_id' not in USUARIOS[0]:
        data = {"name": "Mazo de Denis"}
        response = requests.post(f"{BASE_URL}/decks", headers=headers_denis, json=data)
        if response.status_code == 201:
            USUARIOS[0]['deck_id'] = response.json()['deck_id']
            # Añadir carta si existe
            if 'carta_id' in USUARIOS[0]:
                data = {"card_id": USUARIOS[0]['carta_id'], "quantity": 1}
                requests.post(f"{BASE_URL}/decks/{USUARIOS[0]['deck_id']}/cards", headers=headers_denis, json=data)
    
    if 'deck_id' not in USUARIOS[1]:
        data = {"name": "Mazo de Dariella"}
        response = requests.post(f"{BASE_URL}/decks", headers=headers_dariella, json=data)
        if response.status_code == 201:
            USUARIOS[1]['deck_id'] = response.json()['deck_id']
            # Añadir carta si existe
            if 'carta_id' in USUARIOS[0]:
                data = {"card_id": USUARIOS[0]['carta_id'], "quantity": 1}
                requests.post(f"{BASE_URL}/decks/{USUARIOS[1]['deck_id']}/cards", headers=headers_dariella, json=data)
    
    if 'deck_id' not in USUARIOS[0] or 'deck_id' not in USUARIOS[1]:
        print("[!] No se pudieron crear mazos para ambos usuarios, omitiendo pruebas de partidas")
        return
    
    # Caso 1: Crear partida (Denis)
    data = {"deck_id": USUARIOS[0]['deck_id']}
    response = requests.post(f"{BASE_URL}/matches", headers=headers_denis, json=data)
    success = response.status_code == 201
    print_result(success, "Denis crea una nueva partida", response)
    
    if not success:
        return
    
    match_id = response.json()['match_id']
    
    # Caso 2: Obtener partidas disponibles
    response = requests.get(f"{BASE_URL}/matches", headers=headers_dariella)
    success = response.status_code == 200 and len(response.json()['waiting_matches']) > 0
    print_result(success, "Dariella ve las partidas disponibles", response)
    
    # Caso 3: Unirse a partida (Dariella)
    data = {"deck_id": USUARIOS[1]['deck_id']}
    response = requests.post(f"{BASE_URL}/matches/{match_id}/join", headers=headers_dariella, json=data)
    success = response.status_code == 200
    print_result(success, "Dariella se une a la partida de Denis", response)
    
    if not success:
        return
    
    # Caso 4: Obtener estado de la partida
    print("\nVerificando estado de la partida para ambos jugadores...")
    
    # Estado para Denis
    response = requests.get(f"{BASE_URL}/matches/current", headers=headers_denis)
    success = response.status_code == 200
    print_result(success, "Denis obtiene el estado de la partida", response)
    if success:
        print(f"Estado de la partida para Denis:\n{json.dumps(response.json(), indent=2)}")
    
    # Estado para Dariella
    response = requests.get(f"{BASE_URL}/matches/current", headers=headers_dariella)
    success = response.status_code == 200
    print_result(success, "Dariella obtiene el estado de la partida", response)
    if success:
        print(f"Estado de la partida para Dariella:\n{json.dumps(response.json(), indent=2)}")
    
    # Caso 5: Realizar acciones en la partida
    print("\nProbando acciones en la partida...")
    
    # Verificar quién tiene el turno
    response = requests.get(f"{BASE_URL}/matches/current", headers=headers_denis)
    if response.status_code == 200:
        current_player = response.json()['match_info']['current_player']
        player_with_turn = "Denis" if current_player == USUARIOS[0]['user_id'] else "Dariella"
        print(f"Turno actual: {player_with_turn}")
        
        # Pasar turno
        if current_player == USUARIOS[0]['user_id']:  # Denis
            data = {"action": "end_turn"}
            response = requests.post(f"{BASE_URL}/matches/action", headers=headers_denis, json=data)
            success = response.status_code == 200
            print_result(success, "Denis pasa el turno", response)
        else:  # Dariella
            data = {"action": "end_turn"}
            response = requests.post(f"{BASE_URL}/matches/action", headers=headers_dariella, json=data)
            success = response.status_code == 200
            print_result(success, "Dariella pasa el turno", response)
    
    # Caso 6: Rendirse en la partida
    confirm = input("\n¿Desea probar la rendición en la partida? (s/n): ").strip().lower()
    if confirm == 's':
        # Dariella se rinde
        response = requests.post(f"{BASE_URL}/matches/{match_id}/surrender", headers=headers_dariella, json={})
        success = response.status_code == 200
        print_result(success, "Dariella se rinde en la partida", response)

def main():
    print("INICIANDO PRUEBAS AUTOMATIZADAS DEL JUEGO DE CARTAS")
    print(f"URL base: {BASE_URL}")
    
    # Ejecutar pruebas en orden
    test_registro()
    test_login()
    test_cartas()
    test_mazos()
    test_partidas()
    
    print("\nPRUEBAS COMPLETADAS")

if __name__ == "__main__":
    main()
