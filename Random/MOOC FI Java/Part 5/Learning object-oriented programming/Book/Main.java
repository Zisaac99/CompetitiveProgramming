import java.util.*;
import java.lang.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Author: ");
        String author = input.nextLine();

        System.out.print("Enter name of book: ");
        String name = input.nextLine();

        System.out.print("Enter number of pages: ");
        int pages = Integer.valueOf(input.nextLine());

        Book book = new Book(author,name,pages);
        System.out.println(book);
    }
}