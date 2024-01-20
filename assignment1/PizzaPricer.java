package assignment1;

import java.util.Scanner;

public class PizzaPricer {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        
        int diameter=0;
        int cents;
        int people;
        double dollers;
        double area;
        double centsPerSquareInch;
        double tip;
        double cost;
        double costPerPerson;


        System.out.println("Pizza Pricer\n Enter diametermeter of pizza (inches): ");
        diameter=in.nextInt();
        System.out.println("Enter cost of pizza (dollars) : ");
        dollers=in.nextDouble();

        cents=(int)(dollers*100);
        area=Math.PI*diameter*diameter*0.25;
        people=(int)area/50;
        centsPerSquareInch=cents/area;
        cost=dollers/people;
        tip=0.15*cost;
        costPerPerson=cost+tip;

        System.out.println("\n This pizza " +people+" people");
        System.out.println("  cents/square inch\t ="+ centsPerSquareInch);
        System.out.println("  cost/person\t = "+ costPerPerson+ " dollers (includes a 15% tip)");

        in.close();
    }
}
