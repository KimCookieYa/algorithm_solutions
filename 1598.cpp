#include <iostream>

using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	
	int verticality = (n-1)%4 - (m-1)%4;
	if (verticality < 0) {
		verticality *= -1;
	}
	
	int horizontal = (n-1)/4 - (m-1)/4;
	if (horizontal < 0) {
		horizontal *= -1;
	}
	
	cout << verticality + horizontal;
	
	return 0;
}
