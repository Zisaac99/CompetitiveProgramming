public class Money {

    private final int euros;
    private final int cents;

    public Money(int euros, int cents) {
        this.euros = euros;
        this.cents = cents;
    }

    public int euros() {
        return euros;
    }

    public int cents() {
        return cents;
    }

    public Money plus(Money addition){
        int newCents = this.cents + addition.cents;
        int extraEuros = newCents / 100;
        newCents = newCents % 100;

        int newEuros =  this.euros + addition.euros + extraEuros;

        Money newMoney = new Money(newEuros, newCents);
        return newMoney;
    }

    public boolean lessThan(Money compared){
        if(this.euros < compared.euros){
            return true;
        }

        if(this.euros == compared.euros && this.cents < compared.cents){
            return true;
        }

        return false;
    }

    public Money minus(Money decreaser){
        int newCents = 0;
        int newEuros = 0;
        if(this.lessThan(decreaser)){
            newCents = decreaser.cents - this.cents;

            if(newCents % 100 > 0){
                newEuros += newCents / 100;
                newCents = newCents % 100;
            }

            if(newCents < 0){
                newCents += 100;
                newEuros -= 1;
            }

            newEuros += decreaser.euros - this.euros;
            newEuros *= -1;
        }else{
            newCents = this.cents - decreaser.cents;

            if(newCents % 100 > 0){
                newEuros += newCents / 100;
                newCents = newCents % 100;
            }

            if(newCents < 0){
                newCents += 100;
                newEuros -= 1;
            }

            newEuros += this.euros - decreaser.euros;
        }

        Money newMoney = new Money(newEuros,newCents);
        return newMoney;
    }

    public String toString() {
        String zero = "";
        if (cents <= 10) {
            zero = "0";
        }

        return euros + "." + zero + cents + "e";
    }
}