class student
{
    int rollno;         // global variable //
    String name;
    float fee;

    public student(int rollno,String name,float fee )   // constructer//
    {
        this.rollno=rollno;
        this.name=name;
        this.fee=fee;
    }

    public void disp()
    {
        System.out.println(rollno+name+fee);
    }

    public static void main()
    {
        student s=new student(5, "k", 5000);
        s.disp();
    }
}