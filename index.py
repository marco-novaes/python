#Mudacça versao 2
import time

# Lista (Array) com os versos da música
letra = [
    "Tu tá com o código aberto, cara de preocupado",
    "Lendo documentação com o olhar cansado",
    "WE WILL DEBUG YOU", 
    "Tem um leak de memória, o servidor travou",
    "WE WILL DEBUG YOU", 
    "O prazo da entrega já se esgotou!"
]

def tocar_ritmo():
    # Saída de Dados com formatação especial
    print("🥁 TUM", end=" ", flush=True)
    time.sleep(0.3)
    print("🥁 TUM", end=" ", flush=True)
    time.sleep(0.3)
    print("🎸 PÁ!", flush=True)

# Lógica de iteração com controle de índice
for indice, verso in enumerate(letra):
    tocar_ritmo()
    
    # Condicional (If) usando operador de Módulo (%)
    if indice % 2 == 0:
        print(f"🎤 {verso.upper()} !!!") # Gritando no refrão
    else:
        print(f"🎤 {verso.lower()}...")   # Baixo nos versos
    
    print("-" * 30)
