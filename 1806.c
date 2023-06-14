#include <stdio.h>

int main(void) {
	int n, m, start, end;
	int i, j;
	int a[100000];
	long long min = 10000*100000, sum;
	
	scanf_s("%d", &n, sizeof(n));
	scanf_s("%d", &m, sizeof(m));
	
	for (i = 0; i < n; i++) {
		scanf_s("%d", &a[i], sizeof(int));
	}
	
	for (i = 0; i < n; i++) {
		sum = 0;
		
		start = i;
		end;
		for (j = i; j < n && sum < m; j++) {
			sum += a[j];
			end = j;
		}
		
		if (sum == m && min > end-start+1) {
			min = end-start+1;
		}
	}
	
	if (min == 10000*100000)
		printf("0");
	else
		printf("%d", min);
	
	return 0;
}
