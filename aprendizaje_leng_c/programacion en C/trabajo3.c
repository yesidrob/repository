#include <stdio.h>
int main() {

    float peso, altura, imc;
    printf("ingrese su peso: ");
    scanf("%f",&peso);


    printf("ingrese su altura: ");
    scanf("%f",&altura);

    imc = peso / (altura * altura);

    if (imc < 18.5) {
        printf("El peso esta por debajo de lo normal");  
    }  else if ((imc >= 18.5) && (imc < 25))  {//18.5 <= imc <25000
        printf("tiene un peso saludable");
    }  else if ((imc >= 25) && (imc < 30))  {
        printf("tiene sobrepeso");
    } else if (imc >= 30) {
        printf("Tiene obesidad");
    }



return 0;

}