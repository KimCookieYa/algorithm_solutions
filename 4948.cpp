#include <iostream>

using namespace std;

int main(void) {
	int num = 123456 * 2 + 1;
	
	bool arr[num] = {true, true, };
	for (int i = 2; i <= num/2; i++) {
		if (arr[i] == false) {
			for (int j = 2; i * j <= num-1; j++) {
				arr[i*j] = true;
			}
		}
	}
	
	int n;
	while (1) {
		cin >> n;
		
		if (n == 0) {
			break;
		}
		
		int cnt = 0;
		for (int i = n+1; i <= 2*n; i++) {
			if (arr[i] == false) {
				cnt++;
			}
		}
		
		cout << cnt << '\n';
	}
	
	return 0;
}
