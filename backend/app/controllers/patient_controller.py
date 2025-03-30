from flask import request, jsonify
from app.services.patient_service import PatientService

def get_patients():
    # Obtiene query param opcional (?q=texto)
    query = request.args.get("q")
    patients = PatientService.get_all(query)
    return jsonify([p.to_dict() for p in patients]), 200

def create_patient():
    data = request.json
    try:
        patient = PatientService.create(data)
        return jsonify(patient.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
