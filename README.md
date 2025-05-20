# Fractais Geométricos em Python (com Turtle e Matplotlib)

Este repositório contém implementações de diversos fractais geométricos clássicos usando Python e as bibliotecas gráficas `turtle` e `matplotlib`. A combinação oferece flexibilidade para visualizações interativas e também para plotagens rápidas e estáticas, sendo ideal para aprendizado, demonstrações e experimentações visuais.

---

## Fractais incluídos

- Árvore Fractal  
- Floco de Neve de Koch  
- Curva de Koch  
- Triângulo de Sierpinski  
- Conjunto de Mandelbrot *(representado visualmente com base em iterações)*  

---

## Funcionalidades

- Menu interativo via terminal para escolher o fractal desejado.  
- Visualização gráfica animada com `turtle` (modo interativo, visual passo a passo).  
- Visualização rápida e estática com `matplotlib` (ideal para imagens de alta qualidade).  
- Opção de escolher o método de renderização para cada fractal (via parâmetro `usar_turtle`).  
- Ajuste da profundidade de recursão para observar diferentes níveis de complexidade.  
- Códigos organizados em módulos separados para facilitar a leitura e manutenção.  
- Interface visual com fundo preto e linhas brancas para melhor contraste e estética.  

---

## Métodos de desenho

### Modo Turtle

- Utiliza a biblioteca `turtle` para um desenho dinâmico, visualizando passo a passo a construção do fractal.  
- Ideal para demonstrações educacionais e interativas.  
- Possui velocidade configurável e permite interação direta com a janela gráfica.  

### Modo Matplotlib

- Utiliza a biblioteca `matplotlib` (com auxílio do `numpy` para cálculos eficientes) para plotagem rápida.  
- Produz imagens estáticas de alta qualidade e fácil exportação.  
- Visual com fundo preto e linhas brancas para alta visibilidade.  
- Ideal para geração rápida e visualização detalhada.  

---

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo
