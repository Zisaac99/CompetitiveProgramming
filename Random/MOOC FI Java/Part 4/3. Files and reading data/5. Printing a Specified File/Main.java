import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        try{
            Scanner input = new Scanner(System.in);
            System.out.println("Which file should have its contents printed?");
            String fileName = input.nextLine();

            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                String text = file.nextLine();
                System.out.println(text);
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }
}