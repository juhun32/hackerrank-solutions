#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(a, b, c, d) {
    int temp1 = 0;
    int temp2 = 0;
    if (a >= b) {
        temp1 = a;
    } else {
        temp1 = b;
    }
    if (c >= d) {
        temp2 = c;
    } else {
        temp2 = d;
    }
    if (temp1 >= temp2) {
        return temp1;
    } else {
        return temp2;
    }
    

}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

