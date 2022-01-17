package cafe_business_logic;
import java.util.ArrayList;
public class CafeUtil {

    public Integer getStreakGoal(Integer numWeeks) {
        int sum = 0;
        for (int i = 1; i < numWeeks; i++){
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
            System.out.println(menuItems.get(i));
        }
    }

    public String greetSpanish(String name) {
        return "Hola, " + name;
        
    }
}
    