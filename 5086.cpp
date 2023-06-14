#include <bits/stdc++.h>

using namespace std;

int main(void) {
	while (1) {
		int a, b;
		cin >> a >> b;
		if (a == 0 && b == 0) {
			break;
		}
		
		if (a%b == 0 && a > b) {
			cout << "multiple\n";
		}
		else if (b%a == 0 && a < b) {
			cout << "factor\n";
		}
		else {
			cout << "neither\n";
		}
	}
	
	return 0;
}
