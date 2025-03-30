from app import db

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    disease = db.Column(db.String(100), nullable=False)
    
    # Método auxiliar para convertir el modelo a un dict JSON-friendly
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "document": self.document,
            "email": self.email,
            "phone": self.phone,
            "disease": self.disease
        }
