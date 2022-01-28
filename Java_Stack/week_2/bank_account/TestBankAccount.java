public class TestBankAccount {
    
    public static void main(String[] args) {

        BankAccount PeterPan = new BankAccount();
        System.out.println("Welcome new user");
        PeterPan.depositMoney(1000, 1);
        PeterPan.withDrawMoney(500, 2);
        PeterPan.withDrawMoney(500, 1);
        PeterPan.depositMoney(2000, 2);
        PeterPan.getTotal();

        BankAccount mysteriousUser = new BankAccount();
        System.out.println("Welcome new user");
        mysteriousUser.depositMoney(1000, 1);
        mysteriousUser.depositMoney(5000, 2);
        mysteriousUser.getTotal();
        mysteriousUser.withDrawMoney(777, 1);
        mysteriousUser.withDrawMoney(10000, 2);
        mysteriousUser.withDrawMoney(1000, 2);
        mysteriousUser.getTotal();
    }
}