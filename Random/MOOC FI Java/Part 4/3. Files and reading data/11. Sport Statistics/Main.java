import java.util.*;
import java.nio.file.Paths;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("File:");
        String fileName = input.nextLine();

        System.out.println("Team:");
        String team = input.nextLine();

        ArrayList<Games> gamesList = readRecordsFromFile(fileName);

        // Part 1:
        // System.out.println("Games: " + countGames(team,gamesList));


        // Part 2:
        int stats[] = winsAndLosses(team,gamesList);

        System.out.println("Games: " + stats[0]);
        System.out.println("Wins: " + stats[1]);
        System.out.println("Losses: " + stats[2]);
    }

    public static ArrayList<Games> readRecordsFromFile(String fileName){
        ArrayList<Games> gamesList= new ArrayList<Games>();

        try{
            Scanner file = new Scanner(Paths.get(fileName));

            while(file.hasNextLine()){
                String line = file.nextLine();
                if(line.isEmpty()){
                    continue;
                }

                String[] data = line.split(",");

                String vt = data[0];
                String ht = data[1];
                int vtp = Integer.valueOf(data[2]);
                int htp = Integer.valueOf(data[3]);

                gamesList.add(new Games(vt,ht,vtp,htp));

            }
        }catch(Exception e){
            System.out.println(e);
        }

        return gamesList;
    }

    public static int countGames(String name, ArrayList<Games> list){
        int counter = 0;

        for(Games g: list){
            String[] namesArr = g.getTeamNames();
            if(namesArr[0].equals(name) || namesArr[1].equals(name)){
                counter += 1;
            }
        }

        return counter;
    }

    public static int[] winsAndLosses(String name, ArrayList<Games> list){
        int totalGames = 0;
        int wins = 0;
        int loss = 0;
        
        for(Games g: list){
            String[] namesArr = g.getTeamNames();
            int[] points = g.getPoints();

            if(!namesArr[0].equals(name) && !namesArr[1].equals(name)){
                continue;
            }

            totalGames += 1;

            if(namesArr[0].equals(name) && points[0] > points[1]){
                wins += 1;
            }else if(namesArr[0].equals(name) && points[0] < points[1]){
                loss += 1;
            }

            if(namesArr[1].equals(name) && points[1] > points[0]){
                wins += 1;
            }else if(namesArr[1].equals(name) && points[1] < points[0]){
                loss += 1;
            }
        }

        int[] stats = {totalGames,wins,loss};
        return stats;
    }


}