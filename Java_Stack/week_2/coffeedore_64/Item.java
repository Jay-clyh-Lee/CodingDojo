public class Item {
    
        // MEMBER VARIABLES
        private String name;
        private double price;
        
        // CONSTRUCTOR
        public Item(){}

        public Item(String name, double price){
            this.name = name;
            this.price = price;
        }
        
        // GETTERS & SETTERS  - for name and price
        public String getName(){
            return this.name;
        }
        
        public void setName(String name){
            this.name = name;
        }

        public double getPrice(){
            return this.price;
        }
        
        public void setPrice(double price){
            this.price = price;
        }
}
