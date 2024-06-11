public class TelevisionProgram{
    private String name;
    private int duration;

    public TelevisionProgram(String name, int duration){
        this.name = name;
        this.duration = duration;
    }

    public int getDuration(){
        return this.duration;
    }

    @Override
    public String toString(){
        return this.name + ", " + this.duration + " minutes";
    }
}