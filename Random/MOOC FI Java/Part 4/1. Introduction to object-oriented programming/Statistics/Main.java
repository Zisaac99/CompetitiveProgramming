import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        Statistics totalSum = new Statistics();
        Statistics evenSum = new Statistics();
        Statistics oddSum = new Statistics();

        while(true){
            System.out.print("Enter number: ");
            int num = Integer.valueOf(input.nextLine());

            if(num == -1){
                break;
            }

            totalSum.addNumber(num);
            if(num % 2 == 0){
                evenSum.addNumber(num);
            }else{
                oddSum.addNumber(num);
            }

        }

        System.out.println("Sum: " + totalSum.sum());
        System.out.println("Sum of even numbers: " + evenSum.sum());
        System.out.println("Sum of odd numbers: " + oddSum.sum());
    }
}