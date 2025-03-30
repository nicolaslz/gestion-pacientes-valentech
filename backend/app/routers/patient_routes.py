from flask import Blueprint
from app.controllers.patient_controller import get_patients, create_patient

# Blueprint que agrupa las rutas relacionadas con pacientes
patient_bp = Blueprint('patients', __name__)

patient_bp.route('/', methods=['GET'])(get_patients)
patient_bp.route('/', methods=['POST'])(create_patient)