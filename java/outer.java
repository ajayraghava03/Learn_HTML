class outer {
    static class inner
    {
        public int sum(int a,int b)
        {
            
            System.out.println("a+b is ");

            return a+b;
        }
    }
    public static void main(String[] args) {
        int res;
        outer.inner oi=new outer.inner();
            res=oi.sum(5,10);
            System.out.println(res);

    }
}

