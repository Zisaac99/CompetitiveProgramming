import java.util.*;
import java.lang.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Fitbyte assistant = new Fitbyte(30, 60);

        int percentage = 50;

        while (percentage < 100) {
            double target = assistant.targetHeartRate(1.0 * percentage /100);
            System.out.println("Target " + (percentage) + "% of maximum: " + target);
            percentage = percentage + 10;
        }
    }
}