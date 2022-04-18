import java.util.ArrayList;

public class OrderKiosk {

    // ATTRIBUTES/MEMBER VARIABLES
    ArrayList<Item> menu = new ArrayList<Item>();
    ArrayList<Order> orders = new ArrayList<Order>();

    // CONSTRUCTOR
    pubic OrderKiosk(){}

    public void addMenuItem(String name, double price){
        menu.add(name, price);
    }


}