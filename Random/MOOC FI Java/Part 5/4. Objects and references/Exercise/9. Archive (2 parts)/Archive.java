public class Archive{
    private String identifer;
    private String name;

    public Archive(String identifer, String name){
        this.identifer = identifer;
        this.name = name;
    }

    @Override
    public String toString(){
        return this.identifer + ": " + this.name;
    }

    @Override
    public boolean equals(Object compared){
        if(this == compared){
            return true;
        }

        if(!(compared instanceof Archive)){
            return false;
        }

        Archive cA = (Archive) compared;
        if(this.identifer.equals(cA.identifer)){
            return true;
        }

        return false;
    }
}