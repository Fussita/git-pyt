
def test_existe_endpoint_obtener_usuario(client, json_headers, id_user_exists):
    response = client.get("/usuarios/"+str( id_user_exists ), headers=json_headers)
    assert response.status_code == 200
    assert response.json()["id"] == id_user_exists

def test_existe_endpoint_obtener_usuarios(client, json_headers, users_length):
    response = client.get("/usuarios", headers=json_headers)
    assert response.status_code == 200
    assert len(response.json()["user"]) == users_length


