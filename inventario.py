from conexion import conectar_base_datos

def registrar_producto():
    print("\n--- Registro de Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una breve descripción: ")
    
    try:
        precio = float(input("Ingrese el precio unitario: "))
        stock = int(input("Ingrese la cantidad en stock: "))
    except ValueError:
        print("Error: El precio y el stock deben ser valores numéricos.")
        return

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Consulta SQL para insertar el producto
            sql = "INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (nombre, descripcion, precio, stock))
            
            # Confirmar los cambios en la base de datos
            conexion.commit()
            print("¡Producto registrado exitosamente en la base de datos!")
            
            cursor.close()
            conexion.close()
        except Exception as error:
            print("Error al registrar el producto:", error)

if __name__ == "__main__":
    registrar_producto()
