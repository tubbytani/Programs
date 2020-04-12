#include<stdio.h>
int main()
{
    int num=100000,i,j;
     printf("the prime numbers upto 1,00,000 are ");
  
    for(i=1;i<=num;i++)
    { 
        int counter=0;
        for(j=1;j<num;j++)
        {
                if((i%j)==0)
                counter++;
            
        }
        if(counter==2)
        printf("%d ",i);
    }
   
   
    return 0;
}
