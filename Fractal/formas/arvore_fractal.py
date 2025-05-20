import turtle  # Biblioteca para desenho gráfico com tartaruga
import matplotlib.pyplot as plt  # Biblioteca para gráficos e visualizações
import math  # Funções matemáticas (como seno, cosseno)

def desenhar_arvore(profundidade, usar_turtle):
    if usar_turtle:
        # Configuração da janela e tartaruga
        t = turtle.Turtle()
        wn = turtle.Screen()
        wn.bgcolor("black")      # Cor de fundo
        t.color("white")         # Cor do desenho
        t.speed("fastest")       # Velocidade máxima
        t.hideturtle()           # Esconde a tartaruga
        t.penup()
        t.goto(0, -200)          # Posição inicial (base da árvore)
        t.left(90)               # Aponta para cima
        t.pendown()

        branchSize = 100  # Tamanho inicial do tronco

        # Função recursiva para desenhar galhos
        def draw_branch(level):
            if level > profundidade:
                return

            # Tamanho e ângulo do galho diminuem com a profundidade
            tamanho = branchSize * (0.8 ** level)
            angulo = 45 * (0.6 ** level)

            t.forward(tamanho)           # Desenha o galho principal
            t.left(angulo)              # Vira à esquerda
            draw_branch(level + 1)      # Desenha subgalho esquerdo

            t.right(2 * angulo)         # Vira à direita
            draw_branch(level + 1)      # Desenha subgalho direito

            t.left(angulo)              # Retorna à posição original
            t.backward(tamanho)         # Retorna à base do galho

        draw_branch(0)  # Inicia a árvore do nível 0
        wn.exitonclick()  # Fecha a janela ao clicar

    else:
        # Modo matplotlib para desenhar a árvore de forma rápida
         plt.figure(figsize=(8, 8), facecolor="black")
    ax = plt.gca()
    ax.set_facecolor("black")
    ax.axis("off")  # Remove eixos

    branch_size = 100

    def draw_branch(x, y, angle, level):
        if level > profundidade:
            return

        # Calcula o tamanho do galho
        length = branch_size * (0.8 ** level)

        # Coordenadas do ponto final
        x_end = x + length * math.cos(math.radians(angle))
        y_end = y + length * math.sin(math.radians(angle))

        # Desenha linha do galho atual
        ax.plot([x, x_end], [y, y_end], color="white", linewidth=1)

        # Chamada recursiva para galhos esquerdo e direito
        draw_branch(x_end, y_end, angle + 30, level + 1)
        draw_branch(x_end, y_end, angle - 30, level + 1)

    # Início da árvore no centro inferior
    draw_branch(0, -200, 90, 0)

    # Ajusta os limites da tela
    ax.set_xlim(-150, 150)
    ax.set_ylim(-250, 250)
    ax.set_aspect("equal")

    plt.tight_layout()
    plt.show()
