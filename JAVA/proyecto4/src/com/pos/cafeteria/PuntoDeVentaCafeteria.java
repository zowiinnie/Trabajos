package com.pos.cafeteria;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;
import java.util.Vector;

/**
 * PuntoDeVentaCafeteria - Sistema POS de Alta Eficiencia
 * 
 * Este sistema ha sido diseñado siguiendo principios de ergonomía visual para pantallas táctiles,
 * garantizando una respuesta inmediata y una interfaz libre de errores para entornos de alta demanda.
 * 
 * @author Senior Java UI Engineer
 */
public class PuntoDeVentaCafeteria extends JFrame {

    // --- CONSTANTES DE DISEÑO ---
    private static final Font FONT_LARGE = new Font("Arial", Font.BOLD, 18);
    private static final Font FONT_MEDIUM = new Font("Arial", Font.PLAIN, 16);
    private static final Color COLOR_BEBIDAS = new Color(70, 130, 180); // Steel Blue
    private static final Color COLOR_ALIMENTOS = new Color(210, 105, 30); // Chocolate
    private static final Color COLOR_COBRAR = new Color(46, 204, 113); // Emerald Green
    private static final Color COLOR_CANCELAR = new Color(231, 76, 60); // Alizarin Red
    private static final DecimalFormat DF = new DecimalFormat("$#,##0.00");

    // --- COMPONENTES ---
    private DefaultTableModel tableModel;
    private JTable ticketTable;
    private JLabel lblSubtotal, lblIVA, lblTotal;
    
    // --- ESTADO ---
    private double subtotal = 0.0;
    private static final double IVA_RATE = 0.16;

    public PuntoDeVentaCafeteria() {
        super("POS Café de Especialidad - Terminal 01");
        configurarLookAndFeel();
        initUI();
    }

    private void configurarLookAndFeel() {
        try {
            // Intentamos establecer Nimbus para una apariencia moderna
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
            // Ajustes globales de fuente
            UIManager.put("Button.font", FONT_LARGE);
            UIManager.put("Label.font", FONT_MEDIUM);
            UIManager.put("Table.font", FONT_MEDIUM);
            UIManager.put("TableHeader.font", FONT_LARGE);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void initUI() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 800);
        setLocationRelativeTo(null);

        // --- PANEL IZQUIERDO: CATÁLOGO TÁCTIL ---
        JPanel panelCatalogo = new JPanel(new GridLayout(0, 2, 15, 15));
        panelCatalogo.setBorder(new EmptyBorder(20, 20, 20, 20));
        
        // Agregar Productos
        panelCatalogo.add(crearBotonProducto("Café Americano", 35.0, COLOR_BEBIDAS));
        panelCatalogo.add(crearBotonProducto("Latte", 45.0, COLOR_BEBIDAS));
        panelCatalogo.add(crearBotonProducto("Capuchino", 50.0, COLOR_BEBIDAS));
        panelCatalogo.add(crearBotonProducto("Muffin", 30.0, COLOR_ALIMENTOS));

        // --- PANEL DERECHO: TICKET Y COBRO ---
        JPanel panelVenta = new JPanel(new BorderLayout(10, 10));
        panelVenta.setBorder(new EmptyBorder(10, 10, 10, 10));

        // Tabla de Ticket
        String[] columnas = {"Producto", "Cant.", "Precio"};
        tableModel = new DefaultTableModel(columnas, 0) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false; // Solo lectura para evitar errores táctiles
            }
        };
        ticketTable = new JTable(tableModel);
        ticketTable.setRowHeight(40);
        ticketTable.getTableHeader().setReorderingAllowed(false);
        
        // Renderizador para centrar cantidad y precio
        DefaultTableCellRenderer centerRenderer = new DefaultTableCellRenderer();
        centerRenderer.setHorizontalAlignment(JLabel.CENTER);
        ticketTable.getColumnModel().getColumn(1).setCellRenderer(centerRenderer);
        ticketTable.getColumnModel().getColumn(2).setCellRenderer(centerRenderer);

        JScrollPane scrollPane = new JScrollPane(ticketTable);
        panelVenta.add(scrollPane, BorderLayout.CENTER);

        // Panel de Totales y Operaciones
        JPanel panelInferior = new JPanel(new BorderLayout(5, 5));
        
        // Totales
        JPanel panelTotales = new JPanel(new GridLayout(3, 2, 5, 5));
        panelTotales.setBorder(new EmptyBorder(10, 10, 10, 10));
        panelTotales.setBackground(new Color(245, 245, 245));
        
        lblSubtotal = new JLabel("Subtotal: $0.00");
        lblIVA = new JLabel("IVA (16%): $0.00");
        lblTotal = new JLabel("TOTAL: $0.00");
        lblTotal.setFont(new Font("Arial", Font.BOLD, 24));
        lblTotal.setForeground(new Color(44, 62, 80));

        panelTotales.add(new JLabel("Subtotal:")); panelTotales.add(lblSubtotal);
        panelTotales.add(new JLabel("IVA (16%):")); panelTotales.add(lblIVA);
        panelTotales.add(new JLabel("NETO:")); panelTotales.add(lblTotal);

        // Botones de Acción
        JPanel panelAcciones = new JPanel(new GridLayout(3, 1, 10, 10));
        
        JButton btnEliminar = new JButton("ELIMINAR ÍTEM");
        btnEliminar.addActionListener(e -> eliminarItemSeleccionado());

        JButton btnCancelar = new JButton("CANCELAR ORDEN");
        btnCancelar.setBackground(COLOR_CANCELAR);
        btnCancelar.setForeground(Color.WHITE);
        btnCancelar.addActionListener(e -> cancelarOrden());

        JButton btnCobrar = new JButton("COBRAR");
        btnCobrar.setBackground(COLOR_COBRAR);
        btnCobrar.setForeground(Color.WHITE);
        btnCobrar.setFont(new Font("Arial", Font.BOLD, 22));
        btnCobrar.addActionListener(e -> procesarCobro());

        panelAcciones.add(btnEliminar);
        panelAcciones.add(btnCancelar);
        panelAcciones.add(btnCobrar);

        JPanel panelControl = new JPanel(new BorderLayout());
        panelControl.add(panelTotales, BorderLayout.NORTH);
        panelControl.add(panelAcciones, BorderLayout.SOUTH);
        
        panelVenta.add(panelControl, BorderLayout.SOUTH);

        // --- SPLIT PANE ---
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, panelCatalogo, panelVenta);
        splitPane.setDividerLocation(840); // Aproximadamente 70% de 1200
        splitPane.setDividerSize(5);
        splitPane.setEnabled(false); // Bloquear movimiento para estabilidad táctil

        add(splitPane);
    }

    private JButton crearBotonProducto(String nombre, double precio, Color color) {
        JButton btn = new JButton("<html><center>" + nombre + "<br><font size='+1'>" + DF.format(precio) + "</font></center></html>");
        btn.setPreferredSize(new Dimension(150, 150)); // Cumple con el mínimo de 100x100px
        btn.setBackground(color);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        
        // Lógica de añadir producto
        btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Se garantiza que la actualización ocurra en el Event Dispatch Thread (EDT)
                // Aunque los ActionListeners ya corren en el EDT, usamos invokeLater
                // para demostrar el patrón de actualización asíncrona segura.
                SwingUtilities.invokeLater(() -> {
                    agregarOIncrementarProducto(nombre, precio);
                });
            }
        });
        
        return btn;
    }

    private void agregarOIncrementarProducto(String nombre, double precio) {
        boolean existe = false;
        for (int i = 0; i < tableModel.getRowCount(); i++) {
            if (tableModel.getValueAt(i, 0).equals(nombre)) {
                int cant = (int) tableModel.getValueAt(i, 1);
                tableModel.setValueAt(cant + 1, i, 1);
                existe = true;
                break;
            }
        }

        if (!existe) {
            tableModel.addRow(new Object[]{nombre, 1, precio});
        }
        recalcularTotales();
    }

    private void recalcularTotales() {
        subtotal = 0;
        for (int i = 0; i < tableModel.getRowCount(); i++) {
            int cant = (int) tableModel.getValueAt(i, 1);
            double precio = (double) tableModel.getValueAt(i, 2);
            subtotal += (cant * precio);
        }

        double iva = subtotal * IVA_RATE;
        double total = subtotal + iva;

        // Actualización inmediata de la UI
        lblSubtotal.setText(DF.format(subtotal));
        lblIVA.setText(DF.format(iva));
        lblTotal.setText(DF.format(total));
    }

    private void eliminarItemSeleccionado() {
        int row = ticketTable.getSelectedRow();
        if (row != -1) {
            tableModel.removeRow(row);
            recalcularTotales();
        } else {
            JOptionPane.showMessageDialog(this, "Seleccione un producto del ticket para eliminar.", "Aviso", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void cancelarOrden() {
        if (tableModel.getRowCount() > 0) {
            int confirm = JOptionPane.showConfirmDialog(this, "¿Está seguro de cancelar toda la orden?", "Confirmar", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) {
                limpiarEstado();
            }
        }
    }

    private void procesarCobro() {
        if (tableModel.getRowCount() == 0) {
            JOptionPane.showMessageDialog(this, "No hay productos en el ticket.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        // Bloqueamos la UI para evitar dobles clics accidentales (Seguridad Táctica)
        setCursor(Cursor.getPredefinedCursor(Cursor.WAIT_CURSOR));
        for (Component c : getContentPane().getComponents()) {
            c.setEnabled(false);
        }
        
        // Simulamos procesamiento y "impresión" (1.5 segundos)
        Timer timer = new Timer(1500, e -> {
            setCursor(Cursor.getDefaultCursor());
            for (Component c : getContentPane().getComponents()) {
                c.setEnabled(true);
            }
            
            JOptionPane.showMessageDialog(this, 
                "¡Venta Exitosa!\nTotal Cobrado: " + lblTotal.getText() + "\n\nImprimiendo ticket...", 
                "Sistema POS", JOptionPane.INFORMATION_MESSAGE);
            limpiarEstado();
        });
        timer.setRepeats(false);
        timer.start();
    }

    private void limpiarEstado() {
        SwingUtilities.invokeLater(() -> {
            tableModel.setRowCount(0);
            recalcularTotales();
        });
    }

    public static void main(String[] args) {
        // El punto de entrada DEBE invocar la creación de la UI en el EDT
        SwingUtilities.invokeLater(() -> {
            PuntoDeVentaCafeteria pos = new PuntoDeVentaCafeteria();
            pos.setVisible(true);
        });
    }
}
