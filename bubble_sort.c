#include <stdio.h>

int main(void) {
    int n;

    printf("Dizideki eleman sayisini girin: ");
    scanf("%d", &n);

    int dizi[n];

    printf("%d elemani girin:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &dizi[i]);
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (dizi[j] > dizi[j + 1]) {
                int temp = dizi[j];
                dizi[j] = dizi[j + 1];
                dizi[j + 1] = temp;
            }
        }
    }

    printf("Kucukten buyuge siralanmis dizi:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", dizi[i]);
    }
    printf("\n");

    return 0;
}
