from sqlalchemy import create_engine, inspect

# Configura la conexión a tu base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/practica"

try:
    # Crear el motor de conexión
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)

    # Obtener la lista de tablas
    tables = inspector.get_table_names()
    print("Tablas en la base de datos:", tables)
except Exception as e:
    print("Error al conectar a la base de datos:", e)
