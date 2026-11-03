#SISTEMA DE ALERTA DA REPRESA 

#LIMPEZA DO TERMINAL AO EXECUTAR O PROGRAMA
import os
os.system('cls' if os.name == 'nt' else 'clear')

#SORTEIO 
import random

#FUNÇÕES

#Inicialização do sistema
def inicio():
    print("-" * 40)
    print("Sistema de alerta da Represa")
    print("-" * 40)

def monitoracao():
    print("-" * 40)
    print("Ativando sistema de monitoração:")
    print("-" * 40)

def final():
    print("=" * 40)

#NÍVEIS DA REPRESA
represa = [
    ["Nível 1","Muito baixo (crítico)"],
    ["Nível 2","Baixo"],
    ["Nível 3","Médio"],
    ["Nível 4","Alto"],
    ["Nível 5","Muito alto (alerta)"]
]

#ESTRUTURA DO PROGRAMA

inicio()

monitoracao()

nivel = random.choice(represa)
print(f"\nA situação da represa é: {nivel}!")

final()