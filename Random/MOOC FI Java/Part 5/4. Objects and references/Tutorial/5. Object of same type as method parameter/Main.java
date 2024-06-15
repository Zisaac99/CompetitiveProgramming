public class Main{
    public static void main(String[] args){
        Person jamal = new Person("Jamal javontus IV",13,12,2002);
        Person jafar = new Person("Jafar javontus IV",14,12,2002);

        if(jamal.olderThan(jafar)){
            System.out.println(jamal.getName() + " is older than " + jafar.getName());
        }else{
            System.out.println(jafar.getName() + " is older than " + jamal.getName());
        }
    }
}