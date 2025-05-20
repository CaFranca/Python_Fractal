import turtle  # Biblioteca para desenho gráfico

def desenhar_floco(profundidade):
    t = turtle.Turtle()  # Cria a "caneta" para desenhar
    wn = turtle.Screen()  # Cria a janela do desenho
    wn.bgcolor("black")   # Define o fundo branco
    t.speed("fastest")    # Define a velocidade máxima do desenho
    t.color("white")      # Define a cor da linha como preta

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

    # Desenha 3 lados da figura, girando 120 graus após cada lado para formar o floco de neve
    for _ in range(3):
        koch(300, profundidade)
        t.right(120)

    wn.exitonclick()  # Mantém a janela aberta até o clique do usuário
