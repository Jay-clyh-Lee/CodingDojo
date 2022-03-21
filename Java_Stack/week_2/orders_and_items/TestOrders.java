import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args) {
    
        Order order1 = new Order();
        order1.name = "Mocha Latte";
        order1.total = 10;
        order1.ready = true;

        System.out.printf("Name: %s\n", order1.name);
        System.out.printf("Total: %s\n", order1.total);
        System.out.printf("Ready: %s\n", order1.ready);
    }
}
