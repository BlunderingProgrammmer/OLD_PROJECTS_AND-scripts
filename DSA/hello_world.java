import java.util.*;

public class hello_world {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        String opereation = sc.next();
        int result =  0;

        switch (opereation) {
            case + :result = a+b;
            System.out.println(result);
            break;
            case - :result = a-b;
            System.out.println(result);
            break;
            case * :result = a*b;
            System.out.println(result);
            break;
            case / :result = a/b;
            System.out.println(result);
            break;
            default:System.out.println("invalid operation");
            break;
        }





    


    }
}
