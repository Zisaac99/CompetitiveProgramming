import java.util.*;
import java.lang.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        // Person:

        // Scanner reader = new Scanner(System.in);
        // System.out.println("What's your name?");
        // String name = reader.nextLine();
        // System.out.println("What's your age?");
        // int age = Integer.valueOf(reader.nextLine());
        // System.out.println("What's your weight?");
        // double weight = Double.valueOf(reader.nextLine());
        // System.out.println("What's your height?");
        // double height = Double.valueOf(reader.nextLine());

        // Person person = new Person(name, age, weight, height);
        // System.out.println(person);

        //Rectangle:
        
        Rectangle first = new Rectangle(40, 80);
        Rectangle rectangle = new Rectangle(10, 10);
        System.out.println(first);
        System.out.println(rectangle);

        first.narrow();
        System.out.println(first);
        System.out.println(first.surfaceArea());
    }
}