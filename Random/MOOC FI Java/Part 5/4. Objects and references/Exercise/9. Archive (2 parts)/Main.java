import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<Archive> archiveList = new ArrayList<Archive>();

        while(true){
            System.out.println("Identifier? (empty will stop)");
            String identifer = input.nextLine();

            if(identifer.isEmpty()){
                break;
            }

            System.out.println("Name? (empty will stop)");
            String name = input.nextLine();

            if(name.isEmpty()){
                break;
            }

            Archive a = new Archive(identifer,name);
            if(!archiveList.contains(a)){
                archiveList.add(a);
            }
        }

        System.out.println("==Items==");

        for(Archive a: archiveList){
            System.out.println(a);
        }
    }
}