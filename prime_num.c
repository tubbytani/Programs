#include<stdio.h>
int main()
{
    int num=100,i,j,counter=0;
     printf("the prime numbers upto 1,00,000 are ");
  
    for(i=1;i<=num;i++)
    { 
        for(j=1;j<(num/2);j++)
        {
                if((i%j)==0)
                counter++;
            
        }
        if(counter==2)
        printf("%d ",i);
    }
   
    return 0;
}
