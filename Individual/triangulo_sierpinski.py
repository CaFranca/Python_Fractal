import turtle              # Biblioteca para desenho interativo
import matplotlib.pyplot as plt  # Biblioteca para gráficos
import numpy as np          # Biblioteca para manipulação de arrays

def desenhar_sierpinski(profundidade, usar_turtle):
    """
    Desenha o Triângulo de Sierpinski.
    
    profundidade → número de níveis de recursão do fractal
    usar_turtle → True para Turtle (interativo), False para Matplotlib (rápido)
    """

    if usar_turtle:
        # --- VERSÃO INTERATIVA COM TURTLE ---
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Triângulo de Sierpinski - Turtle")

        t = turtle.Turtle()
        t.speed(0)  # Máxima velocidade
        t.hideturtle()
        t.penup()
        t.color("white")

        def draw_triangle(points):
            """Desenha um triângulo conectando os 3 pontos"""
            t.penup()
            t.goto(points[0])
            t.pendown()
            t.goto(points[1])
            t.goto(points[2])
            t.goto(points[0])

        def sierpinski(points, level):
            """
            Função recursiva para dividir o triângulo em 3 triângulos menores
            e desenhar o padrão de Sierpinski
            """
            draw_triangle(points)
            if level > 0:
                # Calcula os pontos médios de cada lado
                mid = lambda p1, p2: ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)
                # Chama recursivamente para cada triângulo menor
                sierpinski([points[0], mid(points[0], points[1]), mid(points[0], points[2])], level-1)
                sierpinski([points[1], mid(points[1], points[0]), mid(points[1], points[2])], level-1)
                sierpinski([points[2], mid(points[2], points[0]), mid(points[2], points[1])], level-1)

        # Pontos do triângulo base
        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski(base, profundidade)

        screen.exitonclick()  # Fecha a janela ao clicar

    else:
        # --- VERSÃO RÁPIDA COM MATPLOTLIB ---
        def midpoint(p1, p2):
            """Calcula o ponto médio entre dois pontos"""
            return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

        def sierpinski_matplotlib(points, level):
            """Função recursiva para desenhar o Triângulo de Sierpinski com matplotlib"""
            if level == 0:
                # Conecta os pontos para formar o triângulo
                triangle = np.array(points + [points[0]])
                plt.plot(triangle[:, 0], triangle[:, 1], 'w-')  # 'w-' = linha branca
            else:
                # Chama recursivamente para cada triângulo menor
                sierpinski_matplotlib([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])], level-1)
                sierpinski_matplotlib([points[1],
                    midpoint(points[1], points[0]),
                    midpoint(points[1], points[2])], level-1)
                sierpinski_matplotlib([points[2],
                    midpoint(points[2], points[0]),
                    midpoint(points[2], points[1])], level-1)

        # Configuração da figura
        plt.figure(facecolor="black")
        ax = plt.gca()
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        plt.axis("off")  # Remove eixos

        # Triângulo base
        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski_matplotlib(base, profundidade)

        plt.tight_layout()
        plt.show()


# --- Permite rodar sozinho sem app.py ---
if __name__ == "__main__":
    print("Executando Triângulo de Sierpinski sem app.py")
    try:
        profundidade = int(input("Digite a profundidade da recursão (ex: 4 a 8): "))
    except ValueError:
        profundidade = 4
        print("Valor inválido, usando profundidade = 4")

    metodo = input("Escolha a biblioteca (1 = Turtle, 2 = Matplotlib): ")
    usar_turtle = metodo.strip() == "1"

    desenhar_sierpinski(profundidade, usar_turtle)
