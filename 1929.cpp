#include <iostream>

using namespace std;

int main(void) {
	int m, n;
	cin >> m >> n;
	
	bool arr[1000001] = {true, true, };
	for (int i = 2; i <= n; i++) {
		if (arr[i] == false) {
			for (int j = 2; i * j <= n; j++) {
				arr[i*j] = true;
			}
			
			if (m <= i && i <= n) {
				cout << i << '\n';
			}
			else if (i > n) {
				break;
			}
		}
	}
	
	return 0;
}
