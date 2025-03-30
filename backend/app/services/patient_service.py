import requests
from app.models.patient import Patient
from app import db

class PatientService:
    @staticmethod
    def get_all(query=None):
        # Devuelve todos los pacientes, o filtra por nombre o enfermedad si se recibe `query`
        if query:
            return Patient.query.filter(
                (Patient.name.ilike(f"%{query}%")) | (Patient.disease.ilike(f"%{query}%"))
            ).all()
        return Patient.query.all()

    @staticmethod
    def create(data):
        # Validar contra API externa (Random User API)
        # Consulta la API externa para buscar pacientes similares
        external_users = requests.get("https://randomuser.me/api/?results=10").json()
        for user in external_users["results"]:
            if user["email"] == data["email"] or user["name"]["first"] in data["name"]:
                print("Paciente similar encontrado (Random User API)")
        
        # Crea y guarda un nuevo paciente en la base de datos
        patient = Patient(**data)
        db.session.add(patient)
        db.session.commit()
        return patient
