import customtkinter as ctk
from tkinter import messagebox
from backend import UserBackend

# Configuración general de la apariencia
ctk.set_appearance_mode("dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class UserApp(ctk.CTk):
    """
    Clase para la interfaz gráfica de usuario.
    Implementa los principios de UX/UI solicitados.
    """
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Sistema de Registro de Usuarios")
        self.geometry("500x450")
        self.backend = UserBackend()

        # Centrar la ventana en la pantalla
        self.eval('tk::PlaceWindow . center')

        # Configuración del grid
        self.grid_columnconfigure(0, weight=1)
        
        # --- UI ELEMENTS ---
        
        # Título
        self.label_titulo = ctk.CTkLabel(
            self, 
            text="REGISTRO DE USUARIOS", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#1f6aa5"
        )
        self.label_titulo.grid(row=0, column=0, padx=20, pady=(30, 20))

        # Contenedor para los campos (Frame)
        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.grid(row=1, column=0, padx=40, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure(1, weight=1)

        # Campo: Nombre
        self.label_nombre = ctk.CTkLabel(self.form_frame, text="Nombre:", font=ctk.CTkFont(size=14))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.form_frame, placeholder_text="Ingrese nombre completo")
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Campo: Carrera
        self.label_carrera = ctk.CTkLabel(self.form_frame, text="Carrera:", font=ctk.CTkFont(size=14))
        self.label_carrera.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_carrera = ctk.CTkEntry(self.form_frame, placeholder_text="Ingrese carrera")
        self.entry_carrera.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Campo: Edad
        self.label_edad = ctk.CTkLabel(self.form_frame, text="Edad:", font=ctk.CTkFont(size=14))
        self.label_edad.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_edad = ctk.CTkEntry(self.form_frame, placeholder_text="Ingrese edad")
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # --- BOTONES ---
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, padx=40, pady=30)

        # Botón Registrar
        self.btn_registrar = ctk.CTkButton(
            self.button_frame, 
            text="Registrar", 
            command=self.accion_registrar,
            width=120,
            fg_color="#1f6aa5",
            hover_color="#144870"
        )
        self.btn_registrar.grid(row=0, column=0, padx=10)

        # Botón Borrar
        self.btn_borrar = ctk.CTkButton(
            self.button_frame, 
            text="Borrar", 
            command=self.accion_borrar,
            width=120,
            fg_color="#d32f2f",
            hover_color="#b71c1c"
        )
        self.btn_borrar.grid(row=0, column=1, padx=10)

    def accion_registrar(self):
        """Maneja la lógica del botón Registrar."""
        nombre = self.entry_nombre.get()
        carrera = self.entry_carrera.get()
        edad = self.entry_edad.get()

        exito, mensaje = self.backend.registrar_usuario(nombre, carrera, edad)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.accion_borrar() # Limpiar después de registrar
        else:
            messagebox.showwarning("Error de Validación", mensaje)

    def accion_borrar(self):
        """Maneja la lógica del botón Borrar (limpia campos)."""
        self.entry_nombre.delete(0, 'end')
        self.entry_carrera.delete(0, 'end')
        self.entry_edad.delete(0, 'end')
        self.entry_nombre.focus()

if __name__ == "__main__":
    app = UserApp()
    app.mainloop()
