public class Counter{
    private int value;

    public Counter(int startValue){
        this.value = startValue;
    }

    public Counter(){
        this(0);
    }

    public int value(){
        return this.value;
    }

    // Part 1:
    // public void decrease(){
    //     this.value -= 1;
    // }

    // public void increase(){
    //     this.value += 1;
    // }

    // Part 2

    public void decrease(int decreaseBy){
        if(decreaseBy > 0){
            this.value -= decreaseBy;
        }
    }

    public void increase(int increaseBy){
        if(increaseBy > 0){
            this.value += increaseBy;
        }
    }

    
}