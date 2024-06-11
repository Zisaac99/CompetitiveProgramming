import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<String> names = new ArrayList<String>();

        System.out.println("Name of the file:");
        String fileName = input.nextLine();

        System.out.println("Search for:");
        String name = input.nextLine();

        try{
            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                String line = file.nextLine();
                names.add(line);
            }

            if(names.contains(name)){
                System.out.println("Found!");
            }else{
                System.out.println("Not found.");
            }

        }catch(Exception e){
            System.out.println("Reading the file " + fileName + " failed");
        }
    }
}