import java.util.*;
import java.nio.file.Paths;

public class Main{
	public static void main(String[] args){
        Person paul = new Person("Paul", 24);
        System.out.println(paul);

        paul.growOlder();
        System.out.println(paul);

        paul.growOlder(10);
        System.out.println(paul);
    }
}

