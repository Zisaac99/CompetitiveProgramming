public class Account{
    private String accountName;
    private double balance;

    public Account(String accountName, double balance){
        this.accountName = accountName;
        this.balance = balance; 
    } 

    public void withdraw(double amount){
        this.balance -= amount;
    }

    public void deposit(double amount){
        this.balance += amount;
    }

    public double balance(){
        return this.balance;
    }

    @Override 
    public String toString(){
        return this.accountName + " balance: " + this.balance;
    }


}