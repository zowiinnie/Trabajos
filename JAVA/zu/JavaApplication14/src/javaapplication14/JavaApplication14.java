
package javaapplication14;
import java.util.Scanner;
public class JavaApplication14 {
    public static void main(String[] args) {
        
    Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- SENSOR DE ALERTA AMBIENTAL ---");
        System.out.print("Ingrese la temperatura del sistema (double): ");
        double nivelTemp = scanner.nextDouble();
        
        System.out.print("Ingrese presión del cilindro (int): ");
        int presion = scanner.nextInt();
        
        // Evaluamos doble factor de riesgo
        if (nivelTemp > 80.0 && presion > 100) {
            System.out.println("¡ALERTA ROJA! Riesgo inminente de explosión térmica.");
        } else if (nivelTemp > 80.0 || presion > 100) {
            System.out.println("Aviso: Un valor excedió el límite de control. Por favor, revise de inmediato.");
        } else {
            System.out.println("Sistema en condiciones operativas óptimas. Riesgo calculado bajo.");
        }
        
        scanner.close();
    }
}
       
