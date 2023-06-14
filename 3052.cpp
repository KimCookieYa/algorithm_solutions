#include <iostream>

using namespace std;

int main(void) {
	int p = 42;
	int n = 10;
	int numbers[n];
	
	int memory[p];
	for (int i = 0; i < p; i++)
		memory[i] = false;
		
	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
		a[i] = numbers[i] % p;
		if (memory[numbers[i]] == false)
			memory[numbers[i]] = true;
	}
	
	int num = 0;
	for (int i = 0; i < p; i++)
		if (memory[i] == true)
			num++;
	
	cout << num;
	return 0;
}
