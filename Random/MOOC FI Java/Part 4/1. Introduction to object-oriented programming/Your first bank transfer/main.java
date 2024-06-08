import java.util.*;

public class main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        Account mathewsAccount = new Account("Matthews account", 1000);
        Account myAccount = new Account("My account", 0);

        System.out.println("Initial state");
        System.out.println(mathewsAccount);
        System.out.println(myAccount);

        mathewsAccount.withdraw(100);
        myAccount.deposit(100);

        System.out.println("End state");
        System.out.println(mathewsAccount);
        System.out.println(myAccount);
    }
}