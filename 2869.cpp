#include <iostream>

using namespace std;

int main(void) {
	long long a,b,v;
	cin >> a >> b >> v;
	
	double temp = (v-a) / (double)(a-b);
	temp = temp - (long long)temp;
	
	long long day = 1;
	if (temp > 0)
		day++;
	
	day += ((v-a) / (a-b)); 
	
	cout << day;
	
	return 0;
}
