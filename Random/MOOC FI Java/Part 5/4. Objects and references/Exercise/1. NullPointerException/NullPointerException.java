import java.util.*;

public class NullPointerException{
    public static void main(String[] args){
        ArrayList<String> arr = new ArrayList<String>();
        arr = null;
        arr.add("test");
    }
}