import os
import logging
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

# Configuración mediante variables de entorno (valores por defecto para phpMyAdmin/XAMPP)
# phpMyAdmin/XAMPP normalmente usa: user='root', password='', host='127.0.0.1', port=3306
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'hotel_db')

# Construir la URL de conexión de forma segura
_password_quoted = quote_plus(DB_PASSWORD)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{_password_quoted}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Crear una clase base para los modelos
Base = declarative_base()

# Crear una clase para manejar las sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Generador que proporciona una sesión de base de datos.

    Uso:
        from principal.conexion import get_db
        with next(get_db()) as db:  # o usar como generador en frameworks
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Crea las tablas definidas en los modelos si no existen.
    """
    logger.info('Inicializando la base de datos: %s', DATABASE_URL)
    Base.metadata.create_all(bind=engine)