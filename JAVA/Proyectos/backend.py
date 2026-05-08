import pandas as pd

class UserBackend:
    """
    Clase encargada de la lógica de negocio y gestión de datos.
    Utiliza pandas para el almacenamiento temporal de los registros.
    """
    def __init__(self):
        # Inicializamos el DataFrame con las columnas necesarias
        self.columns = ["Nombre", "Carrera", "Edad"]
        self.df = pd.DataFrame(columns=self.columns)
        
    def registrar_usuario(self, nombre, carrera, edad):
        """
        Valida y añade un nuevo registro al DataFrame.
        """
        # Validación de campos vacíos
        if not nombre or not carrera or not edad:
            return False, "Todos los campos son obligatorios."
        
        try:
            # Validar que la edad sea un número
            edad_int = int(edad)
            if edad_int <= 0:
                return False, "La edad debe ser un número positivo."
        except ValueError:
            return False, "La edad debe ser un valor numérico."

        # Crear nueva fila
        nueva_fila = pd.DataFrame([[nombre, carrera, edad_int]], columns=self.columns)
        
        # Concatenar al DataFrame existente
        self.df = pd.concat([self.df, nueva_fila], ignore_index=True)
        
        # Opcional: Imprimir en consola para verificar
        print("\n--- Registro Actualizado ---")
        print(self.df)
        
        return True, f"Usuario '{nombre}' registrado con éxito."

    def obtener_datos(self):
        """Retorna el DataFrame actual."""
        return self.df
