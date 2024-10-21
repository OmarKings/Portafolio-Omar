#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main() {
    char cve[6];
    char nom[21];
    int pre;

    while (true) {
        printf("Indica la clave del producto :");
        gets(cve);

        if (strlen(cve) > 5) {
            printf("Error , clave no más de 5 caracteres\n");
        } else {
            break;
        }
    }

    while (true) {
        printf("Indica el nombre del producto :");
        gets(nom);

        if (strlen(nom) > 20) {
            printf("Error , nombre no más de 20 caracteres\n");
        } else {
            break;
        }
    }

    while (true) {
        printf("Indica el precio del producto: ");
        gets(pre);
        if (pre >= 1 && pre <= 9999) {
            break;
        } else {
            printf("Error , precio no está en el rango de 1 a 9999\n");
        }
    }

    ofstream arch;
    arch.open("Productos.csv", ios::app);
    arch << cve << "," << nom << "," << pre << "\n";
    arch.close();

    return 0;
}
