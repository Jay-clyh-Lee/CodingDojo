package cafe_business_logic;
import java.util.ArrayList;

public class CafeUtil {

    public Integer getStreakGoal() {
        int sum = 0;
        for (int i = 1; i <= 10; i++){
            sum = sum + i;
        }
        return sum;
    }

    public double getOrderTotal(double[] prices) {
        double total = 0;
        for (int i = 0; i < prices.length; i++){
            total = total + prices[i];
        }
        return total;
    }
    public void displayMenu(ArrayList<String> menuItems) {
        for (int i = 0; i < menuItems.size(); i++) {
            System.out.println(i + " " + menuItems.get(i));
        }
    }

    public void addCustomer(ArrayList<String> customers) {
        String userName = System.console().readLine();
        customers.add(userName);
    }

    public boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> prices) {
        return menuItems.size() == prices.size();
    }

}
    