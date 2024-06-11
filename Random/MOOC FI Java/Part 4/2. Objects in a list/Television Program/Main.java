import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<TelevisionProgram> programList = new ArrayList<TelevisionProgram>();

        while(true){
            System.out.print("Name: ");
            String name = input.nextLine();

            if(name.isEmpty()){
                break;
            }

            System.out.print("Duration: ");
            int duration = Integer.valueOf(input.nextLine());

            programList.add(new TelevisionProgram(name,duration));
        }

        System.out.println();
        
        System.out.print("Program's maximum duration? ");
        int maxDuration = Integer.valueOf(input.nextLine());

        for(TelevisionProgram tp: programList){
            if(tp.getDuration() <= maxDuration){
                System.out.println(tp);
            }
        }
    }
}