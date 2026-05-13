package com.veterinaria.modelo;

/**
 * Clase que representa el modelo de dominio de un Paciente en el sistema veterinario.
 * Sigue el principio de encapsulamiento estricto.
 * 
 * @author Arquitecto Java Senior
 */
public class Paciente {
    private String id;
    private String nombre;
    private String especie;
    private String raza;
    private int edad;
    private String dueno;
    private String telefono;
    private String sintomas;

    /**
     * Constructor por defecto.
     */
    public Paciente() {
    }

    /**
     * Constructor sobrecargado para inicialización completa.
     * 
     * @param id Identificador único del paciente.
     * @param nombre Nombre del animal.
     * @param especie Especie (ej. Canino, Felino).
     * @param raza Raza del animal.
     * @param edad Edad en años.
     * @param dueno Nombre del propietario.
     * @param telefono Teléfono de contacto.
     * @param sintomas Descripción de los síntomas.
     */
    public Paciente(String id, String nombre, String especie, String raza, int edad, String dueno, String telefono, String sintomas) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.raza = raza;
        this.edad = edad;
        this.dueno = dueno;
        this.telefono = telefono;
        this.sintomas = sintomas;
    }

    // Getters y Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getEspecie() { return especie; }
    public void setEspecie(String especie) { this.especie = especie; }

    public String getRaza() { return raza; }
    public void setRaza(String raza) { this.raza = raza; }

    public int getEdad() { return edad; }
    public void setEdad(int edad) { this.edad = edad; }

    public String getDueno() { return dueno; }
    public void setDueno(String dueno) { this.dueno = dueno; }

    public String getTelefono() { return telefono; }
    public void setTelefono(String telefono) { this.telefono = telefono; }

    public String getSintomas() { return sintomas; }
    public void setSintomas(String sintomas) { this.sintomas = sintomas; }

    @Override
    public String toString() {
        return "Paciente{" + "id=" + id + ", nombre=" + nombre + ", dueno=" + dueno + '}';
    }
}
