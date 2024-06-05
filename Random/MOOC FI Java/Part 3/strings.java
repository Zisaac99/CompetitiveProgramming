import java.util.*;

public class strings{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
        //login(input);
        // lineByLine(input);
        // av(input);
        // lastWords(input);
        // ageOfOldest(input);
        // nameOfOldest(input);
        personalDetails(input);
    }

    public static void login(Scanner input){
        List<String> usernames = new ArrayList<String>(Arrays.asList("alex","emma"));
        List<String> passwords = new ArrayList<String>(Arrays.asList("sunshine","haskell"));


        System.out.print("Enter username: ");
        String user = input.nextLine();

        System.out.print("Enter password: ");
        String pass = input.nextLine();

        boolean successfulLogin = false;

        for(int i = 0; i < usernames.size(); i++){
            if(user.equals(usernames.get(i)) && pass.equals(passwords.get(i))){
                successfulLogin = true;
                break;
            }
        }

        if(successfulLogin){
            System.out.println("You have successfully logged in!");
        }else{
            System.out.println("Incorrect username or password!");
        }
    }

    public static void lineByLine(Scanner input){
        System.out.print("Enter a string: ");
        String str = input.nextLine();
        String[] strArr = str.split(" ");

        for(String s: strArr){
            System.out.println(s);
        }
    }

    public static void av(Scanner input){
        while(true){
            System.out.print("Enter a string: ");
            String str = input.nextLine();

            if(str.equals("")){
                break;
            }

            String[] strSplit = str.split(" ");

            for(String s: strSplit){
                if(s.contains("av")){
                    System.out.println(s);
                }
            }
        }
    }

    public static void lastWords(Scanner input){
        while(true){
            System.out.print("Enter a string: ");
            String str = input.nextLine();

            if(str.equals("")){
                break;
            }

            String[] strSplit = str.split("");

            System.out.println(strSplit[strSplit.length - 1]);
        }
    }

    public static void ageOfOldest(Scanner input){
        int maxAge = Integer.MIN_VALUE;
        while(true){
            System.out.print("Enter a string: ");
            String str = input.nextLine();

            if(str.equals("")){
                break;
            }

            String[] strSplit = str.split(",");

            int currAge = Integer.valueOf(strSplit[1]);

            if(currAge > maxAge){
                maxAge = currAge;
            }
        }
        System.out.printf("Age of the oldest: %d\n",maxAge);
    }

    public static void nameOfOldest(Scanner input){
        int maxAge = Integer.MIN_VALUE;
        String nameOldest = "";
        while(true){
            System.out.print("Enter a string: ");
            String str = input.nextLine();

            if(str.equals("")){
                break;
            }

            String[] strSplit = str.split(",");

            int currAge = Integer.valueOf(strSplit[1]);

            if(currAge > maxAge){
                maxAge = currAge;
                nameOldest = strSplit[0];
            }
        }
        System.out.printf("Name of the oldest: %s\n",nameOldest);
    }

    public static void personalDetails(Scanner input){
        String longestName = "";
        Double sumOfYears = 0.0;
        int num = 0;
        while(true){
            System.out.print("Enter a string: ");
            String str = input.nextLine();

            if(str.equals("")){
                break;
            }

            String[] strSplit = str.split(",");

            String name = strSplit[0];

            if(name.length() > longestName.length()){
                longestName = name;
            }

            sumOfYears += Double.valueOf(strSplit[1]);
            num += 1;
        }

        System.out.printf("Longest Name: %s\n",longestName);
        System.out.printf("Average of the birth years: " + (sumOfYears / num));
    }
}