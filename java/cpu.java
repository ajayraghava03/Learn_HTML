public class cpu {
    double price;
    class processor
    {
        double core;
        String manufacture;
        processor(double core,String manufacture)
        {
            this.core=core;
            this.manufacture=manufacture;

        }
        double getcache()
        {
            return this.core;
        }

    }
    class RAM
    {
        double memory;
        String manufacture;
        RAM(double memory,String manufacture)
        {
            this.memory=memory;
            this.manufacture=manufacture;
        }
        double getspeed()
        {
            return this.memory;
        }
    }
}
