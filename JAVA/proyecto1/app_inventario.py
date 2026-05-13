import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from typing import List, Dict, Optional, Union

# =============================================================================
# MODELO (Capa de Datos)
# =============================================================================

class Product:
    """Clase que representa un producto en el inventario."""
    def __init__(self, code: str, name: str, stock: int, price: float):
        self.code = code
        self.name = name
        self.stock = stock
        self.price = price

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convierte el objeto a un diccionario para facilitar el guardado en CSV."""
        return {
            "Codigo": self.code,
            "Nombre": self.name,
            "Stock": self.stock,
            "Precio": self.price
        }

class InventoryModel:
    """Maneja la persistencia de datos en el archivo CSV."""
    FILE_NAME = "inventario.csv"

    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.load_from_csv()

    def load_from_csv(self):
        """Carga los productos desde el archivo local CSV."""
        if not os.path.exists(self.FILE_NAME):
            return
        
        try:
            with open(self.FILE_NAME, mode='r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = Product(
                        code=row["Codigo"],
                        name=row["Nombre"],
                        stock=int(row["Stock"]),
                        price=float(row["Precio"])
                    )
                    self.products[product.code] = product
        except Exception as e:
            print(f"Error cargando datos: {e}")

    def save_to_csv(self):
        """Guarda el estado actual del inventario en el archivo CSV."""
        try:
            with open(self.FILE_NAME, mode='w', encoding='utf-8', newline='') as f:
                fieldnames = ["Codigo", "Nombre", "Stock", "Precio"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for p in self.products.values():
                    writer.writerow(p.to_dict())
        except Exception as e:
            print(f"Error guardando datos: {e}")

    def add_product(self, product: Product) -> bool:
        """Agrega un producto si el código no existe."""
        if product.code in self.products:
            return False
        self.products[product.code] = product
        self.save_to_csv()
        return True

    def update_product(self, product: Product) -> bool:
        """Actualiza un producto existente."""
        if product.code not in self.products:
            return False
        self.products[product.code] = product
        self.save_to_csv()
        return True

    def delete_product(self, code: str) -> bool:
        """Elimina un producto por su código."""
        if code in self.products:
            del self.products[code]
            self.save_to_csv()
            return True
        return False

    def get_all_products(self) -> List[Product]:
        """Retorna una lista de todos los productos."""
        return list(self.products.values())

# =============================================================================
# VISTA (Capa de Interfaz de Usuario)
# =============================================================================

class InventoryView(tk.Tk):
    """Clase principal de la interfaz gráfica."""
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Inventario - Refaccionaria")
        self.geometry("1000x600")
        self.configure(bg="#f0f2f5")
        
        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        """Configura los estilos personalizados para ttk."""
        style = ttk.Style()
        style.theme_use('clam')

        # Colores
        primary_color = "#2c3e50"    # Azul oscuro
        secondary_color = "#34495e"  # Azul grisáceo
        accent_color = "#3498db"     # Azul brillante
        bg_color = "#f0f2f5"         # Gris claro

        style.configure("Treeview", 
                        background="white", 
                        foreground="black", 
                        rowheight=25, 
                        fieldbackground="white")
        style.map("Treeview", background=[('selected', accent_color)])
        
        style.configure("Treeview.Heading", 
                        background=primary_color, 
                        foreground="white", 
                        font=('Segoe UI', 10, 'bold'))
        
        style.configure("TButton", 
                        padding=6, 
                        relief="flat", 
                        background=primary_color, 
                        foreground="white",
                        font=('Segoe UI', 9, 'bold'))
        style.map("TButton", background=[('active', secondary_color)])

        style.configure("TLabel", background=bg_color, font=('Segoe UI', 10))
        style.configure("Header.TLabel", font=('Segoe UI', 14, 'bold'), foreground=primary_color)

    def _build_ui(self):
        """Construye la disposición de los widgets en la ventana."""
        
        # --- Layout Principal ---
        # Panel Izquierdo: Formulario
        self.sidebar = tk.Frame(self, bg="#ffffff", width=300, padx=20, pady=20, relief="flat")
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        
        # Panel Derecho: Tabla y Búsqueda
        self.main_content = tk.Frame(self, bg="#f0f2f5", padx=20, pady=20)
        self.main_content.pack(side="right", expand=True, fill="both")

        # --- Widgets Sidebar (Formulario) ---
        ttk.Label(self.sidebar, text="Detalles del Producto", style="Header.TLabel", background="#ffffff").pack(pady=(0, 20))

        self.vars = {
            "code": tk.StringVar(),
            "name": tk.StringVar(),
            "stock": tk.StringVar(),
            "price": tk.StringVar()
        }

        fields = [
            ("Código de Pieza:", "code"),
            ("Nombre:", "name"),
            ("Stock (Cantidad):", "stock"),
            ("Precio Unitario ($):", "price")
        ]

        for label_text, var_name in fields:
            ttk.Label(self.sidebar, text=label_text, background="#ffffff").pack(anchor="w", pady=(10, 0))
            entry = ttk.Entry(self.sidebar, textvariable=self.vars[var_name], font=('Segoe UI', 10))
            entry.pack(fill="x", pady=5)

        # Botones de Acción en Sidebar
        self.btn_add = ttk.Button(self.sidebar, text="Añadir Producto")
        self.btn_add.pack(fill="x", pady=(20, 5))
        
        self.btn_update = ttk.Button(self.sidebar, text="Actualizar Seleccionado")
        self.btn_update.pack(fill="x", pady=5)
        
        self.btn_clear = ttk.Button(self.sidebar, text="Limpiar Formulario")
        self.btn_clear.pack(fill="x", pady=5)
        
        self.btn_delete = ttk.Button(self.sidebar, text="Eliminar Producto", cursor="hand2")
        self.btn_delete.pack(fill="x", pady=(20, 0))

        # --- Widgets Main Content (Búsqueda y Tabla) ---
        search_frame = tk.Frame(self.main_content, bg="#f0f2f5")
        search_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(search_frame, text="Buscar:").pack(side="left", padx=(0, 10))
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=40)
        self.search_entry.pack(side="left")

        # Tabla (Treeview)
        table_frame = tk.Frame(self.main_content)
        table_frame.pack(expand=True, fill="both")

        columns = ("code", "name", "stock", "price")
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        self.tree.heading("code", text="CÓDIGO", command=lambda: self._sort_column("code", False))
        self.tree.heading("name", text="NOMBRE", command=lambda: self._sort_column("name", False))
        self.tree.heading("stock", text="STOCK", command=lambda: self._sort_column("stock", False))
        self.tree.heading("price", text="PRECIO", command=lambda: self._sort_column("price", False))

        self.tree.column("code", width=100, anchor="center")
        self.tree.column("name", width=300)
        self.tree.column("stock", width=80, anchor="center")
        self.tree.column("price", width=100, anchor="e")

        # Scrollbars
        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscroll.set)
        
        self.tree.pack(side="left", expand=True, fill="both")
        yscroll.pack(side="right", fill="y")

    def _sort_column(self, col, reverse):
        """Permite ordenar las columnas al hacer clic."""
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        
        # Intentar ordenar numéricamente si es posible
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        self.tree.heading(col, command=lambda: self._sort_column(col, not reverse))

    def get_form_data(self) -> Dict[str, str]:
        """Obtiene los datos escritos en el formulario."""
        return {k: v.get().strip() for k, v in self.vars.items()}

    def clear_form(self):
        """Limpia todos los campos del formulario."""
        for var in self.vars.values():
            var.set("")

    def set_form_data(self, data: Dict[str, Union[str, int, float]]):
        """Rellena el formulario con datos específicos."""
        self.vars["code"].set(data["Codigo"])
        self.vars["name"].set(data["Nombre"])
        self.vars["stock"].set(str(data["Stock"]))
        self.vars["price"].set(str(data["Precio"]))

# =============================================================================
# CONTROLADOR (Capa de Lógica de Negocio)
# =============================================================================

class InventoryController:
    """Orquestador entre el Modelo y la Vista."""
    def __init__(self, model: InventoryModel, view: InventoryView):
        self.model = model
        self.view = view
        
        self._bind_events()
        self.refresh_table()

    def _bind_events(self):
        """Enlaza los botones y eventos de la vista con las funciones del controlador."""
        self.view.btn_add.config(command=self.add_product)
        self.view.btn_update.config(command=self.update_product)
        self.view.btn_delete.config(command=self.delete_product)
        self.view.btn_clear.config(command=self.view.clear_form)
        self.view.search_var.trace_add("write", lambda *args: self.refresh_table())
        
        # Selección en tabla
        self.tree = self.view.tree
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def validate_inputs(self, data: Dict[str, str]) -> Optional[Product]:
        """Valida que los datos ingresados sean correctos."""
        if not data["code"] or not data["name"]:
            messagebox.showerror("Error", "El Código y el Nombre son obligatorios.")
            return None
        
        try:
            stock = int(data["stock"])
            if stock < 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El Stock debe ser un número entero positivo.")
            return None

        try:
            price = float(data["price"])
            if price < 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El Precio debe ser un número decimal positivo.")
            return None

        return Product(data["code"], data["name"], stock, price)

    def refresh_table(self):
        """Actualiza los datos mostrados en la tabla, aplicando filtros de búsqueda."""
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        search_query = self.view.search_var.get().lower()
        
        products = self.model.get_all_products()
        for p in products:
            if search_query in p.code.lower() or search_query in p.name.lower():
                self.tree.insert("", "end", values=(p.code, p.name, p.stock, f"{p.price:.2f}"))

    def add_product(self):
        """Lógica para añadir un nuevo producto."""
        data = self.view.get_form_data()
        product = self.validate_inputs(data)
        
        if product:
            if self.model.add_product(product):
                messagebox.showinfo("Éxito", "Producto registrado correctamente.")
                self.view.clear_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", f"El código '{product.code}' ya existe.")

    def update_product(self):
        """Lógica para actualizar un producto seleccionado."""
        data = self.view.get_form_data()
        product = self.validate_inputs(data)
        
        if product:
            if self.model.update_product(product):
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                self.refresh_table()
            else:
                messagebox.showerror("Error", "No se pudo actualizar. Asegúrate de que el código exista.")

    def delete_product(self):
        """Lógica para eliminar un producto con confirmación."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Atención", "Por favor, selecciona un producto de la tabla.")
            return
        
        code = self.tree.item(selected_item)["values"][0]
        
        confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar el producto con código {code}?")
        if confirm:
            if self.model.delete_product(str(code)):
                messagebox.showinfo("Eliminado", "Producto eliminado con éxito.")
                self.view.clear_form()
                self.refresh_table()

    def on_tree_select(self, event):
        """Al seleccionar un item en la tabla, carga sus datos en el formulario."""
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            # Convertir valores de vuelta para el form
            data = {
                "Codigo": values[0],
                "Nombre": values[1],
                "Stock": values[2],
                "Precio": values[3]
            }
            self.view.set_form_data(data)

# =============================================================================
# EJECUCIÓN DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Inicializar componentes
    app_model = InventoryModel()
    app_view = InventoryView()
    app_controller = InventoryController(app_model, app_view)
    
    # Iniciar el bucle de eventos de la interfaz
    app_view.mainloop()
