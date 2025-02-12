#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int *array, int size);

void printArray(int *array, int size) {
    for (int *p = array; p < array + size; p++) {
        printf("%2d ", *p);
    }
    printf("\n");
}

int main() {
    int list1[] = {5, 3, 8, 4, 2, 7, 1, 6};
    int size1 = sizeof(list1) / sizeof(list1[0]);
    printf("Original list: ");
    printArray(list1, size1);
    bubbleSort(list1, size1);
    printf("Sorted list:   ");
    printArray(list1, size1);
    printf("\n");

    int list2[] = {5, 5, 5, 10, 5};
    int size2 = sizeof(list2) / sizeof(list2[0]);
    printf("Original list: ");
    printArray(list2, size2);
    bubbleSort(list2, size2);
    printf("Sorted list:   ");
    printArray(list2, size2);
    printf("\n");

    int list3[] = {-6, 10, -4, 8, -2, 0};
    int size3 = sizeof(list3) / sizeof(list3[0]);
    printf("Original list: ");
    printArray(list3, size3);
    bubbleSort(list3, size3);
    printf("Sorted list:   ");
    printArray(list3, size3);
    printf("\n");

    int list4[] = {10, 20, 30, 40, 0};
    int size4 = sizeof(list4) / sizeof(list4[0]);
    printf("Original list: ");
    printArray(list4, size4);
    bubbleSort(list4, size4);
    printf("Sorted list:   ");
    printArray(list4, size4);
    printf("\n");

    return 0;
}
