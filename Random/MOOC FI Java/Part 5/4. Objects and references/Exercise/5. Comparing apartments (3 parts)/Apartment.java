import java.lang.Math;

public class Apartment {
    private int rooms;
    private int squares;
    private int pricePerSquare;

    public Apartment(int rooms, int squares, int pricePerSquare) {
        this.rooms = rooms;
        this.squares = squares;
        this.pricePerSquare = pricePerSquare;
    }

    public boolean largerThan(Apartment compared){
        if(this.squares > compared.squares){
            return true;
        }

        return false;
    }

    public int priceDifference(Apartment compared){
        int price = this.squares * this.pricePerSquare;
        int comparedPrice = compared.squares * compared.pricePerSquare;

        return Math.round(Math.abs(price - comparedPrice));
    }

    public boolean moreExpensiveThan(Apartment compared){
        int price = this.squares * this.pricePerSquare;
        int comparedPrice = compared.squares * compared.pricePerSquare;

        if(price > comparedPrice){
            return true;
        }

        return false;
    }
}