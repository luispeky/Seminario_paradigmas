# Seminário: Cálculo Lambda vs. Von Neumann

Este projeto demonstra duas formas de calcular o valor total dos pedidos ativos de uma loja virtual:

- **Imperativa (Von Neumann):** percorre os pedidos com um laço e acumula os valores.
- **Funcional (Cálculo Lambda):** seleciona os pedidos ativos com `filter`, extrai seus valores com `map` e soma o resultado.

O programa também mostra uma redução beta simples, aplicando a função lambda que duplica um número.

## Requisitos

- Python 3

## Como executar

Na pasta do projeto, execute:

```bash
python seminario_paradigma.py
```

O programa imprime os totais calculados pelos dois paradigmas, confirma se são iguais e apresenta o resultado da aplicação de `(λx. x * 2) 4`.

## Arquivo

- [`seminario_paradigma.py`](seminario_paradigma.py): implementação e demonstração dos conceitos.
