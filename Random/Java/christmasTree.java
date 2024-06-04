public class christmasTree{
    public static void main(String[] args){
        christmasTrees(102);
    }

    public static void christmasTrees(int size){
        int maxStars = (size * 2) - 1;
        String trunk = "";
        for(int i = 1; i <= size; i++){
            int numberOfStars = (i * 2) - 1;
            int numberOfSpaces = (maxStars - numberOfStars) / 2;
            String space = printSpaces(numberOfSpaces);
            String line = space + printStars(numberOfStars) + space;

            if(i == 2){
                trunk = line;
            }

            System.out.println(line);
        }

        System.out.println(trunk);
        System.out.println(trunk);
    }

    public static String printStars(int num){
        String stars = "";
        for(int i = 0; i < num; i++){
            stars += "*";
        }
        return stars;
    }

    public static String printSpaces(int num){
        String space = "";
        for(int i = 0; i < num; i++){
            space += " ";
        }
        return space;
    }
    
}