from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- Modelos ---

class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)

class Comuna(Base):
    __tablename__ = "comuna"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    id_region = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")

class Actividad(Base):
    __tablename__ = "actividad"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime, nullable=True)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad")
    contactos = relationship("ContactarPor", back_populates="actividad")
    temas = relationship("ActividadTema", back_populates="actividad")

class Foto(Base):
    __tablename__ = "foto"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="fotos")


class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="contactos")


class ActividadTema(Base):
    __tablename__ = "actividad_tema"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tema = Column(Enum('música', 'deporte', 'ciencias', 'religión', 'política', 'tecnología', 'juegos', 'baile', 'comida', 'otro'), nullable=False)
    glosa_otro = Column(String(15), nullable=True)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)

    actividad = relationship("Actividad", back_populates="temas")

