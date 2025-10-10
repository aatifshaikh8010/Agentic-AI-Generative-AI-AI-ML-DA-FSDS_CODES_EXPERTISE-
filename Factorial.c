#include<stdio.h>
void main()
{
    int x=1,n,s=1;
   printf("\n Enter any Number =")
   scanf("%d",&n);
   while(x<=n)
  {
    s=s+x;
    x++;
  }
  printf("\n Factorial=%d",s);
}  
