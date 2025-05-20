import turtle
import matplotlib.pyplot as plt
import numpy as np

def desenhar_sierpinski(profundidade, usar_turtle):
    if usar_turtle:
        screen = turtle.Screen()   # Cria a tela para o desenho
        screen.bgcolor("black")    # Fundo escuro
        screen.title("Triângulo de Sierpinski")  # Título da janela

        t = turtle.Turtle()    # Cria a tartaruga (caneta)
        t.speed(0)             # Velocidade máxima de desenho
        t.hideturtle()         # Esconde o cursor da tartaruga
        t.penup()              # Levanta a caneta para movimentar sem desenhar
        t.color("white")       # Cor da linha branca

        def draw_triangle(points):
            """
            Desenha um triângulo ligando os três pontos fornecidos.
            """
            t.penup()
            t.goto(points[0])
            t.pendown()
            t.goto(points[1])
            t.goto(points[2])
            t.goto(points[0])

        def sierpinski(points, level):
            """
            Desenha recursivamente o triângulo de Sierpinski.
            """
            draw_triangle(points)
            if level > 0:
                mid = lambda p1, p2: ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

                sierpinski([points[0], mid(points[0], points[1]), mid(points[0], points[2])], level-1)
                sierpinski([points[1], mid(points[1], points[0]), mid(points[1], points[2])], level-1)
                sierpinski([points[2], mid(points[2], points[0]), mid(points[2], points[1])], level-1)

        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski(base, profundidade)

        screen.exitonclick()

    else:
        # Versão com matplotlib (plotagem rápida)
        def midpoint(p1, p2):
            return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

        def sierpinski_matplotlib(points, level):
            if level == 0:
                triangle = np.array(points + [points[0]])  # fecha o triângulo
                plt.plot(triangle[:, 0], triangle[:, 1], 'w-')  # linha branca
            else:
                sierpinski_matplotlib([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])], level-1)
                sierpinski_matplotlib([points[1],
                    midpoint(points[1], points[0]),
                    midpoint(points[1], points[2])], level-1)
                sierpinski_matplotlib([points[2],
                    midpoint(points[2], points[0]),
                    midpoint(points[2], points[1])], level-1)

        plt.figure(facecolor='black')
        ax = plt.gca()
        ax.set_facecolor("black")
        ax.set_aspect('equal')
        plt.axis('off')

        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski_matplotlib(base, profundidade)

        plt.tight_layout()
        plt.show()
