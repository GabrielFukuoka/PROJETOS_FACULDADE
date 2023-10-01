// Gabriel de Ângelo Fukuoka - 32329377
// Kaike Carvalho Machado - 32332130

#include <stdio.h>
#include <math.h>
double calcularValorPolinomio(double coeficientes[], int grau, double x) {
    double resultado = 0.0;
    for (int i = 0; i <= grau; i++) {
        resultado += coeficientes[i] * pow(x, i);
    }
    return resultado;
}

void somarPolinomios(double coef1[], int grau1, double coef2[], int grau2, double resultado[]) {
    int grauResultado = (grau1 > grau2) ? grau1 : grau2;

    for (int i = 0; i <= grauResultado; i++) {
        double termo1 = (i <= grau1) ? coef1[i] : 0;
        double termo2 = (i <= grau2) ? coef2[i] : 0;
        resultado[i] = termo1 + termo2;
    }
}

void multiplicarPolinomios(double coef1[], int grau1, double coef2[], int grau2, double resultado[]) {
    int grauResultado = grau1 + grau2;

    for (int i = 0; i <= grauResultado; i++) {
        resultado[i] = 0;
    }

    for (int i = 0; i <= grau1; i++) {
        for (int j = 0; j <= grau2; j++) {
            resultado[i + j] += coef1[i] * coef2[j];
        }
    }
}

int main() {
    int grau1, grau2;
    printf("Informe o grau do primeiro polinomio: ");
    scanf("%d", &grau1);

    double coef1[grau1 + 1];

    printf("Informe os coeficientes do primeiro polinomio (do maior grau para o menor):\n");
    for (int i = grau1; i >= 0; i--) {
        printf("Coeficiente x^%d: ", i);
        scanf("%lf", &coef1[i]);
    }

    printf("Informe o grau do segundo polinomio: ");
    scanf("%d", &grau2);

    double coef2[grau2 + 1];

    printf("Informe os coeficientes do segundo polinomio (do maior grau para o menor):\n");
    for (int i = grau2; i >= 0; i--) {
        printf("Coeficiente x^%d: ", i);
        scanf("%lf", &coef2[i]);
    }

    int opcao;
    do {
        printf("\nOperacoes disponiveis:\n");
        printf("1. Calcular o valor do primeiro polinomio para um valor de x.\n");
        printf("2. Calcular o valor do segundo polinomio para um valor de x.\n");
        printf("3. Somar dois polinomios.\n");
        printf("4. Multiplicar dois polinomios.\n");
        printf("5. Sair.\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        double x, resultado;
        switch (opcao) {
            case 1: {
                printf("Informe o valor de x: ");
                scanf("%lf", &x);
                resultado = calcularValorPolinomio(coef1, grau1, x);
                printf("Resultado do primeiro polinomio: %.2lf\n", resultado);
                break;
            }
            case 2: {
                printf("Informe o valor de x: ");
                scanf("%lf", &x);
                resultado = calcularValorPolinomio(coef2, grau2, x);
                printf("Resultado do segundo polinomio: %.2lf\n", resultado);
                break;
            }
            case 3: {
                int grauResultadoSoma = (grau1 > grau2) ? grau1 : grau2;
                double resultadoSoma[grauResultadoSoma + 1];
                somarPolinomios(coef1, grau1, coef2, grau2, resultadoSoma);
                printf("Resultado da soma:\n");
                for (int i = grauResultadoSoma; i >= 0; i--) {
                    printf("%.2lfx^%d", resultadoSoma[i], i);
                    if (i > 0) {
                        printf(" + ");
                    }
                }
                printf("\n");
                break;
            }
            case 4: {
                int grauResultadoMultiplicacao = grau1 + grau2;
                double resultadoMultiplicacao[grauResultadoMultiplicacao + 1];
                multiplicarPolinomios(coef1, grau1, coef2, grau2, resultadoMultiplicacao);
                printf("Resultado da multiplicacao:\n");
                for (int i = grauResultadoMultiplicacao; i >= 0; i--) {
                    printf("%.2lfx^%d", resultadoMultiplicacao[i], i);
                    if (i > 0) {
                        printf(" + ");
                    }
                }
                printf("\n");
                break;
            }
            case 5:
                printf("Saindo do programa.\n");
                break;
            default:
                printf("Opcao invalida. Tente novamente.\n");
                break;
        }
    } while (opcao != 5);

    return 0;
}