import turtle  # Biblioteca para desenho gráfico
import matplotlib.pyplot as plt  # Para visualização com mathlib
import math  # Funções trigonométricas

def desenhar_arvore(profundidade, usar_turtle):
    if usar_turtle:
        t = turtle.Turtle()  # Cria a "caneta" para desenhar
        wn = turtle.Screen()  # Cria a janela do desenho
        wn.bgcolor("black")   # Fundo escuro
        t.color("white")      # Cor da linha clara
        t.speed("fastest")    # Velocidade máxima do desenho

        t.penup()
        t.goto(0, -200)  # Posição inicial da base da árvore
        t.left(90)       # Aponta para cima
        t.pendown()
        t.hideturtle()   # Esconde a tartaruga após o desenho
        branchSize = 100  # Tamanho inicial do tronco

        def draw_branch(level):
            if level > profundidade:  # Condição de parada da recursão
                return
            # Tamanho e ângulo diminuem com o nível para efeito natural
            tamanho = branchSize * (0.8 ** level)
            angulo = 45 * (0.6 ** level)

            t.forward(tamanho)   # Desenha o galho principal
            t.left(angulo)       # Vira para o galho esquerdo
            draw_branch(level + 1)  # Recursão para galho esquerdo

            t.right(2 * angulo)  # Vira para o galho direito
            draw_branch(level + 1)  # Recursão para galho direito

            t.left(angulo)       # Volta à direção original
            t.backward(tamanho)  # Retorna para o ponto inicial do galho

        draw_branch(0)  # Inicia a recursão a partir do nível 0
        wn.exitonclick()  # Fecha a janela ao clicar

    else:
        # Usando matplotlib para desenhar a árvore com recursão
        fig, ax = plt.subplots()
        ax.set_facecolor("black")  # Fundo preto
        ax.axis("off")  # Remove eixos
        branchSize = 100  # Tamanho inicial do tronco

        # Lista para armazenar as linhas da árvore
        linhas = []

        def draw_branch(x, y, angulo, level):
            if level > profundidade:
                return
            # Calcula o comprimento do galho com base no nível
            tamanho = branchSize * (0.8 ** level)

            # Coordenadas do ponto final do galho
            x_fim = x + tamanho * math.cos(math.radians(angulo))
            y_fim = y + tamanho * math.sin(math.radians(angulo))

            # Adiciona a linha à lista
            linhas.append(((x, x_fim), (y, y_fim)))

            # Recursão para os galhos esquerdo e direito
            novo_angulo = 45 * (0.6 ** level)
            draw_branch(x_fim, y_fim, angulo + novo_angulo, level + 1)
            draw_branch(x_fim, y_fim, angulo - novo_angulo, level + 1)

        # Início da árvore no centro inferior
        draw_branch(0, -200, 90, 0)  # ✅ MOVIDA para fora da função

        # Desenha todas as linhas calculadas
        for linha in linhas:
            ax.plot(linha[0], linha[1], color="white", linewidth=1)

        # Ajusta os limites da área visível
        ax.set_xlim(-150, 150)
        ax.set_ylim(-250, 200)
        ax.set_aspect("equal")      # ✅ Mantém proporção correta
        ax.autoscale(False)         # ✅ Desativa ajuste automático

        plt.show()

