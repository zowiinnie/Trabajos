package com.veterinaria.dao;

import com.veterinaria.modelo.Paciente;
import java.util.ArrayList;
import java.util.List;

/**
 * Clase que implementa el patrón Data Access Object (DAO) para la gestión de Pacientes.
 * Actualmente utiliza una persistencia simulada en memoria (ArrayList).
 * 
 * @author Arquitecto Java Senior
 */
public class PacienteDAO {
    private final List<Paciente> listaPacientes;

    /**
     * Inicializa la lista de pacientes en memoria.
     */
    public PacienteDAO() {
        this.listaPacientes = new ArrayList<>();
    }

    /**
     * Registra un nuevo paciente en el sistema.
     * @param paciente El objeto paciente a guardar.
     */
    public void guardar(Paciente paciente) {
        listaPacientes.add(paciente);
    }

    /**
     * Elimina un paciente de la lista por su índice.
     * @param index Índice del paciente en la lista.
     * @return true si se eliminó correctamente.
     */
    public boolean eliminar(int index) {
        if (index >= 0 && index < listaPacientes.size()) {
            listaPacientes.remove(index);
            return true;
        }
        return false;
    }

    /**
     * Obtiene todos los pacientes registrados.
     * @return Lista de pacientes.
     */
    public List<Paciente> obtenerTodos() {
        return new ArrayList<>(listaPacientes);
    }
    
    /**
     * Busca un paciente por ID.
     * @param id ID a buscar.
     * @return Paciente encontrado o null.
     */
    public Paciente buscarPorId(String id) {
        return listaPacientes.stream()
                .filter(p -> p.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}
