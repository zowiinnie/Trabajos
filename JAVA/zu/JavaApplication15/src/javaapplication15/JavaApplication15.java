package javaapplication15;
import java.util.Scanner;
public class JavaApplication15 {
    
    public static void main(String[] args) {
        Scanner lector=new Scanner(System.in);
        System.out.println("Dame tu salario anual: ");
        double salario=lector.nextDouble();
        
        if (salario <= 10000 ){
            System.out.printf("La cantidad de %.2f no paga impuestos.", salario);
        }
        else if (salario  <= 30000.00){
            double impuesto=salario*0.15;
            System.out.printf("Debe pagar %.2f pesos.", impuesto);
        }
        else{
            double impu=salario*0.3;
            System.out.printf("La cantidad de impuestos a pagar es: %.2f", impu);
    }
    
    }
}
