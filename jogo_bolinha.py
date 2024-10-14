#===================== IMPORTS =======================
import pygame as pg
import random as rm
import sys

#===================== VARIAVEIS =======================
#definir cores
VERMELHO = (255, 0, 0)
AMARELA = (255, 255, 0)
PRETO = (0,0,0)
BRANCO = (255, 255, 255)

LARGURAJANELA = 700
ALTURAJANELA = 500 
TAMANHO_BOLA = 20
VELOCIDADE_BOLA = 5

#===================== INICIALIZAÇÂO =======================
#inicia o pygame
pg.init()

#===================== TELA =======================
#cria a janela com as dimenções 
janela = pg.display.set_mode((LARGURAJANELA, ALTURAJANELA))
#coloca um nome na janela
pg.display.set_caption("Jogo da bolinha")

fundo = pg.image.load("fundo.jpg")
tela_vitoria = pg.image.load("tela_vitoria.png")

#cria relogio
clock = pg.time.Clock()

#cria variavel para usar no while para deixar a janela aberta
janela_aberta = True

# Variável para controlar o estado do jogo
jogo_iniciado = False

#===================== JOGADOR =======================
#cria retangulo 
retangulo1 = pg.Rect(50, ALTURAJANELA / 2 - 50, 20, 100)
retangulo2 = pg.Rect(LARGURAJANELA - 50 - 20, ALTURAJANELA / 2 - 50, 20, 100)

#===================== BOLA =======================
#cria bola
#bola = pg.draw.circle(janela, AMARELA, (LARGURAJANELA / 2, ALTURAJANELA / 2), TAMANHO_BOLA)
bola = pg.Rect(LARGURAJANELA / 2, ALTURAJANELA / 2, TAMANHO_BOLA, TAMANHO_BOLA) 

#velocidade da bola quando a bola for criada no retangulo pode ser alterada para uma posição aleatoria 
velocidade_bola= [rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA]), rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA])]

#===================== PONTUAÇÃO =======================
pontos_jogador1 = 0
pontos_jogador2 = 0

fonte = pg.font.SysFont("Calibre", 50)


# Loop do jogo
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                jogo_iniciado = True

    # Desenho da imagem de fundo
    janela.blit(fundo, (0, 0))

    # Desenho do texto "Pressione Enter para Iniciar"
    texto = fonte.render("Pressione 'Enter' para Iniciar", True, (255, 255, 255))
    janela.blit(texto, (120, 250))

    # Atualização da tela
    pg.display.flip()

    # Controle de taxa de quadros
    pg.time.Clock().tick(60)

    # Verificação se o jogo foi iniciado
    if jogo_iniciado:
        break


#===================== LOOP PRINCIPAL =======================
while janela_aberta:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        

    # ====================== JOGADOR =======================
    #teclas 
    teclas = pg.key.get_pressed()

    #teclas jogador1
    if teclas[pg.K_w]:
        retangulo1.y -= 5
        #se retangulo estiver fora da janela o retangulo volta para o topo
        if retangulo1.y < 0:
            retangulo1.y = 0   
    if teclas[pg.K_s]:
        retangulo1.y += 5
        #se retangulo estiver fora da janela o retangulo volta para o fundo
        if retangulo1.y > ALTURAJANELA - retangulo1.height:
            retangulo1.y = ALTURAJANELA - retangulo1.height 

    #teclas jogador2
    if teclas[pg.K_o]:
        retangulo2.y -= 5
        #se retangulo estiver fora da janela o retangulo volta para o topo 
        if retangulo2.y < 0:
            retangulo2.y = 0
    if teclas[pg.K_l]:
        retangulo2.y += 5
        #se retangulo estiver fora da janela o retangulo volta para o fundo 
        if retangulo2.y > ALTURAJANELA - retangulo2.height:
            retangulo2.y = ALTURAJANELA - retangulo2.height

   


   #===================  BOLA =======================
    # Movimentação da bola
    bola.x += velocidade_bola[0]
    bola.y += velocidade_bola[1]

    # Colisão com os retângulos
    if bola.colliderect(retangulo1) or bola.colliderect(retangulo2):
        velocidade_bola[0] = -velocidade_bola[0]

     # Colisão com as bordas da tela
    if bola.y < 0 or bola.y > ALTURAJANELA - TAMANHO_BOLA:
        velocidade_bola[1] = -velocidade_bola[1]
    if bola.x < 0:
        pontos_jogador2 += 1
        bola.x = LARGURAJANELA / 2
        bola.y = ALTURAJANELA / 2
        velocidade_bola = [rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA]), rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA])]
    elif bola.x > LARGURAJANELA - TAMANHO_BOLA:
        pontos_jogador1 += 1
        bola.x = LARGURAJANELA / 2
        bola.y = ALTURAJANELA / 2
        velocidade_bola = [rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA]), rm.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA])]

    # ===================  DESENHO =======================
    #desenho da tela
    janela.blit(fundo, (0, 0))
    pg.draw.rect(janela, VERMELHO, retangulo1)
    pg.draw.rect(janela, BRANCO, retangulo2)
    pg.draw.ellipse(janela, AMARELA, bola)

    #exibir os pontos
    texto_pontos_jogador1 = fonte.render(str(pontos_jogador1), True, VERMELHO)
    texto_pontos_jogador2 = fonte.render(str(pontos_jogador2), True, BRANCO)
    janela.blit(texto_pontos_jogador1, (LARGURAJANELA / 4, 20))
    janela.blit(texto_pontos_jogador2, (LARGURAJANELA * 3 / 4, 20))

    #===================== TELA DE VENCEDOR ========================
    if pontos_jogador1 == 1:
        janela.blit(tela_vitoria,(0,0))
        vencedor = fonte.render(f"Vencedor: jogador 1", True, (255, 255, 255))
        janela.blit(vencedor, (200, 250))
        pg.display.flip()
        pg.time.wait(2000)
        break
    elif pontos_jogador2 == 1:
        janela.blit(tela_vitoria,(0,0))
        vencedor = fonte.render(f"Vencedor: jogador 2", True, (255, 255, 255))
        janela.blit(vencedor, (200, 250))
        pg.display.flip()
        pg.time.wait(2000)
        break

    #================ TELA =================
    # alterações na tela
    pg.display.flip()

    #controle de taxa de quadros
    clock.tick(60)




