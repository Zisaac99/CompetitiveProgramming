public class SimpleDate {
    private int day;
    private int month;
    private int year;

    public SimpleDate(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public String toString() {
        return this.day + "." + this.month + "." + this.year;
    }

    public void advance(){
        this.day += 1;
        
        int daysInAMonth = 30;
        if(this.day > daysInAMonth){
            this.day = 1;
            this.month += 1;

            if(this.month > 12){
                this.year += 1;
            }
        }
    }

    public void advance(int howManyDays){
        int years = howManyDays / 360;
        int monthsInDays = howManyDays % 360;
        int months = monthsInDays / 30;
        int daysLeft = monthsInDays % 30;

        if(years != 0){
            this.year += years;
        }

        if(months != 0){
            this.month += months;

        }
        
        this.day += daysLeft;
        int daysInAMonth = 30;
        if(this.day > daysInAMonth){
            this.day -= daysInAMonth;
            this.month += 1;

            if(this.month > 12){
                this.year += 1;
            }
        }
    }

    public SimpleDate afterNumberOfDays(int days) {
        SimpleDate newDate = new SimpleDate(this.day,this.month,this.year);
        newDate.advance(days);
        return newDate;
    }

    public boolean before(SimpleDate compared) {
        // first compare years
        if (this.year < compared.year) {
            return true;
        }

        // if the years are the same, compare months
        if (this.year == compared.year && this.month < compared.month) {
            return true;
        }

        // the years and the months are the same, compare days
        if (this.year == compared.year && this.month == compared.month &&
            this.day < compared.day) {
            return true;
        }

        return false;
    }
}