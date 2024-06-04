import java.util.Scanner;
import java.util.ArrayList;

public class playground{
    public static void main(String[] args){
        // ArrayList<String> arr = new ArrayList<>();
        // Scanner input = new Scanner(System.in);

        // while(true){
        //     String name = input.nextLine();

        //     if(name.equals("")){
        //         break;
        //     }

        //     arr.add(name);
        // }

        // System.out.print("Search for? ");
        // String nameToFind = input.nextLine();

        // if(arr.contains(nameToFind)){
        //     System.out.printf("%s was found!",nameToFind);
        // }else{
        //     System.out.printf("%s was not found!",nameToFind);
        // }

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(3);
        numbers.add(2);
        numbers.add(6);
        numbers.add(-1);
 
        System.out.println(sum(numbers));

        numbers.add(5);
        numbers.add(1);
        System.out.println(sum(numbers));

        System.out.println(numbers.indexOf(1));

        // ArrayList<String> strings = new ArrayList<>();

        // strings.add("First");
        // strings.add("Second");
        // strings.add("Third");

        // System.out.println(strings);

        // removeLast(strings);
        // removeLast(strings);

        // System.out.println(strings);
    }

    public static void printNumbersInRange(ArrayList<Integer> list, int start, int end){
        for(Integer val: list){
            if(val >= start && val <= end){
                System.out.println(val);
            }
        }
    }

    public static int size(ArrayList<Integer> list){
        return list.size();
    }

    public static int sum(ArrayList<Integer> list){
        int totalSum = 0;
        for(Integer val: list){
            totalSum += val;
        }

        return totalSum;
    }

    public static void removeLast(ArrayList<String> list){
        list.remove(list.size() - 1);
    }
}