
from time import sleep
from os import system
system('clear')
print('\033[32m{:=^35}\033[m'.format('Maratona 2021'))
print('''\033[33m[ 1 ]\033[m \033[34mLISTA DE FILMES DA DISNEY\033[m
\033[33m[ 2 ]\033[m \033[34mLISTA DE TERROR FILMES\033[m
\033[33m[ 3 ]\033[m \033[34mLISTA DE FILMES DE ACÃO\033[m
\033[33m[ 4 ]\033[m \033[34mLISTA DE FILMES DE SUSPENCE\033[m
\033[33m[ 5 ]\033[m \033[34mLISTA DE FILMES DE ROMANCE\033[m
\033[33m[ 6 ]\033[m \033[34mSAIR\033[m''')
print('\033[32m='*35,'\033[m')
menu = int(input('\033[4;36mEscolha uma opção:\033[m '))
print('\033[36m='*47,'\033[m')
print('\033[32mBuscando resultados...Aguarde.\033[m')
sleep(3)
if menu == 1:
	list_disney = ['Ghost in the Shell (1996)','Frozen: Uma Aventura Congelante (2013)','Aladdin (1992)','O Rei Leão (1994)','Uma Cilada Para Roger Rabbit (1988)','A Viagem de Chihiro (2002)','O Gigante de Ferro (1999)','Monstros S.A. (2001)','Fantasia (1940)','Ratatouille (2007)','Kubo e as Cordas Mágicas (2016)','Moana (2016)','Uma Aventura LEGO (2014)','WALL-E (2008)','Toy Story (1995)','Procurando Nemo (2003)','Up: Altas Aventuras (2009)','Divertida Mente (2015)']
	for n in list_disney:
		print('\033[35mFilme: {}\033[m'.format(n))
elif menu == 2:
	list_terror = ['01/10 - O EXORCISTA (1973)','02/10 - SUSPIRIA (1977)','03/10 - O MASSACRE DA SERRA-ELÉTRICA (1974)','04/10 - A BRUXA (2015)','05/10 - O SEXTO SENTIDO (1999)','06/10 - ARRASTE-ME PARA O INFERNO (2009)','07/10 - PSICOSE (1960)','08/10 - HEREDITÁRIO (2018)','09/10 - TUBARÃO (1975)','10/10 - INVOCAÇÃO DO MAL (2013)','11/10 - O BABADOOK (2014)','12/10 - JOGOS MORTAIS (2004)','13/10 - CARRIE (1976)','14/10 - O ILUMINADO (1980','15/10 - O BRINQUEDO ASSASSINO (1988)','16/10 - PREDADOR (1987)','17/10 - SEXTA-FEIRA 13 (1980)','Campo do Medo (2019)','Influência (2019)','SAINT MAUD','ARMY OF THE DEAD: INVASÃO EM LAS VEGAS','MALIGNANT','ESPÍRITOS OBSCUROS']
	for t in list_terror:
		print('\033[35mFilme: {}\033[m'.format(t))
elif menu == 3:
	list_acao = ['Machete','LEGO Batman: O Filme','Arranha-Céu: Coragem sem Limite','Atômica','Resgate','Velozes & Furiosos: Hobbs & Shaw','Em Ritmo de Fuga','Círculo de Fogo','Akira','Mad Max: Estrada da Fúria','Kingsman: Serviço Secreto (2015)','Dunkirk (2017)','A Identidade Bourne (2002)','Os Mercenários (2010)','Atômica (2017)','007 – Operação Skyfall (2012)','Missão Impossível – Nação Secreta (2015)','Velozes e Furiosos 7 (2015)','Batman: O Cavaleiro das Trevas (2008)','Mad Max: A Estrada da Fúria (2015)']
	for a in list_acao:
		print('\033[35mFilme: {}\033[m'.format(a))
elif menu == 4:
	list_suspence = ['Um Lugar Silencioso (2018)','Seven – Sete Pecados Mortais (1995)','O Sexto Sentido (1999)','Rua Cloverfield, 10 (2016)','O Bebê de Rosemary (1968)','Psicopata Americano (2000)','O Lobo Atrás da Porta (2013)','A Garota no Trem (2016)','Sob o Domínio do Mal (2004)','Amnésia (2000)','Em Chamas (2018)','O Silêncio dos Inocentes (1991)','Durante a Tormenta (2018)','À Espreita do Mal (2019)','Você Nunca Esteve Realmente Aqui (2017)','Clube da Luta (1999)','Donnie Darko (2001)','Se7en: Os Sete Crimes Capitais (1995)','Ilha do Medo (2010)']
	for s in list_suspence:
		print('\033[35mFilme: {}\033[m'.format(s))
elif menu == 5:
	list_romance = ['Dirty Dancing: ritmo quente (1987)','Ghost: do outro lado da vida (1990)','10 Coisas que eu odeio em você (1999)','Amor à segunda vista (2002)','Simplesmente amor (2003)','Brilho eterno de uma mente sem lembranças (2004)','Como se fosse a primeira vez (2004)','Diário de uma paixão (2004)','Quero ficar com Polly (2004)','A casa do lago (2006)','Pegar e largar (2006)','Mamma Mia (2008)','A verdade nua e crua (2009)','Comer Rezar e Amar (2010)','Como você sabe (2010)']
	for r in list_romance:
		print('\033[35mFilme: {}\033[m'.format(r))
elif menu == 6:
		print('\033[4;31mVolte sempre!\033[m')
else:
	print('\033[4;31mOpção invalida!Tente novamente.\033[m')
print('\033[36m='*47,'\033[m')
