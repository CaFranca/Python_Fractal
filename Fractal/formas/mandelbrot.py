# fractais/mandelbrot.py
import turtle  # Biblioteca para desenho gráfico

def desenhar_mandelbrot():
    largura = 300  # Largura da grade de pontos para desenhar (menor para melhor desempenho)
    altura = 300   # Altura da grade de pontos
    zoom = 1       # Zoom aplicado ao conjunto
    x_offset, y_offset = -0.5, 0.0  # Deslocamento para centralizar o fractal
    max_iter = 50  # Número máximo de iterações para determinar se um ponto pertence ao conjunto

    turtle.colormode(255)  # Define o modo de cor RGB com valores entre 0 e 255
    wn = turtle.Screen()   # Cria a janela de desenho
    wn.bgcolor("black")    # Fundo preto para contraste com os pontos coloridos
    wn.setup(width=600, height=600)  # Define o tamanho da janela
    wn.setworldcoordinates(-2, -1.5, 1, 1.5)  # Ajusta o sistema de coordenadas para mapear a região do fractal

    t = turtle.Turtle()   # Cria a tartaruga (caneta)
    t.hideturtle()        # Esconde o cursor da tartaruga para visual mais limpo
    t.speed(0)            # Define a velocidade máxima para o desenho
    t.penup()             # Levanta a caneta para movimentação sem desenhar
    t.color("white")  # Define a cor da caneta como branca

    # Loop pelos pixels da grade para calcular cada ponto do conjunto de Mandelbrot
    for x in range(largura):
        for y in range(altura):
            # Mapeia as coordenadas do pixel para o plano complexo
            zx = 3.0 * (x - largura / 2) / (zoom * largura) + x_offset
            zy = 2.0 * (y - altura / 2) / (zoom * altura) + y_offset
            z = complex(zx, zy)
            c = z
            iter = 0

            # Aplica a iteração da fórmula z = z^2 + c até sair do raio 2 ou alcançar max_iter
            while abs(z) < 2 and iter < max_iter:
                z = z * z + c
                iter += 1

            # Se o ponto "escapa" antes de max_iter, calcula uma cor baseada em quantas iterações durou
            if iter < max_iter:
                cor = (
                    int(255 - iter * 5) % 255,  # Canal vermelho (varia conforme iter)
                    int(iter * 10) % 255,       # Canal verde
                    int(iter * 3) % 255         # Canal azul
                )
                t.goto(zx, zy)  # Move a tartaruga para a posição calculada no plano
                t.dot(2, cor)   # Desenha um ponto pequeno com a cor calculada

    wn.exitonclick()  # Mantém a janela aberta até o clique do usuário
