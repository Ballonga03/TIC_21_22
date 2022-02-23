#include<stdio.h>

int main(){
	char letras[5];
	int cont;
	
	
	//Leo datos del teclado
	for(cont=0;cont<5;cont++){
		printf("Introduce la letra %d: ",cont);
		scanf(" %c" ,&letras[cont]);
		
	}
	//ESCRIBO datos en la pantalla
	printf("\nHAS ESCREITO LA PALABRA: ");
	for(cont=0;cont<5;cont++){
		printf("&c" ,letras[cont]);
	}
	
	
	
	
	return(0);
}
