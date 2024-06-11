import java.util.*;
import java.nio.file.Paths;

public class StoringRecords{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("Filename: ");
        String fileName = input.nextLine();

        ArrayList<Person> personList = readRecordsFromFile(fileName);
        System.out.println("Number of persons: " + personList.size());
        System.out.println("Persons: ");

        for(Person p: personList){
            System.out.println(p);
        }

    }

    public static ArrayList<Person> readRecordsFromFile(String fileName){
        ArrayList<Person> personList = new ArrayList<Person>();

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
                personList.add(new Person(name,age));
            }
        }catch(Exception e){
            System.out.println(e);
        }

        return personList;
    }
}