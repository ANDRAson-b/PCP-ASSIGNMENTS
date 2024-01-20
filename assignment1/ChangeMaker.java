package assignment1;

import java.util.Scanner;

public class ChangeMaker {
    public static void main(String[] args) {

        //declering and intializing scanner class 
        Scanner in=new Scanner(System.in);

        //Declaration of variables
        int[] arr=new int[]{0,0,0,0};
        int cents;

        //giving instructions for user about input
        System.out.print("Change Maker \n Enter amount of change to make (1 to 99 cents):");
        
        //asigning the input
        cents=in.nextInt();
        
        //Displaying conformation for entered input  
        System.out.println("\n\nTo make change for "+cents+" cents");

        //proces for spliting cents
        while(cents>0){
            if(cents>=25){
                arr[0]=cents/25;
                cents%=25;
            }else if(cents>=10){
                arr[1]=cents/10;
                cents%=10;
            }else if(cents>=5){
                arr[2]=cents/5;
                cents%=5;
            }else{
                arr[3]=cents;
                cents%=1;
            }
        }

        //Displaying split cents in quarters, dimes, nickels, and pennies
        System.out.println(" "+arr[0]+ " quarters \n "
                            +arr[1]+ " dimes\n "
                            +arr[2]+ " nickels\n "
                            +arr[3]+ " pennies");

        //closing scanner
        in.close();
    }
    
}
