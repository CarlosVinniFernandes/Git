import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        
        int num1 = Integer.parseInt(sc.nextLine());
        double num2 = sc.nextDouble();
        sc.nextLine();
        String palavra1 = sc.nextLine();
        
        System.out.println("String: " + palavra1);
        System.out.println("Double: " + num2);
        System.out.println("Int: " + num1);
        
    }
}
