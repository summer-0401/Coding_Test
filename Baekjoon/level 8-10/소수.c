#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> //true, false
#include <math.h> //sqrt()
_Bool nums[121];
void eratosthenes()
{
for(int i=0 ; i<=121 ; i++) nums[i] = true; //true로 초기화 후, 합성수 제외
nums[0] = nums[1] = false; //1 제외
int sqrtn = (int)sqrt(120); //√120 > 11 이므로 11까지 순회 (11*11 < 120)
for(int i=2 ; i <= sqrtn ; i++)
{
if(nums[i])
{
for(int j=i*i ; j <= 120 ; j += i) nums[j] = false;
}
}
}

출처: https://snupi.tistory.com/74?category=885572 [SNUPI]