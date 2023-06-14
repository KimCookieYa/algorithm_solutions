#include <iostream>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	int op = 2;
	while (n != 1) {
		if (n%op == 0) {
			n = n/op;
			cout << op << endl;
		}
		else {
			op++;
		}
	}
	
	return 0;
}
