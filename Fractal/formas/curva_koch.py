import turtle  # Biblioteca para desenho gráfico
import matplotlib.pyplot as plt  # Para alternativa com mathlib
import math  # Funções trigonométricas

def desenhar_koch(profundidade, usar_turtle):
    if usar_turtle:
        t = turtle.Turtle()  # Cria a "caneta" para desenhar
        wn = turtle.Screen()  # Cria a janela do desenho
        wn.bgcolor("black")   # Fundo preto
        t.speed("fastest")    # Velocidade máxima do desenho
        t.color("white")      # Cor da linha branca

        def koch(length, level):
            if level == 0:  # Caso base: desenha linha reta
                t.forward(length)
            else:
                # Divide o segmento em 4 partes e desenha os segmentos recursivamente com ângulos para formar o fractal
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)
                t.right(120)
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)

        t.penup()
        t.goto(-150, 0)  # Posiciona para iniciar o desenho no centro-esquerda da tela
        t.pendown()
        t.hideturtle()  # Esconde a tartaruga após o desenho
        koch(300, profundidade)  # Desenha o fractal com tamanho 300 e profundidade dada
        wn.exitonclick()  # Fecha a janela ao clicar

    else:
        # Implementação com matplotlib
        fig, ax = plt.subplots()
        ax.set_facecolor("black")  # Fundo preto
        ax.axis("off")  # Remove os eixos

        linhas = []  # Lista para armazenar os segmentos da curva

        def koch_matplotlib(x1, y1, x2, y2, level):
            if level == 0:
                # Caso base: adiciona segmento reto
                linhas.append(((x1, x2), (y1, y2)))
            else:
                # Divide em 3 partes
                dx = (x2 - x1) / 3
                dy = (y2 - y1) / 3

                xA = x1
                yA = y1

                xB = x1 + dx
                yB = y1 + dy

                # Ponto do vértice do triângulo equilátero
                angulo = math.atan2(y2 - y1, x2 - x1)
                xC = xB + math.cos(angulo - math.pi / 3) * math.hypot(dx, dy)
                yC = yB + math.sin(angulo - math.pi / 3) * math.hypot(dx, dy)

                xD = x1 + 2 * dx
                yD = y1 + 2 * dy

                xE = x2
                yE = y2

                # Recursão para os 4 segmentos
                koch_matplotlib(xA, yA, xB, yB, level - 1)
                koch_matplotlib(xB, yB, xC, yC, level - 1)
                koch_matplotlib(xC, yC, xD, yD, level - 1)
                koch_matplotlib(xD, yD, xE, yE, level - 1)

        # Início da linha horizontal
        koch_matplotlib(-150, 0, 150, 0, profundidade)

        # Desenha todas as linhas calculadas
        for linha in linhas:
            ax.plot(linha[0], linha[1], color="white", linewidth=1)

        plt.show()
