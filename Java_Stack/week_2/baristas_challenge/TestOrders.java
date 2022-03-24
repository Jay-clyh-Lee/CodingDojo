import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args) {
        
        // Menu items
        Item item1 = new Item();
        item1.setName("mocha");
        item1.setPrice(3.25);

        Item item2 = new Item();
        item2.setName("latte");
        item2.setPrice(4.5);

        Item item3 = new Item();
        item2.setName("drip coffee");
        item2.setPrice(2.15);

        Item item4 = new Item();
        item2.setName("capuccino");
        item2.setPrice(3.5);

        // Orders
        Order order1 = new Order();
        order1.addItem(item1);
        order1.addItem(item2);

        Order order2 = new Order();
        order2.addItem(item1);
        order2.addItem(item3);

        Order order3 = new Order("Noah");
        order3.addItem(item2);
        order3.addItem(item3);
        
        Order order4 = new Order("Nova");
        order4.addItem(item1);
        order4.addItem(item1);

        Order order5 = new Order("Nolan");
        order5.addItem(item2);
        order5.addItem(item2);

        // Application Simulations

        order1.display();
        order2.display();
        order3.display();
        order4.display();
        order5.display();
    }

}
