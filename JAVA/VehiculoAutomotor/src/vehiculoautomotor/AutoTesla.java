package vehiculoautomotor;
class AutoTesla extends VehiculoAutomotor {
    private int bateriaElectronica;

    // Constructor Hijo
    public AutoTesla(double litros, int cargaBateria) {
        super(litros); // Llama al constructor del padre
        this.bateriaElectronica = cargaBateria;
    }

    @Override
    public void arranconGen() {
        // Sobrescritura del comportamiento
        System.out.println("El sistema de Autopilot dirige este arranque usando batería. Nivel de energía: " + bateriaElectronica + "%");
    }
}