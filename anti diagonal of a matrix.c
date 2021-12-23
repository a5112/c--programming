#include<stdio.h>
int main()
{
int i,j,A[3][3],sum=0;
{
for(i=0;i<3;i++)
{
	for(j=0;j<3;j++)
{
	scanf("%d",&A[i][j]);
}
}
for(i=0;i<3;i++)
{
	for(j=0;j<3;j++)
	if(i+j==2)
	{
		sum=sum+A[j][i];
	}}
	printf("som of matrix of a anti diagonals%d",sum);

}
}
