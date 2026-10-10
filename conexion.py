import pyodbc

def conectar_base_datos():
    try:
        # Configuración de la conexión para SQL Server usando autenticación de Windows
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=localhost;'                  # Cambia 'localhost' por el nombre de tu servidor si es distinto
            'DATABASE=SistemaInventarioDB;'
            'Trusted_Connection=yes;'
        )
        print("¡Conexión exitosa a la base de datos de inventario!")
        return conexion
    except Exception as error:
        print("Error al conectar a la base de datos:", error)
        return None

if __name__ == "__main__":
    # Prueba rápida de conexión al ejecutar el archivo
    conexion = conectar_base_datos()
    if conexion:
        conexion.close()
        print("Conexión cerrada correctamente.")
