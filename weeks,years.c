#include<stdio.h>
int main()
{int days,years,weeks;
days=1329
years=days/365;
weeks=(days%365)/7;
days=days-((years*365)+(weeks*7))
printf("years:%d/n",years);
prinf("weeks:%d/n",weeks);
printf("days:%d/n"days);
return0;
}
