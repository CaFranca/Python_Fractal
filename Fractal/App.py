# app.py
#pip install matplotlib
#pip install numpy
#pip install turtle

from formas import (
    desenhar_arvore,
    desenhar_koch,
    desenhar_floco,
    desenhar_sierpinski,
    desenhar_mandelbrot,
)

def menu():
    print("Bem-vindo ao Gerador de Fractais!")

    while True:
        print("\nEscolha a biblioteca para desenhar:")
        print("1 - turtle (mais lento, modo gráfico simples)")
        print("2 - matplotlib (mathlib) - mais rápido, visual moderno")
        metodo = input("Digite 1 ou 2: ")

        if metodo not in ["1", "2"]:
            print("❌ Opção inválida. Tente novamente.")
            continue
        break

    usar_turtle = metodo == "1"

    while True:
        print("\nEscolha um fractal para desenhar:")
        print("1 - Árvore Fractal")
        print("2 - Curva de Koch")
        print("3 - Floco de Neve")
        print("4 - Triângulo de Sierpinski")
        print("5 - Conjunto de Mandelbrot")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "0":
            print("Encerrando o programa.")
            break

        if escolha in ["1", "2", "3", "4"]:
            try:
                profundidade = int(input("Digite a profundidade da recursão (ex: 4 a 8): "))
            except ValueError:
                print("❌ Valor inválido. Digite um número inteiro.")
                continue
        else:
            profundidade = None

        nomes = {
            "1": "Árvore Fractal",
            "2": "Curva de Koch",
            "3": "Floco de Neve",
            "4": "Triângulo de Sierpinski",
            "5": "Conjunto de Mandelbrot",
        }
        fractal_nome = nomes.get(escolha, "Fractal")

        print(f"\nDesenhando {fractal_nome}...")

        match escolha:
            case "1":
                desenhar_arvore(profundidade, usar_turtle)
                print(f"{fractal_nome} desenhado!\n")
                break
            case "2":
                desenhar_koch(profundidade, usar_turtle)
                print(f"{fractal_nome} desenhado!\n")
                break
            case "3":
                desenhar_floco(profundidade, usar_turtle)
                print(f"{fractal_nome} desenhado!\n")
                break
            case "4":
                desenhar_sierpinski(profundidade, usar_turtle)
                print(f"{fractal_nome} desenhado!\n")
                break
            case "5":
                desenhar_mandelbrot(usar_turtle)
                print(f"{fractal_nome} desenhado!\n")
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")
                print(f"{fractal_nome} desenhado!\n")
                continue


if __name__ == "__main__":
    menu()
