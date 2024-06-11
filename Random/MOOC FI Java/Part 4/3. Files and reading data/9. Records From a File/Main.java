import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("Name of the file:");
        String fileName = input.nextLine();

        try{
            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                String line = file.nextLine();

                if(line.isEmpty()){
                    continue;
                }

                String[] data = line.split(",");

                String name = data[0];
                int age = Integer.valueOf(data[1]);
                String year = " years";
                if(age <= 1){
                    year = " year";
                }
                System.out.println(name + ", age: " + age + year);
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }
}