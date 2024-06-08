public class Statistics{
    private int count;
    private int sum;
    
    public Statistics(){
        this.count = 0;
        this.sum = 0;
    }

    public void addNumber(int number){
        this.sum += number;
        this.count += 1;
    }

    public int getCount(){
        return this.count;
    }

    public int sum() {
        return this.sum;
    }

    public double average() {
        return (1.0 * this.sum) / this.count;
    }
}