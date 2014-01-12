#include <stdio.h>


/*


The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

*/

int sum_of_squares(int num)
{
	int sum = 0;
	int i;
	
	for(i = 1; i < num + 1; i++) {
		sum += i * i;
    }
    return sum;
}
     
     
int square_of_sums(int num)
{
	int sum = 0, i;
    
    for(i = 1; i < num + 1; i++) {
        sum += i;
	}
	return sum * sum;
}


int main()
{
    printf("\n square_of_sums(100) - sum_of_squares(100) = %d\n",
           square_of_sums(100) - sum_of_squares(100));

}
