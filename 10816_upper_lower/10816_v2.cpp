// lower bound와 upper bound를 이용하여 숫자카드 개수 출력하기
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int lower_bound(int lst[], int n, int target);
int upper_bound(int lst[], int n, int target);
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
		int ub = upper_bound(nList, n, mList[i]);
		int lb = lower_bound(nList, n, mList[i]);
		int result = ub - lb;
		if (nList[ub] == mList[i]){
			result += 1;
		}
		printf("%d ", result);
		
	}

}


int lower_bound(int lst[], int n, int target){
	int start = 0;
	int end = n - 1;
	while(start <= end){
		if(start == end){
			return start;
		}

		int mid = (start + end) / 2;
		if(lst[mid] < target){
			start = mid + 1;
		}else if(lst[mid] >= target){
			end = mid;
		}
	}
}

int upper_bound(int lst[], int n, int target){
	int start = 0;
	int end = n - 1;
	while(start <= end){
		if(start == end){
			return start;
		}

		int mid = (start + end) / 2;
		if(lst[mid] <= target){
			start = mid + 1;
		}else if(lst[mid] > target){
			end = mid;
		}
	}
}
