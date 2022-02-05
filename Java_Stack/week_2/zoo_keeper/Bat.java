public class Bat extends Mammal {
    
   //This does not work if overload Mammal class.
    public Bat(int energyLevel) {
        super(energyLevel);
    }

    public void fly() {
        System.out.println("The bat is flying around!");
        energyLevel -= 50;
    }

    public void eatHumans() {
        System.out.println("The bat is eatin... well, never mind!");
        energyLevel += 25;
    }

    public void attackTown() {
        System.out.println("Crackling sound in bat.");
        energyLevel -= 10;
    }

}