import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Counter counter = new Counter(10);
        System.out.println("Counter current value: " + counter.value());

        counter.increase(2);
        System.out.println("Counter current value: " + counter.value());
        counter.increase(4);
        System.out.println("Counter current value: " + counter.value());
        counter.decrease(8);
        System.out.println("Counter current value: " + counter.value());
    }
}