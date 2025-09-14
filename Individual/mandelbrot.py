import numpy as np          # Biblioteca para cálculos com arrays/matrizes
import matplotlib.pyplot as plt  # Biblioteca para gráficos matemáticos
import turtle               # Biblioteca para desenho interativo

def desenhar_mandelbrot(usar_turtle):
    """
    Desenha o Conjunto de Mandelbrot.
    
    usar_turtle → True para Turtle (lento, interativo)
                   False para Matplotlib (rápido, elegante)
    """

    # --- PARÂMETROS COMUNS ---
    largura, altura = 300, 300  # Número de pontos horizontais e verticais
    max_iter = 100              # Número máximo de iterações para cada ponto

    # Limites do plano complexo (área do fractal que será desenhada)
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5

    if usar_turtle:
        # --- VERSÃO INTERATIVA COM TURTLE ---
        turtle.colormode(255)  # Permite cores RGB de 0 a 255
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.setup(width=600, height=600)
        wn.setworldcoordinates(x_min, y_min, x_max, y_max)  # Define coordenadas do mundo

        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)  # Velocidade máxima
        t.penup()   # Levanta a "caneta" para posicionamento

        # Percorre cada ponto da tela
        for x in range(largura):
            for y in range(altura):
                # Converte coordenadas da tela para coordenadas complexas
                zx = x_min + (x / largura) * (x_max - x_min)
                zy = y_min + (y / altura) * (y_max - y_min)
                z = complex(0, 0)
                c = complex(zx, zy)
                iter = 0

                # Iteração de Mandelbrot
                while abs(z) < 2 and iter < max_iter:
                    z = z*z + c
                    iter += 1

                # Se o ponto "escapou", calcula cor
                if iter < max_iter:
                    cor = (
                        int(255 - iter * 5) % 255,
                        int(iter * 10) % 255,
                        int(iter * 3) % 255
                    )
                    t.goto(zx, zy)
                    t.dot(2, cor)  # Desenha o ponto com a cor calculada

        wn.exitonclick()  # Fecha a janela ao clicar

    else:
        # --- VERSÃO RÁPIDA COM MATPLOTLIB E NUMPY ---
        x = np.linspace(x_min, x_max, largura)  # Valores horizontais
        y = np.linspace(y_min, y_max, altura)   # Valores verticais
        X, Y = np.meshgrid(x, y)               # Cria grade de coordenadas
        C = X + 1j * Y                          # Converte para números complexos

        Z = np.zeros_like(C)        # Inicializa Z = 0 para todos os pontos
        imagem = np.zeros(C.shape, dtype=int)  # Guarda cores/iteração de cada ponto

        # Iteração de Mandelbrot
        for i in range(max_iter):
            mascara = np.abs(Z) <= 2           # Pontos ainda dentro do conjunto
            Z[mascara] = Z[mascara] ** 2 + C[mascara]
            imagem[mascara & (np.abs(Z) > 2)] = i  # Marca quando o ponto "escapou"

        # Cria figura para exibir
        plt.figure(figsize=(8, 8), facecolor="black")
        ax = plt.gca()
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        ax.axis("off")  # Remove eixos

        # Mostra o fractal usando colormap 'inferno'
        plt.imshow(imagem, extent=[x_min, x_max, y_min, y_max],
                   cmap="inferno", interpolation="bilinear")

        plt.tight_layout()
        plt.show()


# --- Permite rodar sozinho sem app.py ---
if __name__ == "__main__":
    print("Executando Conjunto de Mandelbrot sem app.py")

    # Escolha da biblioteca pelo usuário
    metodo = input("Escolha a biblioteca (1 = Turtle, 2 = Matplotlib): ")
    usar_turtle = metodo.strip() == "1"

    desenhar_mandelbrot(usar_turtle)
