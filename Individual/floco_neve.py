import turtle  # Biblioteca que permite desenhar na tela como uma tartaruga
import matplotlib.pyplot as plt  # Biblioteca para gráficos matemáticos
import math  # Biblioteca com funções matemáticas (seno, cosseno, radianos)

def desenhar_floco(profundidade, usar_turtle):
    """
    Desenha o Floco de Neve de Koch (triângulo fractal).
    
    profundidade → quantas vezes cada lado será subdividido
    usar_turtle → True para Turtle (interativo), False para Matplotlib (mais rápido)
    """

    if usar_turtle:
        # --- VERSÃO INTERATIVA COM TURTLE ---
        t = turtle.Turtle()  # Cria a "caneta" para desenhar
        wn = turtle.Screen()  # Cria a janela do desenho
        wn.bgcolor("black")   # Fundo preto
        t.speed("fastest")    # Velocidade máxima da tartaruga
        t.color("white")      # Cor da linha branca

        def koch(length, level):
            """
            Função recursiva que desenha um segmento da curva de Koch.
            
            length → tamanho do segmento
            level → nível da recursão
            """
            if level == 0:
                # Caso base: apenas desenha linha reta
                t.forward(length)
            else:
                # Divide o segmento em 4 partes formando o "dente" do fractal
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)
                t.right(120)
                koch(length / 3, level - 1)
                t.left(60)
                koch(length / 3, level - 1)

        # Posiciona a tartaruga para começar o desenho
        t.penup()
        t.goto(-150, 100)
        t.pendown()
        t.hideturtle()

        # Desenha os 3 lados do triângulo (floco de neve)
        for _ in range(3):
            koch(300, profundidade)
            t.right(120)  # Vira 120° para desenhar o próximo lado

        wn.exitonclick()  # Fecha a janela quando o usuário clicar

    else:
        # --- VERSÃO RÁPIDA COM MATPLOTLIB ---
        plt.figure(figsize=(8, 6), facecolor="black")  # Cria figura com fundo preto
        ax = plt.gca()
        ax.set_facecolor("black")
        ax.axis("off")  # Remove eixos e números
        ax.set_aspect("equal")  # Mantém proporção correta

        linhas = []  # Lista para guardar todos os segmentos da curva

        def koch_matplotlib(x1, y1, x2, y2, level):
            """
            Calcula recursivamente os segmentos da curva de Koch.
            
            (x1, y1) → ponto inicial
            (x2, y2) → ponto final
            level → nível da recursão
            """
            if level == 0:
                linhas.append(((x1, x2), (y1, y2)))
            else:
                # Divide o segmento em 3 partes
                dx = (x2 - x1) / 3
                dy = (y2 - y1) / 3

                xA, yA = x1, y1
                xB, yB = x1 + dx, y1 + dy

                # Calcula ponto do "dente" do fractal
                angulo = math.atan2(y2 - y1, x2 - x1)  # Ângulo do segmento
                dist = math.hypot(dx, dy)              # Comprimento do terço
                xC = xB + math.cos(angulo - math.pi / 3) * dist
                yC = yB + math.sin(angulo - math.pi / 3) * dist

                xD, yD = x1 + 2*dx, y1 + 2*dy
                xE, yE = x2, y2

                # Chamada recursiva para os 4 segmentos
                koch_matplotlib(xA, yA, xB, yB, level - 1)
                koch_matplotlib(xB, yB, xC, yC, level - 1)
                koch_matplotlib(xC, yC, xD, yD, level - 1)
                koch_matplotlib(xD, yD, xE, yE, level - 1)

        def desenhar_triangulo_koch(x, y, size, level):
            """
            Desenha um triângulo com curvas de Koch nos 3 lados.
            
            x, y → ponto inicial do triângulo
            size → tamanho do lado do triângulo
            level → profundidade da curva
            """
            # Calcula os 3 vértices do triângulo equilátero
            pontos = [
                (x, y),
                (x + size, y),
                (x + size / 2, y + (math.sqrt(3)/2) * size)
            ]
            # Desenha os 3 lados usando a função koch_matplotlib
            koch_matplotlib(pontos[0][0], pontos[0][1], pontos[1][0], pontos[1][1], level)
            koch_matplotlib(pontos[1][0], pontos[1][1], pontos[2][0], pontos[2][1], level)
            koch_matplotlib(pontos[2][0], pontos[2][1], pontos[0][0], pontos[0][1], level)

        # Inicia o desenho do triângulo com tamanho 300
        desenhar_triangulo_koch(-150, 0, 300, profundidade)

        # Desenha todas as linhas calculadas
        for linha in linhas:
            ax.plot(linha[0], linha[1], color="white", linewidth=1)

        # Ajusta limites da tela
        ax.set_xlim(-180, 180)
        ax.set_ylim(-50, 280)

        plt.tight_layout()
        plt.show()


# --- Permite rodar sozinho sem app.py ---
if __name__ == "__main__":
    print("Executando Floco de Neve (Curva de Koch) sem app.py")

    # Solicita profundidade da recursão ao usuário
    try:
        profundidade = int(input("Digite a profundidade da recursão (ex: 3 a 6): "))
    except ValueError:
        profundidade = 4
        print("Valor inválido, usando profundidade = 4")

    # Solicita escolha da biblioteca
    metodo = input("Escolha a biblioteca (1 = Turtle, 2 = Matplotlib): ")
    usar_turtle = metodo.strip() == "1"

    desenhar_floco(profundidade, usar_turtle)
