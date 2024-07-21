#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n;
    int m;
    float j;
    float k;

    scanf("%d %d", &n, &m);
    scanf("%f %f", &j, &k);

    printf("%d %d\n", n + m, n - m);
    printf("%.1f %.1f", j + k, j - k);

    return 0;
}