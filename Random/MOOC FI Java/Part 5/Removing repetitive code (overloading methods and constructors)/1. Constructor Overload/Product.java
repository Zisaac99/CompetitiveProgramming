public class Product{
    private String location;
    private String name;
    private int weight;

    public Product(String name){
        this(name,"shelf");
    }

    public Product(String name, String location){
        this.name = name;
        this.location = location;
        this.weight = 1;
    }

    public Product(String name, int weight){
        this.name = name;
        this.location = "shelf";
        this.weight = weight;
    }

    @Override
    public String toString(){
        return this.name + " (" + this.weight + " kg) can be found from the " + this.location;
    }
}