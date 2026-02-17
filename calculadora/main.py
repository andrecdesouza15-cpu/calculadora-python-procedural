import math

def adicao(numero_a, numero_b):
    return numero_a + numero_b

def subtracao(numero_a, numero_b):
    return numero_a - numero_b

def multiplicacao(numero_a, numero_b):
    return numero_a * numero_b

def divisao(numero_a, numero_b):
    if numero_b == 0:
        raise ValueError("Erro: Divisão por zero não permitida")
    return numero_a / numero_b

def potencia(numero_a, numero_b):
    return numero_a ** numero_b

def raiz_quadrada(radicando):
    if radicando < 0:
        raise ValueError("Erro: Raíz quadrada de números negativos não permitida")
    return math.sqrt(radicando)

def linha():
    print("----------------------------")

def mostrar_erro_digitacao():
    print("----------------------------")
    print("Entrada inválida. Digite apenas números.")

def listar_historico(historico):
    if not historico:
        linha()
        print("Histórico inexistente ou vazio")
    else:
        linha()
        print("Histórico de Cálculos:\n")
        for calculo in historico:
            print(calculo)

def main():
    historico = []
    operacoes = {
        1: ("Adição", "+", adicao),
        2: ("Subtração", "-", subtracao),
        3: ("Multiplicação", "*", multiplicacao),
        4: ("Divisão", "/", divisao),
        5: ("Potência", "**", potencia),
        6: ("Raiz Quadrada", "√", raiz_quadrada)
    }

    while True:
        linha()
        print("APP Calculadora")
        print("1. Efetuar cálculos")
        print("2. Consultar histórico de cálculos")
        print("0. Encerrar o programa")
        try:
            opcao = int(input("\nDigite sua opção: "))
        except ValueError:
            mostrar_erro_digitacao()
            continue
        if opcao == 1:
            linha()
            print("Qual operação deseja realizar?")
            print("1. Adição | 2. Subtração | 3. Multiplicação")
            print("4. Divisão | 5. Potência | 6. Raiz Quadrada")
            print("0. Retornar ao menu principal")
            try:
                opcao_calculo = int(input("Digite a sua opção de cálculo: "))
            except ValueError:
                mostrar_erro_digitacao()
                continue

            if opcao_calculo in [1, 2, 3, 4, 5, 6]:
                try:
                    linha()

                    nome, simbolo, funcao_calc = operacoes[opcao_calculo]

                    if opcao_calculo == 6:
                        radicando = float(input("Digite o radicando: "))
                        resultado = funcao_calc(radicando)
                        frase = f"{nome}: {simbolo}{radicando} = {resultado}"

                    else:
                        primeiro_numero = float(input("Digite o primeiro número: "))
                        segundo_numero = float(input("Digite o segundo número: "))
                        resultado = funcao_calc(primeiro_numero, segundo_numero)
                        frase = f"{nome}: {primeiro_numero} {simbolo} {segundo_numero} = {resultado}"

                    linha()
                    print(frase)
                    historico.append(frase)

                except ValueError as erro:
                    if "Erro" in str(erro):
                        linha()
                        print(erro)
                    else:
                        mostrar_erro_digitacao()
                        continue

            elif opcao_calculo == 0:
                continue
            else:
                linha()
                print("Opção inválida! Tente novamente.")

        elif opcao == 2:
            listar_historico(historico)

        elif opcao == 0:
            print("Encerrando...")
            break

        else:
            linha()
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()