import java.util.*;

public class arrays{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        //int[] numbers = new int[5];
        int[] numbers = {5, 1, 3, 4, 2};
        System.out.printf("Sum of array is: %d",sumOfNumbersInArray(numbers));
        printNeatly(numbers);
        printArrayInStars(numbers);
    }

    public static void printArrayVal(int[] arr){
        for(int val: arr){
            System.out.println(val);
        }
    }

    public static int check(int[] arr, int value){
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == value){
                return i;
            }
        }

        return -1;
    }

    public static int sumOfNumbersInArray(int[] arr){
        int sum = 0;
        for(int val: arr){
            sum += val;
        }

        return sum;
    }

    public static void printNeatly(int[] arr){
        String toPrint = "";
        int arrLen = arr.length;
        for(int i = 0; i < arrLen; i++){
            int val = arr[i];
            if(i == arrLen - 1){
                toPrint += String.valueOf(val);
            }else{
                toPrint += String.valueOf(val) + ", ";
            }
        }

        System.out.println(toPrint);
    }

    public static void printArrayInStars(int[] arr){
        String stars = "";
        for(int val: arr){
            for(int i = 0; i < val; i++){
                stars += "*";
            }
            System.out.println(stars);
            stars = "";
        }
    }
}