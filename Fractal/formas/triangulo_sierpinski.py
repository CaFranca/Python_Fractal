# Importamos as bibliotecas necessárias
import turtle                 # Usada para desenhar de forma interativa (como uma "caneta" na tela)
import matplotlib.pyplot as plt   # Usada para fazer gráficos e desenhos estáticos
import numpy as np            # Usada para trabalhar com arrays e cálculos matemáticos

# Função principal que desenha o triângulo de Sierpinski
# profundidade → quantas vezes o triângulo será dividido em partes menores
# usar_turtle → escolhe se o desenho será feito com Turtle (True) ou com Matplotlib (False)
def desenhar_sierpinski(profundidade, usar_turtle):
    
    # --- VERSÃO COM TURTLE ---
    if usar_turtle:
        # Criamos a tela onde o desenho aparecerá
        screen = turtle.Screen()   
        screen.bgcolor("black")          # Fundo preto
        screen.title("Triângulo de Sierpinski")  # Título da janela
        
        # Criamos a "tartaruga" (um cursor que desenha na tela)
        t = turtle.Turtle()
        t.speed(0)              # Velocidade máxima de desenho
        t.hideturtle()          # Esconde o desenho da tartaruga (só aparece o traço)
        t.penup()               # Levanta a caneta (não desenha enquanto se move)
        t.color("white")        # Cor do traço branco

        # Função que desenha um triângulo a partir de 3 pontos
        def draw_triangle(points):
            """
            Desenha um triângulo ligando os três pontos fornecidos.
            """
            t.penup()              # Levanta a caneta para ir até o primeiro ponto sem desenhar
            t.goto(points[0])      # Vai até o ponto inicial
            t.pendown()            # Abaixa a caneta para começar a desenhar
            t.goto(points[1])      # Desenha linha até o segundo ponto
            t.goto(points[2])      # Desenha linha até o terceiro ponto
            t.goto(points[0])      # Fecha o triângulo voltando ao ponto inicial

        # Função recursiva para criar o triângulo de Sierpinski
        def sierpinski(points, level):
            """
            Desenha recursivamente o triângulo de Sierpinski.
            """
            draw_triangle(points)   # Desenha o triângulo atual
            if level > 0:           # Se ainda houver níveis de divisão
                # Função auxiliar que calcula o ponto médio entre dois pontos
                mid = lambda p1, p2: ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

                # Chama a função recursivamente para os 3 novos triângulos formados
                sierpinski([points[0], mid(points[0], points[1]), mid(points[0], points[2])], level-1)
                sierpinski([points[1], mid(points[1], points[0]), mid(points[1], points[2])], level-1)
                sierpinski([points[2], mid(points[2], points[0]), mid(points[2], points[1])], level-1)

        # Pontos iniciais do triângulo maior (um triângulo equilátero)
        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski(base, profundidade)   # Inicia o desenho recursivo

        screen.exitonclick()  # Mantém a janela aberta até clicar nela

    # --- VERSÃO COM MATPLOTLIB ---
    else:
        # Função auxiliar para calcular o ponto médio entre dois pontos
        def midpoint(p1, p2):
            return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

        # Função recursiva para desenhar o triângulo de Sierpinski
        def sierpinski_matplotlib(points, level):
            if level == 0:   # Caso base: só desenha o triângulo atual
                triangle = np.array(points + [points[0]])  # Fecha o triângulo (volta ao início)
                plt.plot(triangle[:, 0], triangle[:, 1], 'w-')  # Desenha em branco
            else:
                # Divide o triângulo em 3 menores e chama a função para cada um
                sierpinski_matplotlib([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])], level-1)
                sierpinski_matplotlib([points[1],
                    midpoint(points[1], points[0]),
                    midpoint(points[1], points[2])], level-1)
                sierpinski_matplotlib([points[2],
                    midpoint(points[2], points[0]),
                    midpoint(points[2], points[1])], level-1)

        # Configurações da figura
        plt.figure(facecolor='black')  # Fundo da figura preto
        ax = plt.gca()                 # Pega os eixos da figura
        ax.set_facecolor("black")      # Fundo dos eixos também preto
        ax.set_aspect('equal')         # Mantém proporções corretas
        plt.axis('off')                # Remove os eixos e números (fica só o desenho)

        # Triângulo inicial
        base = [(-200, -100), (0, 200), (200, -100)]
        sierpinski_matplotlib(base, profundidade)  # Inicia a recursão

        plt.tight_layout()  # Ajusta margens automaticamente
        plt.show()          # Mostra o desenho na tela
