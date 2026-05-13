package com.veterinaria.vista;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

/**
 * Ventana principal del sistema veterinario.
 * Diseñada con un enfoque profesional, utilizando bordes y alineación correcta.
 * 
 * @author Arquitecto Java Senior
 */
public class VentanaPrincipal extends JFrame {
    
    // Componentes del Formulario
    public JTextField txtId, txtNombre, txtEspecie, txtRaza, txtEdad, txtDueno, txtTelefono;
    public JTextArea txtSintomas;
    public JButton btnGuardar, btnEliminar, btnLimpiar;
    public JTable tablaPacientes;
    public DefaultTableModel modeloTabla;

    public VentanaPrincipal() {
        configurarVentana();
        inicializarComponentes();
    }

    private void configurarVentana() {
        setTitle("Sistema de Gestión Veterinaria - Registro de Pacientes");
        setSize(1000, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));
    }

    private void inicializarComponentes() {
        // Panel Lateral (Formulario)
        JPanel panelForm = new JPanel(new GridBagLayout());
        panelForm.setBorder(BorderFactory.createCompoundBorder(
                new EmptyBorder(10, 10, 10, 10),
                BorderFactory.createTitledBorder("Datos del Paciente")
        ));
        panelForm.setPreferredSize(new Dimension(350, 0));
        
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.weightx = 1.0;

        // Labels y Fields
        txtId = addField(panelForm, "ID:", 0, gbc);
        txtNombre = addField(panelForm, "Nombre:", 1, gbc);
        txtEspecie = addField(panelForm, "Especie:", 2, gbc);
        txtRaza = addField(panelForm, "Raza:", 3, gbc);
        txtEdad = addField(panelForm, "Edad:", 4, gbc);
        txtDueno = addField(panelForm, "Dueño:", 5, gbc);
        txtTelefono = addField(panelForm, "Teléfono:", 6, gbc);
        
        gbc.gridy = 7; gbc.gridx = 0;
        panelForm.add(new JLabel("Síntomas:"), gbc);
        txtSintomas = new JTextArea(4, 20);
        txtSintomas.setLineWrap(true);
        gbc.gridy = 8;
        panelForm.add(new JScrollPane(txtSintomas), gbc);

        // Panel de Botones
        JPanel panelBotones = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        btnGuardar = new JButton("Guardar");
        btnLimpiar = new JButton("Limpiar");
        btnEliminar = new JButton("Eliminar");
        
        // Estilo de botones (neutros)
        btnGuardar.setBackground(new Color(230, 230, 230));
        btnEliminar.setForeground(Color.RED);
        
        panelBotones.add(btnLimpiar);
        panelBotones.add(btnEliminar);
        panelBotones.add(btnGuardar);
        
        gbc.gridy = 9;
        panelForm.add(panelBotones, gbc);

        // Panel Central (Tabla)
        JPanel panelTabla = new JPanel(new BorderLayout());
        panelTabla.setBorder(new EmptyBorder(10, 10, 10, 10));
        
        String[] columnas = {"ID", "Nombre", "Especie", "Raza", "Edad", "Dueño", "Teléfono"};
        modeloTabla = new DefaultTableModel(columnas, 0) {
            @Override
            public boolean isCellEditable(int row, int column) { return false; }
        };
        tablaPacientes = new JTable(modeloTabla);
        tablaPacientes.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        
        JScrollPane scrollPane = new JScrollPane(tablaPacientes);
        panelTabla.add(new JLabel("Pacientes Registrados", JLabel.CENTER), BorderLayout.NORTH);
        panelTabla.add(scrollPane, BorderLayout.CENTER);

        // Ensamblado
        add(panelForm, BorderLayout.WEST);
        add(panelTabla, BorderLayout.CENTER);
    }

    private JTextField addField(JPanel panel, String label, int row, GridBagConstraints gbc) {
        gbc.gridy = row; gbc.gridx = 0;
        gbc.weightx = 0.3;
        panel.add(new JLabel(label), gbc);
        
        JTextField field = new JTextField();
        gbc.gridx = 0; gbc.gridy = row + 1; // Ajuste para que el label esté arriba o al lado
        // Pero mejor alineado horizontalmente para formulario profesional
        gbc.gridx = 1; gbc.gridy = row;
        gbc.weightx = 0.7;
        panel.add(field, gbc);
        return field;
    }

    public void limpiarCampos() {
        txtId.setText("");
        txtNombre.setText("");
        txtEspecie.setText("");
        txtRaza.setText("");
        txtEdad.setText("");
        txtDueno.setText("");
        txtTelefono.setText("");
        txtSintomas.setText("");
    }
}
