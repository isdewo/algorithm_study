// 피타고라스의 정리
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int main(){
    int a, b, c;
    int num = 0;
    char buf[1024] = "";
    while(scanf("%d %d %d", &a, &b, &c) == 3){
        if (a == 0 && b == 0 && c == 0){
            break;
        }
        num += 1;
        
        int left = 0;
        int right = 0;

        if (a >= b && a >= c){
            left = a*a;
            right = b*b + c*c;
        }else if (b >= c && b >= a){
            left = b*b;
            right = a*a + c*c;
        }else if (c >= a && c >= b){
            left = c*c;
            right = a*a + b*b;
        }


        if (left == right){
            strcat(buf, "right\n");
        }else{
            strcat(buf, "wrong\n");
        }

    }
    printf("%s", buf);

}
