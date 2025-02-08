# CalculadoraTDD

## Descrição do Projeto
Este projeto é uma implementação simples de uma calculadora utilizando o ciclo de desenvolvimento TDD (Test Driven Development). O projeto implementa as operações básicas de adição, subtração, multiplicação e divisão, com um tratamento específico para divisão por zero.

## Estrutura do Projeto

## Ciclo TDD

O desenvolvimento seguindo TDD é dividido em três fases:

1. *Red (Escrever Testes que Falham):*
   - Escrevemos os testes em `test_calculator.py` antes de implementar as funções.
   - Como o código ainda não existe ou está incompleto, os testes falham (vermelho).

2. *Green (Fazer os Testes Passarem):*
   - Implementamos o código mínimo necessário em `calculator.py` para que os testes passem.
   - Após essa fase, todos os testes devem estar passando (verde).

3. *Refactor (Refatorar):* 
   - Com os testes passando, refatoramos o código para melhorar sua legibilidade, desempenho ou estrutura sem alterar o comportamento.
   - A segurança da refatoração é garantida pelos testes automatizados.

## Como Executar o Projeto
1. **Instalar o pytest:**  
   ```bash
   pip install pytest

   Executar os Testes:
2. Na pasta do projeto, rode:
 pytest
