package animales;

public class Gato {
    String Nombre;
    String Color;
    int patas;
    
    public Gato(String name, String color, int legs){
        this.Nombre=name;
        this.Color=color;
        this.patas=legs;
        
    }
    
    public void Sonidogato(){
        System.out.println("El gato hace meow meow");
    }
    }

