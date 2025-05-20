# fractais/mandelbrot.py
import numpy as np
import matplotlib.pyplot as plt
import turtle

def desenhar_mandelbrot(usar_turtle):
    # Parâmetros comuns
    largura, altura = 300, 300
    max_iter = 100

    # Limites do plano complexo
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5

    if usar_turtle:
        turtle.colormode(255)  # Define modo RGB 0-255
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.setup(width=600, height=600)
        wn.setworldcoordinates(x_min, y_min, x_max, y_max)

        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()

        # Desenha ponto por ponto usando turtle (mais lento)
        for x in range(largura):
            for y in range(altura):
                zx = x_min + (x / largura) * (x_max - x_min)
                zy = y_min + (y / altura) * (y_max - y_min)
                z = complex(0, 0)
                c = complex(zx, zy)
                iter = 0

                while abs(z) < 2 and iter < max_iter:
                    z = z*z + c
                    iter += 1

                if iter < max_iter:
                    cor = (
                        int(255 - iter * 5) % 255,
                        int(iter * 10) % 255,
                        int(iter * 3) % 255
                    )
                    t.goto(zx, zy)
                    t.dot(2, cor)
        wn.exitonclick()

    else:
        # Modo matplotlib com numpy, mais rápido e colorido
        x = np.linspace(x_min, x_max, largura)
        y = np.linspace(y_min, y_max, altura)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros_like(C)
        imagem = np.zeros(C.shape, dtype=int)

        for i in range(max_iter):
            mascara = np.abs(Z) <= 2
            Z[mascara] = Z[mascara] ** 2 + C[mascara]
            imagem[mascara & (np.abs(Z) > 2)] = i

        plt.figure(figsize=(8, 8))
        plt.imshow(imagem, extent=[x_min, x_max, y_min, y_max], cmap='hot')
        plt.axis('off')
        plt.show()
