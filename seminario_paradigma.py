
# SEMINÁRIO: CÁLCULO LAMBDA VS. VON NEUMANN

# Dados de entrada: pedidos de uma loja virtual
pedidos = [
    {"produto": "Mouse", "valor": 100, "ativo": True},
    {"produto": "Teclado", "valor": 200, "ativo": True},
    {"produto": "Monitor", "valor": 800, "ativo": False},
    {"produto": "Headset", "valor": 150, "ativo": True}
]


# A) VERSÃO IMPERATIVA - VON NEUMANN
def calcular_total_imperativo(pedidos):
    total = 0

    for p in pedidos:
        if p["ativo"]:
            total += p["valor"]

    return total


# B) VERSÃO FUNCIONAL - CÁLCULO LAMBDA
def calcular_total_funcional(pedidos):
    ativos = filter(
        lambda p: p["ativo"], pedidos
    )

    valores = map(
        lambda p: p["valor"], ativos
    )

    return sum(valores)


# EXECUÇÃO DOS DOIS MÉTODOS
resultado_a = calcular_total_imperativo(pedidos)
resultado_b = calcular_total_funcional(pedidos)

print("=== COMPARAÇÃO DOS PARADIGMAS ===")

print("Resultado imperativo: R$", resultado_a)
print("Resultado funcional: R$", resultado_b)

print("\nOs resultados são iguais?", resultado_a == resultado_b)


# DEMONSTRAÇÃO DE REDUÇÃO BETA
dobro = lambda x: x * 2

print("\n=== CÁLCULO LAMBDA ===")
print("Expressão: (λx. x * 2) 4")
print("Resultado:", dobro(4))
