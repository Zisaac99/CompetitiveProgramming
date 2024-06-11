import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        List<Books> bookList = new ArrayList<Books>();

        while(true){
            System.out.print("Title: ");
            String title = input.nextLine();

            if(title.isEmpty()){
                break;
            }

            System.out.print("Pages: ");
            int pages = Integer.valueOf(input.nextLine());

            System.out.print("Publication Year: ");
            int pubYear = Integer.valueOf(input.nextLine());

            bookList.add(new Books(title,pages,pubYear));
        }

        System.out.println();

        System.out.print("What information will be printed?");
        String whatToPrint =  input.nextLine();

        for(Books b: bookList){
            if(whatToPrint.equals("everything")){
                System.out.println(b);
            }else if(whatToPrint.equals("name")){
                System.out.println(b.getTitle());
            }
        }
    }
}