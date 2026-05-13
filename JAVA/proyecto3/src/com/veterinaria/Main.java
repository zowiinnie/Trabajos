package com.veterinaria;

import com.veterinaria.controlador.PacienteController;
import com.veterinaria.dao.PacienteDAO;
import com.veterinaria.vista.VentanaPrincipal;
import javax.swing.UIManager;

/**
 * Clase principal que inicia la aplicación.
 * Configura el Look And Feel y ensambla las capas del MVC.
 * 
 * @author Arquitecto Java Senior
 */
public class Main {
    public static void main(String[] args) {
        // Establecer Look And Feel del sistema para una apariencia nativa profesional
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            // Continuar con el Look And Feel por defecto si falla
        }

        // Ejecutar en el Event Dispatch Thread (EDT) para seguridad de hilos en Swing
        java.awt.EventQueue.invokeLater(() -> {
            // 1. Instanciar el DAO (Modelo de Datos)
            PacienteDAO dao = new PacienteDAO();
            
            // 2. Instanciar la Vista (UI)
            VentanaPrincipal vista = new VentanaPrincipal();
            
            // 3. Instanciar el Controlador (Puente)
            new PacienteController(vista, dao);
            
            // 4. Mostrar la aplicación
            vista.setVisible(true);
        });
    }
}
