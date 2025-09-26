#include <stdio.h>
int main() {
    float examen1, examen2;
    printf("ingrese la nota del primer examen: ");
    scanf("%f",&examen1);
    printf("ingrese la nota del segundo examen: ");
    scanf("%f",&examen2);
    float notaFinal;
    notaFinal = (examen1 + examen2) / 2;
    printf("La nota final es: %f", notaFinal);
    

/*Escriba un programa en el que se pida ingresar numero entre 1 y 7 
segun el numero elegido va a representar un dia de la semana*/
  int dia;
  printf("ingrese un numero(el num representa un dia):");
  scanf("%d",&dia);
  switch (dia)
  {
  case 1:
    printf("Hoy es dia LUNES");
    break;
  case 2:
    printf("Hoy es dia MARTES");
    break;
  case 3:
    printf("Hoy es dia MIERCOLES");
    break;
   case 4:
    printf("Hoy es dia JUEVES");
    break;
   case 5:
    printf("Hoy es dia VIERNES");
    break;
   case 6:
    printf("Hoy es dia SABADO");
    break;
    
  default:
    printf("Hoy es DOMINGO");
    break;
  }
    return 0;
}