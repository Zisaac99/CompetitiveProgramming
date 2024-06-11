import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("Name of the file:");
        String fileName = input.nextLine();
        
        System.out.println();

        List<String> guestList = new ArrayList<String>();

        try{
            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                guestList.add(file.nextLine());
            }
        }catch(Exception e){
            System.out.println("Error: " + e);
        }

        System.out.println("Enter names, an empty line quits.");
        
        while(true){
            String name = input.nextLine();

            if(name.isEmpty()){
                break;
            }

            if(guestList.contains(name)){
                System.out.println("The name is on the list.");
            }else{
                System.out.println("The name is not on the list.");
            }
        }

        System.out.println("Thank you!");
    }
}