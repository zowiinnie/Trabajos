package com.veterinaria.controlador;

import com.veterinaria.dao.PacienteDAO;
import com.veterinaria.modelo.Paciente;
import com.veterinaria.vista.VentanaPrincipal;
import javax.swing.*;
import java.util.List;

/**
 * Controlador que orquestra la interacción entre el Modelo y la Vista.
 * Implementa validaciones de negocio y manejo de excepciones.
 * 
 * @author Arquitecto Java Senior
 */
public class PacienteController {
    private final VentanaPrincipal vista;
    private final PacienteDAO dao;

    /**
     * Constructor que vincula la vista y el DAO.
     * @param vista Instancia de la interfaz gráfica.
     * @param dao Instancia del acceso a datos.
     */
    public PacienteController(VentanaPrincipal vista, PacienteDAO dao) {
        this.vista = vista;
        this.dao = dao;
        
        // Inicializar eventos
        this.vista.btnGuardar.addActionListener(e -> guardarPaciente());
        this.vista.btnEliminar.addActionListener(e -> eliminarPaciente());
        this.vista.btnLimpiar.addActionListener(e -> vista.limpiarCampos());
        
        actualizarTabla();
    }

    /**
     * Lógica para guardar un paciente. 
     * Incluye validación de campos obligatorios y formato numérico.
     */
    private void guardarPaciente() {
        try {
            // Validar campos vacíos
            if (vista.txtId.getText().isEmpty() || vista.txtNombre.getText().isEmpty() || 
                vista.txtDueno.getText().isEmpty()) {
                throw new Exception("Los campos ID, Nombre y Dueño son obligatorios.");
            }

            // Validar edad
            int edad;
            try {
                edad = Integer.parseInt(vista.txtEdad.getText());
                if (edad < 0) throw new NumberFormatException();
            } catch (NumberFormatException e) {
                throw new Exception("La edad debe ser un número entero positivo.");
            }

            // Crear modelo
            Paciente p = new Paciente(
                vista.txtId.getText(),
                vista.txtNombre.getText(),
                vista.txtEspecie.getText(),
                vista.txtRaza.getText(),
                edad,
                vista.txtDueno.getText(),
                vista.txtTelefono.getText(),
                vista.txtSintomas.getText()
            );

            // Guardar via DAO
            dao.guardar(p);
            
            JOptionPane.showMessageDialog(vista, "Paciente registrado con éxito.", "Éxito", JOptionPane.INFORMATION_MESSAGE);
            vista.limpiarCampos();
            actualizarTabla();

        } catch (Exception ex) {
            JOptionPane.showMessageDialog(vista, ex.getMessage(), "Error de Validación", JOptionPane.ERROR_MESSAGE);
        }
    }

    /**
     * Lógica para eliminar un paciente seleccionado en la tabla.
     */
    private void eliminarPaciente() {
        int fila = vista.tablaPacientes.getSelectedRow();
        if (fila == -1) {
            JOptionPane.showMessageDialog(vista, "Seleccione un paciente de la tabla para eliminar.", "Aviso", JOptionPane.WARNING_MESSAGE);
            return;
        }

        int confirm = JOptionPane.showConfirmDialog(vista, "¿Está seguro de eliminar este registro?", "Confirmar", JOptionPane.YES_NO_OPTION);
        if (confirm == JOptionPane.YES_OPTION) {
            dao.eliminar(fila);
            actualizarTabla();
            JOptionPane.showMessageDialog(vista, "Registro eliminado.");
        }
    }

    /**
     * Sincroniza la tabla de la vista con los datos del DAO.
     */
    private void actualizarTabla() {
        vista.modeloTabla.setRowCount(0);
        List<Paciente> pacientes = dao.obtenerTodos();
        for (Paciente p : pacientes) {
            vista.modeloTabla.addRow(new Object[]{
                p.getId(), p.getNombre(), p.getEspecie(), p.getRaza(), p.getEdad(), p.getDueno(), p.getTelefono()
            });
        }
    }
}
