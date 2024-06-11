import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<PersonalInformation> personalInfoList = new ArrayList<PersonalInformation>();

        while(true){
            System.out.print("First name: ");
            String firstName = input.nextLine();

            if(firstName.equals("")){
                break;
            }

            System.out.print("Last name: ");
            String lastName = input.nextLine();

            System.out.print("Identification number: ");
            String id = input.nextLine();

            personalInfoList.add(new PersonalInformation(firstName,lastName,id));
        }

        System.out.println();
        
        for(PersonalInformation pi: personalInfoList){
            System.out.println(pi);
        }
    }
}