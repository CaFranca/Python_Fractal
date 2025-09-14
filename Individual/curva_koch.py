import turtle  # Biblioteca que permite desenhar na tela como uma tartaruga
import matplotlib.pyplot as plt  # Biblioteca para gráficos matemáticos
import math  # Biblioteca com funções matemáticas (seno, cosseno, radianos)

def desenhar_koch(profundidade, usar_turtle):
    """
    Desenha a Curva de Koch (fractal famoso).
    
    profundidade → quantas vezes a linha será subdividida
    usar_turtle → True para Turtle (interativo), False para Matplotlib (mais rápido)
    """

    if usar_turtle:
        # --- VERSÃO INTERATIVA COM TURTLE ---
        t = turtle.Turtle()  # Cria a "caneta" para desenhar
        wn = turtle.Screen()  # Cria a janela do desenho
        wn.bgcolor("black")  # Fundo preto
        t.speed("fastest")   # Velocidade máxima da tartaruga
        t.color("white")     # Cor da linha branca

        def koch(length, level):
            """
            Função recursiva que desenha a Curva de Koch.
            
            length → tamanho do segmento atual
            level → nível da recursão
            """
            if level == 0:
                # Caso base: apenas desenha linha reta
                t.forward(length)
            else:
                # Divide o segmento em 4 partes menores
                koch(length / 3, level - 1)  # Primeiro terço
                t.left(60)                   # Vira 60° à esquerda
                koch(length / 3, level - 1)  # Segundo segmento
                t.right(120)                 # Vira 120° à direita
                koch(length / 3, level - 1)  # Terceiro segmento
                t.left(60)                   # Vira 60° à esquerda
                koch(length / 3, level - 1)  # Último segmento

        # Posiciona a tartaruga para começar o desenho
        t.penup()
        t.goto(-150, 0)  # Começa do lado esquerdo da tela
        t.pendown()
        t.hideturtle()   # Esconde a tartaruga para ver apenas o desenho

        # Desenha a linha inicial com tamanho 300 e profundidade escolhida
        koch(300, profundidade)
        wn.exitonclick()  # Fecha a janela quando o usuário clicar

    else:
        # --- VERSÃO RÁPIDA COM MATPLOTLIB ---
        plt.figure(figsize=(8, 4), facecolor="black")  # Cria figura com fundo preto
        ax = plt.gca()  # Obtém eixo da figura para desenhar
        ax.set_facecolor("black")  # Garante fundo preto
        ax.set_aspect("equal")     # Mantém proporções corretas
        ax.axis("off")             # Remove eixos e números

        linhas = []  # Lista para guardar todos os segmentos da curva

        def koch_matplotlib(x1, y1, x2, y2, level):
            """
            Calcula recursivamente os segmentos da Curva de Koch.
            
            (x1, y1) → ponto inicial do segmento
            (x2, y2) → ponto final do segmento
            level → nível de recursão
            """
            if level == 0:
                # Caso base: adiciona linha reta
                linhas.append(((x1, x2), (y1, y2)))
            else:
                # Divide o segmento em 3 partes
                dx = (x2 - x1) / 3
                dy = (y2 - y1) / 3

                # Pontos do segmento
                xA, yA = x1, y1
                xB, yB = x1 + dx, y1 + dy

                # Calcula ponto do vértice do "dente" do fractal
                angulo = math.atan2(y2 - y1, x2 - x1)  # Ângulo da linha
                dist = math.hypot(dx, dy)              # Comprimento do terço
                xC = xB + math.cos(angulo - math.pi / 3) * dist
                yC = yB + math.sin(angulo - math.pi / 3) * dist

                xD, yD = x1 + 2 * dx, y1 + 2 * dy
                xE, yE = x2, y2

                # Chamada recursiva para os 4 segmentos
                koch_matplotlib(xA, yA, xB, yB, level - 1)
                koch_matplotlib(xB, yB, xC, yC, level - 1)
                koch_matplotlib(xC, yC, xD, yD, level - 1)
                koch_matplotlib(xD, yD, xE, yE, level - 1)

        # Desenha a linha inicial
        koch_matplotlib(-150, 0, 150, 0, profundidade)

        # Desenha todas as linhas calculadas
        for linha in linhas:
            ax.plot(linha[0], linha[1], color="white", linewidth=1)

        # Ajusta limites da tela para caber todo o fractal
        ax.set_xlim(-160, 160)
        ax.set_ylim(-100, 100)

        plt.tight_layout()
        plt.show()


# --- Permite rodar sozinho sem app.py ---
if __name__ == "__main__":
    print("Executando Curva de Koch sem app.py")

    # Solicita profundidade da recursão ao usuário
    try:
        profundidade = int(input("Digite a profundidade da recursão (ex: 3 a 6): "))
    except ValueError:
        profundidade = 4
        print("Valor inválido, usando profundidade = 4")

    # Solicita escolha da biblioteca
    metodo = input("Escolha a biblioteca (1 = Turtle, 2 = Matplotlib): ")
    usar_turtle = metodo.strip() == "1"

    desenhar_koch(profundidade, usar_turtle)
