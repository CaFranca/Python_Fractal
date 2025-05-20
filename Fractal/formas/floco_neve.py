import turtle  # Biblioteca para desenho gráfico
import matplotlib.pyplot as plt  # Biblioteca para gráficos com mathlib
import math  # Funções trigonométricas para matplotlib

def desenhar_floco(profundidade, usar_turtle):
    if usar_turtle:
        t = turtle.Turtle()  # Cria a "caneta" para desenhar
        wn = turtle.Screen()  # Cria a janela do desenho
        wn.bgcolor("black")   # Define o fundo preto
        t.speed("fastest")    # Define a velocidade máxima do desenho
        t.color("white")      # Define a cor da linha como branca

        # Função recursiva que desenha um segmento da curva de Koch
        def koch(length, level):
            if level == 0:  # Caso base: desenha linha reta
                t.forward(length)
            else:
                # Desenha os 4 segmentos recursivamente, formando o padrão fractal
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)
                t.right(120)
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)

        t.penup()
        t.goto(-150, 100)  # Posiciona a tartaruga para iniciar o desenho do floco
        t.pendown()
        t.hideturtle()  # Esconde a tartaruga após o desenho

        # Desenha 3 lados da figura, girando 120 graus após cada lado para formar o floco de neve
        for _ in range(3):
            koch(300, profundidade)
            t.right(120)

        wn.exitonclick()  # Mantém a janela aberta até o clique do usuário

    else:
        # Corrigido: cria figura com fundo preto diretamente
        plt.figure(figsize=(8, 6), facecolor="black")
        ax = plt.gca()
        ax.set_facecolor("black")
        ax.axis("off")
        ax.set_aspect("equal")  # Mantém proporção do triângulo

        linhas = []  # Lista para armazenar os segmentos da curva de Koch

        def koch_matplotlib(x1, y1, x2, y2, level):
            if level == 0:
                linhas.append(((x1, x2), (y1, y2)))  # Adiciona linha reta
            else:
                dx = (x2 - x1) / 3
                dy = (y2 - y1) / 3

                xA, yA = x1, y1
                xB, yB = x1 + dx, y1 + dy

                angulo = math.atan2(y2 - y1, x2 - x1)
                dist = math.hypot(dx, dy)
                xC = xB + math.cos(angulo - math.pi / 3) * dist
                yC = yB + math.sin(angulo - math.pi / 3) * dist

                xD, yD = x1 + 2 * dx, y1 + 2 * dy
                xE, yE = x2, y2

                # Recursão nos 4 segmentos que formam a curva de Koch
                koch_matplotlib(xA, yA, xB, yB, level - 1)
                koch_matplotlib(xB, yB, xC, yC, level - 1)
                koch_matplotlib(xC, yC, xD, yD, level - 1)
                koch_matplotlib(xD, yD, xE, yE, level - 1)

        def desenhar_triangulo_koch(x, y, size, level):
            # Calcula os 3 vértices do triângulo equilátero
            pontos = [
                (x, y),
                (x + size, y),
                (x + size/2, y + (math.sqrt(3)/2) * size)
            ]

            # Desenha os 3 lados com curva de Koch
            koch_matplotlib(pontos[0][0], pontos[0][1], pontos[1][0], pontos[1][1], level)
            koch_matplotlib(pontos[1][0], pontos[1][1], pontos[2][0], pontos[2][1], level)
            koch_matplotlib(pontos[2][0], pontos[2][1], pontos[0][0], pontos[0][1], level)

        # Inicia o desenho do floco de neve como triângulo com lados de 300 unidades
        desenhar_triangulo_koch(-150, 0, 300, profundidade)

        # Desenha todas as linhas calculadas
        for linha in linhas:
            ax.plot(linha[0], linha[1], color="white", linewidth=1)

        # Corrigido: define limites da tela com base na figura
        ax.set_xlim(-180, 180)
        ax.set_ylim(-50, 280)

        plt.tight_layout()
        plt.show()
