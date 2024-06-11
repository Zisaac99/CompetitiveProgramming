public class Games{
    private String homeTeam;
    private String visitingTeam;
    private int htPoints;
    private int vtPoints;

    public Games(String ht, String vt, int htp, int vtp){
        this.homeTeam = ht;
        this.visitingTeam = vt;
        this.htPoints = htp;
        this.vtPoints = vtp;
    }

    public String[] getTeamNames(){
        String[] teamArr = {this.homeTeam,this.visitingTeam};
        return teamArr;
    }

    public int[] getPoints(){
        int[] pointsArr = {this.htPoints,this.vtPoints};
        return pointsArr;
    }
}