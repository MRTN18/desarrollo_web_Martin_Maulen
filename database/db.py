from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, create_engine
from sqlalchemy.sql import func
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

    comunas = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = "comuna"

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    actividades = relationship("Actividad", back_populates="comuna")
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

# --- Consultas ---

def get_regiones():
    session = SessionLocal()
    regiones = session.query(Region).all()
    session.close()
    return regiones

def get_actividades():
    session = SessionLocal()
    actividades = session.query(Actividad).all()
    session.close()
    return actividades

def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter(Comuna.id == id).first()
    session.close()
    return comuna

def get_actividad_by_id(id):
    session = SessionLocal()
    actividad = session.query(Actividad).filter(Actividad.id == id).first()
    session.close()
    return actividad

def get_actividades_by_date(start_date):
    session = SessionLocal()
    actividades = session.query(Actividad).filter(func.date(Actividad.dia_hora_inicio) == start_date.date()).all()
    session.close()
    return actividades

def get_actividades_by_month(month):
    session = SessionLocal()
    actividades = session.query(Actividad).filter(func.month(Actividad.dia_hora_inicio) == month).all()
    session.close()
    return actividades

def get_tema_by_actividad_id(id):
    session = SessionLocal()
    tema = session.query(ActividadTema).filter(ActividadTema.actividad_id == id).first()
    session.close()
    return tema

def get_fotos_by_actividad_id(id):
    session = SessionLocal()
    fotos = session.query(Foto).filter(Foto.actividad_id == id).all()
    session.close()
    return fotos

def get_redes_sociales_by_actividad_id(id):
    session = SessionLocal()
    redes_sociales = session.query(ContactarPor).filter(ContactarPor.actividad_id == id).all()
    session.close()
    return redes_sociales

def create_actividad(comuna, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion):
    session = SessionLocal()
    new_actividad = Actividad(
        comuna_id=comuna,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion
    )
    session.add(new_actividad)
    session.commit()
    session.close()

def create_foto(ruta_archivo, nombre_archivo, actividad_id):
    session = SessionLocal()
    new_foto = Foto(
        ruta_archivo=ruta_archivo,
        nombre_archivo=nombre_archivo,
        actividad_id=actividad_id
    )
    session.add(new_foto)
    session.commit()
    session.close()

def create_actividad_tema(tema, glosa_otro, actividad_id):
    session = SessionLocal()
    new_actividad_tema = ActividadTema(
        tema=tema,
        glosa_otro=glosa_otro,
        actividad_id=actividad_id
    )
    session.add(new_actividad_tema)
    session.commit()
    session.close()

def create_contactar_por(nombre, identificador, actividad_id):
    session = SessionLocal()
    new_contactar_por = ContactarPor(
        nombre=nombre,
        identificador=identificador,
        actividad_id=actividad_id
    )
    session.add(new_contactar_por)
    session.commit()
    session.close()