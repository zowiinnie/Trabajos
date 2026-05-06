package vehiculoautomotor;
public class Main {

    public static void main(String[] args) {
        // Instancia del AutoTesla
        // Pasamos 0 litros (es eléctrico, pero el padre lo requiere) y 95% de batería
        AutoTesla miTesla = new AutoTesla(0.0, 95);

        // Ejecución del método sobrescrito
        miTesla.arranconGen();
    }
}