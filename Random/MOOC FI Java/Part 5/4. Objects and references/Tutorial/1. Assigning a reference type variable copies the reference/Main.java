public class Main{
    public static void main(String[] args){
        Person joan = new Person("Joan Ball");
        System.out.println(joan);

        Person ball = joan;
        ball.growOlder();
        ball.growOlder();

        System.out.println(joan);

        joan = new Person("Joan B.");
        System.out.println(joan);
    }
}