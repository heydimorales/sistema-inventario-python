from conexion import conectar_base_datos

def listar_productos():
    print("\n--- Listado de Productos en Inventario ---")
    conexion = conectar_base_datos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, nombre, descripcion, precio, stock FROM Productos")
            
            # Obtener todos los registros de la tabla
            productos = cursor.fetchall()
            
            if not productos:
                print("No hay productos registrados en este momento.")
            else:
                print(f"{'ID':<5} | {'Nombre':<20} | {'Precio':<10} | {'Stock':<6}")
                print("-" * 50)
                for prod in productos:
                    print(f"{prod[0]:<5} | {prod[1]:<20} | ${prod[2]:<9.2f} | {prod[4]:<6}")
            
            cursor.close()
            conexion.close()
        except Exception as error:
            print("Error al consultar los productos:", error)

if __name__ == "__main__":
    listar_productos()
