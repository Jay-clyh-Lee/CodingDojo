class Gorilla extends Mammal {
    
    public void throwSomething() {
        System.out.println("The gorilla threw something");
        energyLevel -= 5;
    }

    public void eatBananas() {
        System.out.println("The gorilla is eating bananas");
        energyLevel += 10;
    }

    public void climb() {
        System.out.println("The gorilla is climbing");
        energyLevel -= 10;
    }
    
}