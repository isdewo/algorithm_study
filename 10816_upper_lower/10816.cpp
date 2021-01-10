// upper bound와 lower bound를 이용하여 숫자카드 개수 출력하기
// 내장함수 이용
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
	int n, m;

	scanf("%d", &n);
	int *nList;
	nList = (int*)malloc(sizeof(int)*n);
	for(int i = 0; i < n; i++){
		scanf("%d", &nList[i]);
	}

	scanf("%d", &m);
	int *mList;
	mList = (int*)malloc(sizeof(int)*m);
	for(int i = 0; i < m; i++){
		scanf("%d", &mList[i]);
	}

	sort(nList, nList+n);
	
	for(int i = 0; i < m; i++){
		int ub = upper_bound(nList, nList + n, mList[i]) - nList;
		int lb = lower_bound(nList, nList + n, mList[i]) - nList;
		int result = ub - lb;
		if (nList[ub] == mList[i]){
			result += 1;
		}
		printf("%d ", result);
		
	}

}
