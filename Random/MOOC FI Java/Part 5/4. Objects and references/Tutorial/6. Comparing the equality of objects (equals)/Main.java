import java.util.*;

public class Main{
    public static void main(String[] args){
        SimpleDate first = new SimpleDate(1, 1, 2000);
        SimpleDate second = new SimpleDate(1, 1, 2000);
        SimpleDate third = new SimpleDate(12, 12, 2012);
        SimpleDate fourth = first;

        if (first.equals(first)) {
            System.out.println("Variables first and first are equal");
        } else {
            System.out.println("Variables first and first are not equal");
        }

        if (first.equals(second)) {
            System.out.println("Variables first and second are equal");
        } else {
            System.out.println("Variables first and second are not equal");
        }

        if (first.equals(third)) {
            System.out.println("Variables first and third are equal");
        } else {
            System.out.println("Variables first and third are not equal");
        }

        if (first.equals(fourth)) {
            System.out.println("Variables first and fourth are equal");
        } else {
            System.out.println("Variables first and fourth are not equal");
        }
    }
}