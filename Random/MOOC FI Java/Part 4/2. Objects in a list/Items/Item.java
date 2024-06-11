import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Item{
    private String name;
    private LocalDateTime dateTimeCreatedAt;

    public Item(String name){
        this.name = name;
        this.dateTimeCreatedAt = LocalDateTime.now();
    }

    @Override
    public String toString(){
        DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        return this.name + " (created at: " + this.dateTimeCreatedAt.format(myFormatObj) + ")";
    }
}