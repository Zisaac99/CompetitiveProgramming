public class Main{
    public static void main(String[] args){
        int first = 10;
        int second = first;
        int third = second;
        System.out.println(first + " " + second + " " + third);
        second = 5;
        System.out.println(first + " " + second + " " + third);
    }
}