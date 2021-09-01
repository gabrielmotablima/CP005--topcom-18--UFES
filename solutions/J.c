#include <stdio.h>

int main() {
    int a, b, c, d;
    int X, Y;
    int X_3, Y_3;
    
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    
    
    X = (a+b)*25;
    if (X != 0) X_3 = 30 + (X-10)*2;
    else X_3 = 0;
    
    Y = (c+d)*22;
    if (Y != 0) Y_3 = 48 + (Y-16)*2;
    else Y_3 = 0;
    
    if(Y_3 > X_3) printf("Y Venceu\n");
    else if (Y_3 < X_3) printf("X Venceu\n");
    else printf("Empate\n");
    
    printf("%d-%d\n", X_3, Y_3);
    return 0;
}