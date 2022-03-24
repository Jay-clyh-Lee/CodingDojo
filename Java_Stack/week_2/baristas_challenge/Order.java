import java.util.ArrayList;

public class Order {

    private String name;
    private boolean ready;
    private ArrayList<Item> items = new ArrayList<Item>();

    public Order(){
        this.name = "guest";
        this.ready = false;
    }

    public Order(String name){
        this.name = name;
        this.ready = false;
    }

    public String getName(){
        return this.name;
    }

    public boolean getReady(){
        return this.ready;
    }

    public ArrayList<Item> getItems(){
        return this.items;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setReady(boolean ready){
        this.ready = ready;
    }

    public void setItems(ArrayList<Item> items){
        this.items = items;
    }

    public void addItem(Item item){
        items.add(item);
    }

    public void getStatusMessage(){
        if (ready == true){
            System.out.println("Your order is ready.");
        }
        else {
            System.out.println("Thank you for waiting. Your order will be ready soon.");
        }
    }

    // public double getOrderTotal(){
    //     double total = 0;
    //     for (int i=0; i<items.size(); i++){
    //         total += items.get(i).price;
    //     }
    // }

    public double getOrderTotal(){
        double total = 0.0;
        for(Item i: this.items) {
            total += i.getPrice();
        }
        return total;
    }

    // public String display(){
    //     System.out.println("Customer name: %s", name);
    //     for (int i=0; i<items.length; i++){
    //         System.out.println("%s", items[i].name, " - $%d", items[i].price);
    //     }
    //     System.out.println("Total: %d", total);
    // }
    
    public void display(){
        System.out.println("Customer Name: " + this.name);
        for(Item i: this.items) {
            System.out.println(i.getName() + " - $" + i.getPrice());
        }
        System.out.println("Total: $" + this.getOrderTotal() + "\n");
    }

}