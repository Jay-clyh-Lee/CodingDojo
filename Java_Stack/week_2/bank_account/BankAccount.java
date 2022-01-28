public class BankAccount {

    public static int numberOfAccounts;
    public double totalAmount = 0;

    private double checkingBalance;
    private double savingsBalance;

    public BankAccount() {
        BankAccount.numberOfAccounts += 1;
        this.checkingBalance = 0;
        this.savingsBalance = 0;
    }

    public double getCheckingBalance() {
        return this.checkingBalance;
    }

    public double getSavingsBalance() {
        return this.savingsBalance;
    }

    public void depositMoney(double amount, int account) {
        if (amount > 0) {
            if (account == 1) {
                this.checkingBalance += amount;
            }
            if (account == 2) {
                this.savingsBalance += amount;
            }
        } else {
            System.out.println("cannot deposit negative amount.");
        }
    }

    public void withDrawMoney(double amount, int account) {
        if (account == 1) {
            if (this.checkingBalance > amount) {
                this.checkingBalance = this.checkingBalance - amount;
            } else {
                System.out.println("Not enough money in checking account.");
            }
        } else if (account == 2) {
            if (this.savingsBalance > amount) {
                this.savingsBalance = this.savingsBalance - amount;
            } else {
                System.out.println("Not enough money in savings account.");
            }
        } else {
            System.out.println("Enter only 1 or 2; 1 for checking account and 2 for savings account.");
        }
    }

    public void getTotal() {
        System.out.println(String.format("Savings: %.2f, Checking: %.2f", this.savingsBalance, this.checkingBalance));
    }

}