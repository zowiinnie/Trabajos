package javaapplication12;
import java.util.Scanner;
public class JavaApplication12 {
    
    public static void main(String[] args) {
        Scanner zu=new Scanner(System.in);
        System.out.println("Dame la opcion que quieras: ");
        int opcion_menu =zu.nextInt();
        switch(opcion_menu){
            case 1:
                System.out.println("Inciando ETL. . .");
                break;
            case 2:
                System.out.println("Filtrando base de datos. . .");
                break;
            case 3:
                System.out.println("Exportando a CSV. . .");
                break;
            default:
                System.out.println("Error 404: Opcion no válida en el sistema.");
                      
        }
    }
    
}
