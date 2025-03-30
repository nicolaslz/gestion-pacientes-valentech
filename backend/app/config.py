import os

# URL de conexión a la base de datos PostgreSQL
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/valentechdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False