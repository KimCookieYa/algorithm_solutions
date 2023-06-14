#include <iostream>

using namespace std;

int get_gcd(int a, int b) {
	while (b != 0) {
		int r = a%b;
		a = b;
		b = r;
	}
	
	return a;
}

int main(void) {
	int n;
	cin >> n;
	
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	
	for (int i = 1; i < n; i++) {
		int temp = get_gcd(a[0], a[i]);
		cout << a[0] / temp << '/' << a[i] / temp << endl;
	}
	
	return 0;
}
