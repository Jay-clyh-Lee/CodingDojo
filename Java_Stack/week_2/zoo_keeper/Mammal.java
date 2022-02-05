public class Mammal {
    
    protected int energyLevel = 100;

    public int displayEnergy() {
        // getter
        System.out.println("Current enery level:" + energyLevel);
        return energyLevel;
    }

    public Mammal(int energyLevel) {
		this.energyLevel = energyLevel;
	}
}
