import pytest
from unittest.mock import patch, MagicMock
from app import create_app

# Cliente de prueba de Flask
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

# Mock para el método get_all del servicio
@patch('app.controllers.patient_controller.PatientService.get_all')
def test_get_patients(mock_get_all, client):
    mock_get_all.return_value = [
        MagicMock(to_dict=lambda: {
            "id": 1,
            "name": "Juan Pérez",
            "document": "123456789",
            "email": "juan@mail.com",
            "phone": "3001234567",
            "disease": "Diabetes"
        })
    ]

    response = client.get('/api/patients')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data[0]["name"] == "Juan Pérez"

# Mock para el método create del servicio
@patch('app.controllers.patient_controller.PatientService.create')
def test_create_patient(mock_create, client):
    input_data = {
        "name": "Ana Gómez",
        "document": "987654321",
        "email": "ana@mail.com",
        "phone": "3017654321",
        "disease": "Asma"
    }

    # Simula lo que retornaría PatientService.create
    mock_create.return_value = MagicMock(to_dict=lambda: input_data)

    response = client.post('/api/patients', json=input_data)
    data = response.get_json()

    assert response.status_code == 201
    assert data["email"] == "ana@mail.com"
