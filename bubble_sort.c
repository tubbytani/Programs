
 
#include <stdio.h>
#include<math.h>
int main()
{
    int q[10],p,temp;
    int i,j,k;
	printf("enter 10 numbers \n");
	for(i=0;i<10;i++)
	scanf("%d",&q[i]);
	//bubble sort
	for(i=0;i<10;i++)
	{
	for(j=(i+1);j<10;j++)
	{
	if(q[j]>q[i])
	{  
	    temp=q[i];
	    q[i]=q[j];
	    q[j]=temp;
	}
	}
	}
	printf("the sorted numbers in descending order are:");
	for(i=0;i<10;i++)
	{printf("%d",q[i]);}
    return 0;
}
