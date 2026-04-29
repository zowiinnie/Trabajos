
package javaapplication13;

public class JavaApplication13 {

    public static void main(String[] args) {
    int contador = 0; // Inicializamos un iterador

while (contador <= 5) {
    System.out.println("Iteración número: " + contador);
    contador++;
    }
 for (int i = 0; i < 10; i++) {
    System.out.println("Estamos en iteración " + i);
  }
int[]puntuaciones_sat = {1200, 1500, 1050, 1340, 950};
    
double [] probabilidadVentas =new double[4];
    
    probabilidadVentas [0] = 0.52;
    probabilidadVentas [1] = 0.70;
    
    System.out.println("El valor en la posicioón 2 de la lista puntuaciones_sat es: "+puntuaciones_sat[1]);
    
    }
}
