import turtle  # Biblioteca para desenho gráfico

def desenhar_koch(profundidade):
    t = turtle.Turtle()  # Cria a "caneta" para desenhar
    wn = turtle.Screen()  # Cria a janela do desenho
    wn.bgcolor("black")   # Fundo branco
    t.speed("fastest")    # Velocidade máxima do desenho
    t.color("white")      # Cor da linha preta

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
    koch(300, profundidade)  # Desenha o fractal com tamanho 300 e profundidade dada
    wn.exitonclick()  # Fecha a janela ao clicar
