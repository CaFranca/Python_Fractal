import turtle 

# Criação da tartaruga (caneta) e da tela
t = turtle.Turtle()
wn = turtle.Screen()

# Parâmetros da árvore
depth = 1        # 🔧 Recomendo usar 10 para teste. Pode mudar para 50 depois.
myDepth = 0
branchSize = 100

# Configuração da tela
turtle.screensize(canvwidth=500, canvheight=500)
wn.bgcolor("white")

# Posição inicial da tartaruga
t.penup()
t.goto(0, -200)
t.pendown()

# Desenho do tronco central
t.forward(100)
t.back(200)
t.forward(100)
t.left(90)

# Função recursiva que desenha os galhos
def drawSegment(myDepth, depth):
    print(f"Entrando no nível: {myDepth}")  # Mostra em qual profundidade está
    
    if myDepth >= depth:
        print(f"↳ Profundidade máxima {myDepth} atingida. Retornando.")
        return
    else:
        tamanho = branchSize * (0.8 ** myDepth)
        angulo = 45 * (0.6 ** myDepth)

        print(f"→ Desenhando galho nível {myDepth}: tamanho = {tamanho:.2f}, ângulo = {angulo:.2f}")
        
        t.forward(tamanho)
        t.left(angulo)
        drawSegment(myDepth + 1, depth)  # Galho da esquerda

        t.right(2 * angulo)
        drawSegment(myDepth + 1, depth)  # Galho da direita

        t.left(angulo)
        t.back(tamanho)

        print(f"← Retornando do nível {myDepth}")

# Início do desenho
drawSegment(myDepth, depth)

# Espera clique do usuário para fechar
wn.exitonclick()
