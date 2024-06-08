public class Person{
    private String name;
    private int age;
    private int weight;
    private int height;

    public Person(String initialName) {
        this.age = 0;
        this.weight = 0;
        this.height = 0;
        this.name = initialName;
    }

    public void setHeight(int newHeight) {
        this.height = newHeight;
    }

    public void setWeight(int newWeight) {
        this.weight = newWeight;
    }

    public double bodyMassIndex(){
        double heigthPerHundred  = this.height / 100.0;
        return (this.weight / (heigthPerHundred * heigthPerHundred));
    }

    public void growOlder(){
        this.age += 1;
    }

    public int returnAge(){
        return this.age;
    }

    public boolean isOfLegalAge(){
        if(this.age >= 18){
            return true;
        }

        return false;
    }

    public String getName(){
        return this.name;
    }

    @Override
    public String toString(){
        return this.name + ", age " + this.age + " years";
    }
}