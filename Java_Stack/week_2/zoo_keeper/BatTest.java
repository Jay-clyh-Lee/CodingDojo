public class BatTest {
    
    public static void main(String[] args){
        Bat Dracula = new Bat();
        Dracula.displayEnergy();
        for (int i = 0; i < 3; i++){
            Dracula.attackTown();
        }
        for (int i = 0; i < 2; i++){
            Dracula.eatHumans();
        }
        Dracula.displayEnergy();
    }
}
