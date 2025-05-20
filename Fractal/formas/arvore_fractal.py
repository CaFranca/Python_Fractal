import turtle  # Biblioteca para desenho gráfico

def desenhar_arvore(profundidade):
    t = turtle.Turtle()  # Cria a "caneta" para desenhar
    wn = turtle.Screen()  # Cria a janela do desenho
    wn.bgcolor("black")   # Fundo escuro
    t.color("white")      # Cor da linha clara
    t.speed("fastest")    # Velocidade máxima do desenho

    t.penup()
    t.goto(0, -200)  # Posição inicial da base da árvore
    t.left(90)       # Aponta para cima
    t.pendown()

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
