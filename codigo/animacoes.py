import pygame, sys
import time
from var_globais import *

class Animacoes(pygame.sprite.Sprite):
    def __init__(self,duracao=3):
        self.__fonte = pygame.font.Font('../fonte/Pixeled.ttf',30)
        self.__fonte_buff = pygame.font.Font('../fonte/Pixeled.ttf',10)
        self.__duracao = duracao
        self.__ativa = False
        self.__inicio = 0
        self.__mensagem = ""
        self.__sound = pygame.mixer.Sound('../sons/risada.mp3')

        self.__buff_ativa = False
        self.__buff_inicio = 0
        self.__buff_mensagem = ""
        self.__buff_duracao = 2

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, value):
        self.__fonte = value

    @property
    def fonte_buff(self):
        return self.__fonte_buff

    @fonte_buff.setter
    def fonte_buff(self, value):
        self.__fonte_buff = value

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, value):
        self.__duracao = value

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, value):
        self.__ativa = value

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, value):
        self.__inicio = value

    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, value):
        self.__mensagem = value

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        self.__sound = value

    @property
    def buff_ativa(self):
        return self.__buff_ativa

    @buff_ativa.setter
    def buff_ativa(self, value):
        self.__buff_ativa = value

    @property
    def buff_inicio(self):
        return self.__buff_inicio

    @buff_inicio.setter
    def buff_inicio(self, value):
        self.__buff_inicio = value

    @property
    def buff_mensagem(self):
        return self.__buff_mensagem

    @buff_mensagem.setter
    def buff_mensagem(self, value):
        self.__buff_mensagem = value

    @property
    def buff_duracao(self):
        return self.__buff_duracao

    @buff_duracao.setter
    def buff_duracao(self, value):
        self.__buff_duracao = value
    
    def iniciar_animacao(self) -> None:
        self.ativa = True
        self.inicio = time.time()
        self.sound.play()
        self.mensagem = "PROXIMA ONDA EM"

    def iniciar_animacao_buff(self, mensagem_buff: str) -> None:
        self.buff_ativa = True
        self.buff_inicio = time.time()
        self.buff_mensagem = mensagem_buff
    
    def update(self,screen) -> bool:
        if self.ativa:            
            tempo_passado = time.time() - self.inicio
            tempo_restante = int(self.duracao - tempo_passado) + 1

            if tempo_passado >= self.duracao:
                self.ativa = False
            else: 
                texto = f"{self.mensagem} {tempo_restante}..."
                imagem_texto = self.fonte.render(texto,False,"white")
                posicao_texto = imagem_texto.get_rect(center=(largura_tela // 2, altura_tela // 2))
                screen.blit(imagem_texto,posicao_texto)

        if self.buff_ativa:
            buff_tempo_passado = time.time() - self.buff_inicio
            
            if buff_tempo_passado >= self.buff_duracao:
                self.buff_ativa = False
            else:
                # Optional: make it fade out (more complex, but possible)
                # For now, just display it
                imagem_texto_buff = self.fonte_buff.render(self.buff_mensagem, False, "yellow") # Yellow for buffs
                posicao_texto_buff = imagem_texto_buff.get_rect(bottomleft=(10, altura_tela - 10)) # Adjust position as needed
                screen.blit(imagem_texto_buff, posicao_texto_buff)

        return self.ativa or self.buff_ativa