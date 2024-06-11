import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<Integer> nums = new ArrayList<Integer>();
        int counter = 0;

        System.out.print("File? ");
        String fileName = input.nextLine();

        System.out.print("Lower bound? ");
        int lower = Integer.valueOf(input.nextLine());

        System.out.print("Upper bound? ");
        int upper = Integer.valueOf(input.nextLine());

        try{
            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                int num = Integer.valueOf(file.nextLine());
                nums.add(num);
            }
        }catch(Exception e){
            System.out.println(e);
        }


        for(int n: nums){
            if(n >= lower && n <= upper){
                counter += 1;
            }
        }

        System.out.println("Numbers: " + counter);
    }
}