public class Clock{
    private ClockHand seconds;
    private ClockHand minutes;
    private ClockHand hours;

    public Clock(){
        this.seconds = new ClockHand(60);
        this.minutes = new ClockHand(60);
        this.hours = new ClockHand(24);
    }

    public void advance(){
        this.seconds.advance();

        if(this.seconds.value() == 0){
            this.minutes.advance();

            if(this.minutes.value() == 0){
                this.hours.advance();
            }
        }
    }

    @Override 
    public String toString(){
        return this.hours + ":" + this.minutes + ":" + this.seconds;
    }
}