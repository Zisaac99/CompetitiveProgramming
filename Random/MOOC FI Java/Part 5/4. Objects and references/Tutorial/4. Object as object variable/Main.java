import java.util.*;
import java.nio.file.Paths;
import java.time.LocalDate;

public class Main{
    public static void main(String[] args){
        SimpleDate date = new SimpleDate(1, 1, 780);
        Person muhammad = new Person("Muhammad ibn Musa al-Khwarizmi", date);
        Person pascal = new Person("Blaise Pascal", 19, 6, 1623);

        System.out.println(muhammad);
        System.out.println(pascal);

        LocalDate time = LocalDate.now();
        System.out.println(time);
        System.out.println(time.getDayOfMonth());
        System.out.println(time.getMonthValue());
        System.out.println(time.getYear());
    }
}