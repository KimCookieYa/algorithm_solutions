#include <iostream>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	bool arr[1001] = {true, true, };
	for (int i = 1; i <= 1000; i++) {
		if (arr[i] == false) {
			for (int j = 2; i * j <= 1000; j++) {
				arr[i*j] = true;
			}
		} 
	}
	
	int cnt = 0;
	int a[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		
		if (arr[a[i]] == false) {
			cnt++;
		}
	}
	
	cout << cnt;
	
	return 0;
}
