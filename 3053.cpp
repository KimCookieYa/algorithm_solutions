#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
	double n;
	cin >> n;
	
	double pi = M_PI;
	
	cout.setf(ios::fixed);
	cout.precision(6);
	cout << pi * n * n << '\n';
	cout << 2.0 * n * n;
	
	return 0;
}
