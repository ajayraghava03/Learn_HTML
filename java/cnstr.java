class th extends Thread
{
    public void run()
    {
        System.out.println("code in th");
    }
}


class cnstr 
{
    th a = new th();
     //not working//
    try
    {
        th.sleep(1000);
    }
    catch(Exception e)
    {
        System.out.println(e.toString());
    }


}
