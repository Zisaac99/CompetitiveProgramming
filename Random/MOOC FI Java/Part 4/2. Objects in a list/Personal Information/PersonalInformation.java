public class PersonalInformation{
    private String firstName;
    private String lastName;
    private String id;

    public PersonalInformation(String firstName, String lastName, String id){
        this.firstName = firstName;
        this.lastName = lastName;
        this.id = id;
    }

    @Override
    public String toString(){
        return this.firstName + " " + this.lastName;
    }
}