#include <iostream>

using namespace std;

int main(void) {
	long long l, p;
	cin >> l >> p;
	
	int a[5];
	for (int i = 0; i < 5; i++) {
		cin >> a[i];
		a[i] = a[i] - l*p;
	}
	
	for (int i = 0; i < 5; i++) {
		cout << a[i] << ' ';
	}
	
	return 0;
}
