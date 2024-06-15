public class Person {

    private String name;
    private SimpleDate birthday;
    
    public Person(String name, SimpleDate date) {
        this.name = name;
        this.birthday = date;
    }

    public Person(String name, int day, int month, int year) {
        this.name = name;
        this.birthday = new SimpleDate(day,month,year);
    }

    // other constructors and methods

    public String getName() {
        return this.name;
    }

    @Override
    public String toString() {
        return this.name + ", born on " + this.birthday;
    }
}