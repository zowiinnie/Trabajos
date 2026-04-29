package javaapplication13;

import java.util.Scanner;

public class JavaApplication13 {

    public static void main(String[] args) {
        Scanner Vicente=new Scanner(System.in);
        System.out.print("Dame la probabilidad: ");
        double probabilidadCarga = Vicente.nextDouble();
        if (probabilidadCarga >= 0.90){
            System.out.println("Altamente probable:");
            }
        else if (probabilidadCarga >= 0.60){
            System.out.println("Probabilidad media alta: ");
            }
        else if (probabilidadCarga >= 0.30){
            System.out.println("Probabilidad media baja: "); 
            }
        else{
             System.out.println("Baja probabilidad:");
                    }
        }
    
}
    

