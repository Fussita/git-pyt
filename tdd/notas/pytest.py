
from fastapi.testclient import TestClient
import pytest
from myapp.main import app 

# Uso de Assertions para Verificar Respuestas
def test_read_item():
    response = client.get('/items/42')
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "description": "Some Item"}

# client: Es un fixture que proporciona un cliente de prueba de FastAPI para simular solicitudes HTTP en tus pruebas.
@pytest.fixture
def client():
    """Fixture para proporcionar un cliente de prueba para las pruebas."""
    return TestClient(app)

@pytest.fixture(scope="module")
def database():
    yield some_database_connection
    cleanup_database()

@pytest.fixture
def item_with_database(database):
    """Fixture que depende de la base de datos."""
    item_id = create_item_in_database()
    return item_id

"""
    200 OK: La solicitud fue exitosa.
    201 Created: La solicitud ha tenido éxito y se ha creado un nuevo recurso.
    400 Bad Request: La solicitud no pudo ser procesada debido a un error del cliente.
    404 Not Found: El recurso solicitado no se ha encontrado.
    500 Internal Server Error: Indica un error interno en el servidor
"""