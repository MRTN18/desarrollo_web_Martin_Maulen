from db import engine, Base

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Se ha creado correctamente la base de datos")