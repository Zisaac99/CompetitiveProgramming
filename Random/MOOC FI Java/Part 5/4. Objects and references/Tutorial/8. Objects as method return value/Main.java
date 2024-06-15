import java.util.*;

public class Main{
    public static void main(String[] args){
        Counter counter = new Counter();
        counter.increase();
        counter.increase();

        System.out.println(counter);         // prints 2

        Counter clone = counter.clone();

        System.out.println(counter);         // prints 2
        System.out.println(clone);          // prints 2

        counter.increase();
        counter.increase();
        counter.increase();
        counter.increase();

        System.out.println(counter);         // prints 6
        System.out.println(clone);          // prints 2

        clone.increase();

        System.out.println(counter);         // prints 6
        System.out.println(clone);          // prints 3
    }
}