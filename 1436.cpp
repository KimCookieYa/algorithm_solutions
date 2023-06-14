#include <iostream>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	
	int day = 666;
	for (int i = 2; i <= n; i++) {
		if (n == 1) {
			break;
		}
		
		int cnt = 0;
		while (cnt < 3) {
			cnt = 0;
			day++;
			
			int temp = day;
			while (temp > 0 && cnt < 3) {
				if (temp%10 == 6) {
					cnt++;
				}
				else {
					cnt = 0;
				}
				
				temp = temp/10;
			}
		}
	}
	
	cout << day;
	
	return 0;
}
