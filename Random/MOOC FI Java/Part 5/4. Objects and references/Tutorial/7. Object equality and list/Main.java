import java.util.*;

public class Main{
    public static void main(String[] args){
        ArrayList<Bird> birds = new ArrayList<>();
        Bird red = new Bird("Red");

        if (birds.contains(red)) {
            System.out.println("Red is on the list.");
        } else {
            System.out.println("Red is not on the list.");
        }

        birds.add(red);
        if (birds.contains(red)) {
            System.out.println("Red is on the list.");
        } else {
            System.out.println("Red is not on the list.");
        }


        System.out.println("However!");

        red = new Bird("Red");
        if (birds.contains(red)) {
            System.out.println("Red is on the list.");
        } else {
            System.out.println("Red is not on the list.");
        }
    }
}