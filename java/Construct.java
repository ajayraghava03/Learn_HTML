import java.util.*;
public class Construct {
    int x;
    int y;
    //Construct()            //default//
    //{
         System.out.println("A");
    

    Construct(int x,int y)            //default//
    {
        this.x=x;
        this.y=y;
        System.out.println(x+y);
    }

    public static void main(String[] args) 
    {
        int i,b;
        Scanner s= new Scanner(System.in);
        System.out.println("Enter the Length and breadth :");
        i=s.nextInt();
        b=s.nextInt();
       // Construct ba= new Construct();
        Construct a= new Construct(i,b);
        //
       // a.Construct();  
        //ba.Construct(5,6); 
    }
}
