package vehiculoautomotor;
class VehiculoAutomotor {
    protected double combustibleLitros;
    protected boolean encendido;

    public VehiculoAutomotor(double combustibleLitros) {
        this.combustibleLitros = combustibleLitros;
        this.encendido = false; 
    }

    public void arranconGen() {
        System.out.println("Iniciando arranque genérico del vehículo...");
    }
}
