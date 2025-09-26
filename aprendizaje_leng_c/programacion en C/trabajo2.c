#include <stdio.h>
int main() {

char letra;
printf("ingrese una letra");
scanf("%c",&letra);
switch (letra)
{
case 'a':
    prinf("es una vocal");
    break;
case 'e':
     prinf("es una vocal");     
    break;
case 'i':
     prinf("es una vocal");
    break;

case 'o':
     prinf("es una vocal");
    break;

case 'u':
     prinf("es una vocal");
    break;


default:
    printf("es una consonante");
    break;
}
}