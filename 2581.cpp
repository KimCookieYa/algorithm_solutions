#include <iostream>

using namespace std;

int main(void) {
	int m, n;
	cin >> m >> n;
	
	bool arr[10001] = {true, true, };
	for (int i = 1; i <= 10000; i++) {
		if (arr[i] == false) {
			for (int j = 2; i * j <= 10000; j++) {
				arr[i*j] = true;
			}
		} 
	}
	
	int sum = 0;
	int min = 10001;
	for (int i = m; i <= n; i++) {
		if (arr[i] == false) {
			sum += i;
			
			if (min > i) {
				min = i;
			}
		}
	}
	
	if (sum != 0) {
		cout << sum << endl << min;
	}
	else {
		cout << -1;
	}
	
	return 0;
}
