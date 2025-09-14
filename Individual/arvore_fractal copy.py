import turtle  # Biblioteca que permite desenhar na tela como se fosse uma "tartaruga" com caneta
import matplotlib.pyplot as plt  # Biblioteca para desenhar gráficos e imagens matemáticas
import math  # Biblioteca com funções matemáticas, como seno, cosseno e radianos

def desenhar_arvore(profundidade, usar_turtle):
    """
    Desenha uma Árvore Fractal usando Turtle (interativa) ou Matplotlib (mais rápida).
    
    profundidade → controla quantas vezes os galhos se dividem (quanto maior, mais detalhada)
    usar_turtle → True para Turtle, False para Matplotlib
    """

    if usar_turtle:
        # --- VERSÃO COM TURTLE ---
        
        t = turtle.Turtle()  # Cria a "caneta" que vai desenhar
        wn = turtle.Screen()  # Cria a janela onde o desenho aparece
        wn.bgcolor("black")  # Define fundo preto para a janela
        t.color("white")     # Define cor branca para o desenho
        t.speed("fastest")   # Velocidade máxima da tartaruga
        t.hideturtle()       # Esconde o cursor da tartaruga (apenas o desenho aparece)
        t.penup()            # Levanta a caneta para mover sem desenhar
        t.goto(0, -200)      # Posiciona a tartaruga na base da árvore
        t.left(90)           # Aponta a tartaruga para cima
        t.pendown()          # Abaixa a caneta para começar a desenhar

        branchSize = 100  # Tamanho inicial do tronco principal

        def draw_branch(level):
            """
            Função recursiva que desenha os galhos da árvore.
            level → nível atual da recursão (começa em 0)
            """
            if level > profundidade:  # Condição de parada da recursão
                return  # Se chegamos na profundidade máxima, paramos de desenhar

            # Calcula tamanho e ângulo do galho diminuindo a cada nível
            tamanho = branchSize * (0.8 ** level)
            angulo = 45 * (0.6 ** level)

            t.forward(tamanho)  # Desenha o galho principal
            t.left(angulo)       # Vira para esquerda para desenhar subgalho
            draw_branch(level + 1)  # Desenha subgalho esquerdo

            t.right(2 * angulo)  # Vira para direita para desenhar outro subgalho
            draw_branch(level + 1)  # Desenha subgalho direito

            t.left(angulo)       # Retorna à posição original
            t.backward(tamanho)  # Volta para a base do galho

        draw_branch(0)  # Inicia o desenho a partir do tronco principal
        wn.exitonclick()  # Mantém a janela aberta até o clique do usuário

    else:
        # --- VERSÃO COM MATPLOTLIB ---
        plt.figure(figsize=(8, 8), facecolor="black")  # Cria a figura com fundo preto
        ax = plt.gca()  # Obtém o eixo de desenho
        ax.set_facecolor("black")  # Define fundo preto
        ax.axis("off")  # Remove eixos e números
        ax.set_aspect("equal")  # Mantém proporção correta do desenho

        branch_size = 100  # Tamanho inicial do tronco

        def draw_branch(x, y, angle, level):
            """
            Desenha os galhos usando coordenadas (x, y) e ângulo.
            Cada galho gera dois subgalhos recursivamente.
            """
            if level > profundidade:
                return

            # Calcula o comprimento do galho atual
            length = branch_size * (0.8 ** level)

            # Calcula as coordenadas do final do galho usando trigonometria
            x_end = x + length * math.cos(math.radians(angle))
            y_end = y + length * math.sin(math.radians(angle))

            # Desenha o galho atual
            ax.plot([x, x_end], [y, y_end], color="white", linewidth=1)

            # Chamada recursiva para o galho da esquerda (+30°) e da direita (-30°)
            draw_branch(x_end, y_end, angle + 30, level + 1)
            draw_branch(x_end, y_end, angle - 30, level + 1)

        # Inicia a árvore no centro inferior da tela
        draw_branch(0, -200, 90, 0)

        # Ajusta os limites da tela para caber toda a árvore
        ax.set_xlim(-150, 150)
        ax.set_ylim(-250, 250)

        plt.tight_layout()  # Ajusta margens automaticamente
        plt.show()  # Mostra o desenho na tela


# --- Permite rodar sozinho sem depender de outro arquivo ---
if __name__ == "__main__":
    print("Executando Árvore Fractal sem app.py")
    
    try:
        profundidade = int(input("Digite a profundidade da recursão (ex: 3 a 6): "))
    except ValueError:
        profundidade = 4
        print("Valor inválido, usando profundidade = 4")

    metodo = input("Escolha a biblioteca (1 = Turtle, 2 = Matplotlib): ")
    usar_turtle = metodo.strip() == "1"

    desenhar_arvore(profundidade, usar_turtle)
