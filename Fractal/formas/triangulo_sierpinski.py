import turtle  # Biblioteca para desenhos gráficos com tartaruga

def desenhar_sierpinski(profundidade):

    screen = turtle.Screen()   # Cria a tela para o desenho
    screen.bgcolor("black")    # Define o fundo branco (pode ser alterado para fundo escuro)
    screen.title("Triângulo de Sierpinski")  # Título da janela

    t = turtle.Turtle()    # Cria a tartaruga (caneta)
    t.speed(0)             # Define velocidade máxima de desenho
    t.hideturtle()         # Esconde o cursor da tartaruga para visual mais limpo
    t.penup()              # Levanta a caneta para movimentação sem desenhar
    t.color("white")       # Define a cor da caneta (pode ser alterada para outras cores)
    def draw_triangle(points):
        """
        Desenha um triângulo ligando os três pontos fornecidos.
        """
        t.penup()
        t.goto(points[0])  # Vai para o primeiro ponto
        t.pendown()
        t.goto(points[1])  # Desenha linha até o segundo ponto
        t.goto(points[2])  # Desenha linha até o terceiro ponto
        t.goto(points[0])  # Fecha o triângulo voltando ao primeiro ponto

    def sierpinski(points, level):
        """
        Função recursiva que desenha o triângulo de Sierpinski.
        - points: lista com três pontos (vértices do triângulo)
        - level: nível atual da recursão (profundidade)
        """
        draw_triangle(points)  # Desenha o triângulo atual

        if level > 0:
            # Função auxiliar para calcular ponto médio entre dois pontos
            mid = lambda p1, p2: ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

            # Chamada recursiva para os três triângulos menores, formados pelos vértices e os pontos médios
            sierpinski([points[0], mid(points[0], points[1]), mid(points[0], points[2])], level-1)
            sierpinski([points[1], mid(points[1], points[0]), mid(points[1], points[2])], level-1)
            sierpinski([points[2], mid(points[2], points[0]), mid(points[2], points[1])], level-1)

    # Define os três vértices do triângulo inicial (tamanho e posição podem ser alterados)
    base = [(-200, -100), (0, 200), (200, -100)]

    # Inicia o desenho chamando a função recursiva com a profundidade desejada
    sierpinski(base, profundidade)

    # Mantém a janela aberta até o clique do usuário
    screen.exitonclick()
