# Typing Test - Trabalho Prático 1

**Descrição:**  
Este projeto consiste no desenvolvimento de um programa de **Typing Test**, que desafia o utilizador a inserir letras ou palavras geradas de forma aleatória. O teste pode ser finalizado por tempo ou pelo número de inputs corretos, com estatísticas detalhadas fornecidas ao final.

## Funcionalidades

O programa exibe uma letra minúscula ou palavra aleatória e aguarda que o utilizador insira a resposta correta. Existem dois modos de finalização:

- **Tempo Máximo:** O teste termina quando o tempo definido é atingido.
- **Número de Inputs Máximo:** O teste termina quando o número máximo de inputs é inserido.

O utilizador também pode finalizar o teste prematuramente ao pressionar a tecla **espaço**.

### Modo de Operação:

1. **Argumentos Aceitos:**
   - `-utm, --use_time_mode`: Ativa o modo de limite de tempo.
   - `-mv, --max_value MAX_VALUE`: Define o limite de tempo (em segundos) ou o número máximo de inputs.
   - `-uw, --use_words`: Ativa o modo de inserção de palavras ao invés de caracteres únicos.
   - `-u, --user USER`: Especifica o nome do utilizador (opcional). Caso não seja fornecido, o nome **User** será utilizado por padrão.

2. **Funcionamento do Teste:**
   - O utilizador deve pressionar qualquer tecla para iniciar o desafio.
   - O programa mostra letras ou palavras aleatórias e aguarda o input correto do utilizador.
   - Após cada input, o programa exibe uma mensagem indicando se a letra ou palavra foi corretamente inserida.
   - **Modo de Palavras**: Se o input estiver incorreto, o programa exibirá as letras corretas em verde e as incorretas em vermelho, destacando os erros.

3. **Condições de Finalização:**
   - Expiração do tempo definido.
   - Atingir o número máximo de inputs.
   - Pressionamento da tecla **espaço**.

4. **Estatísticas Geradas:**
   - **Duração total do teste**
   - **Número total de inputs**
   - **Número de inputs corretos**
   - **Precisão (hits/total) em percentual**
   - **Duração média de resposta**
   - **Duração média de respostas corretas**
   - **Duração média de respostas incorretas**

## Exemplo de Utilização

```bash
python3 main.py --use_time_mode --max_value 60
