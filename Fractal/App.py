# app.py
from formas import (
    desenhar_arvore,
    desenhar_koch,
    desenhar_floco,
    desenhar_sierpinski,
    desenhar_mandelbrot
)

def menu():
    while True:
        print("\n🎨 Escolha um fractal para desenhar:")
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
            profundidade = None  # Mandelbrot

        match escolha:
            case "1":
                desenhar_arvore(profundidade)
                break
            case "2":
                desenhar_koch(profundidade)
                break
            case "3":
                desenhar_floco(profundidade)
                break
            case "4":
                desenhar_sierpinski(profundidade)
                break
            case "5":
                desenhar_mandelbrot()
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
    # Executa o menu principal