import java.util.Scanner;

public class Bank {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAcc user1 = new BankAcc("rahul",1001,0);
        System.out.println("Welcome to our Banking System :) ");
        boolean exit = false;
        while (true){
            if (exit) {
                System.out.println("Thanks for using our Bank");
                break;
            }
            System.out.println("Press 1. for Deposit");
            System.out.println("Press 2. for Withdraw");
            System.out.println("Press 3. for Display Account");
            System.out.println("Press 4. for Show Total Accounts Number");
            System.out.println("Press 5. to Exit\n");
            System.out.println("Enter your Choice:- ");
            int choice = scanner.nextInt();
            switch (choice){
                case 1:
                    System.out.println("Enter amount to deposit :- ");
                    int amountdepo = scanner.nextInt();
                    user1.deposit(amountdepo);
                    System.out.println("deposit successfull");
                    break;
                case 2:
                    System.out.println("Enter amount to withdraw :- ");
                    int amountwith = scanner.nextInt();
                    user1.withdraw(amountwith);
                    System.out.println("withdraw successfull");
                    break;
                case 3:
                    user1.showDetails();
                    break;
                case 4:
                    BankAcc.showAccounts();
                    break;
                default:
                    exit = true;
            }
        }
    scanner.close();    
    }
}

class BankAcc {
    static int N_Acc = 0;
    String name;
    int accountId;
    int balance;

    BankAcc(String n,int accid, int bal){
        N_Acc++;
        name = n;
        accountId = accid;
        balance = bal;
    }

    void showDetails(){
        System.out.println("These are your account Details");
        System.out.println("----------------------------------");
        System.out.println("Your name = " + name);
        System.out.println("Your account ID = " + accountId);
        System.out.println("Your account balance = " + balance);
        System.out.println("----------------------------------");
    }

    void deposit(int amount){
        balance += amount;
        System.out.println("Your account credited rupees " + amount);
    }

    void withdraw(int amount){
        balance -= amount;
        System.out.println("Your account deducted rupees " + amount);
    }

    static void showAccounts(){
        System.out.println("These are total number of accounts we have right now: " + N_Acc);
    }
}