#include <iostream>

using namespace std;

int main(void) {
	int a[] = {1,1,2,2,2,8};
	int b[6];
	
	for (int i = 0; i < 6; i++) {
		cin >> b[i];
		b[i] = a[i]- b[i];
	}
	
	int i = 0;
	while (i < 6) {
		cout << b[i++] << ' ';
	}
	
	return 0;
}
