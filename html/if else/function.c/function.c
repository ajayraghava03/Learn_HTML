#include<stdio.h>

int main()
{
    int i,j;
    int a[2][3] ={1,2,3,4,5};
    
    printf(" 2D array \n");
    
    for(i=0;i<2;i++)
    {
        for(j=0;j<3;j++)
        {
            printf("%3d",a[i][j]);
        }
        printf("\n");
    }

    return(0);
}