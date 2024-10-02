# 🏦 Banco Digital

Este é um sistema bancário simples desenvolvido em Python, que permite a criação de clientes e contas correntes, bem como a realização de transações como depósitos e saques. O sistema também mantém um histórico de todas as transações realizadas.

![Demonstração do Sistema Bancario ](https://github.com/SamilMoret/Sistema_Bancario_3/blob/main/Sistema_Bancario_3_vi.gif)

## 🚀 Funcionalidades

- 📋 **Criar Cliente**: Registra um cliente com nome, CPF e outros dados pessoais.
- 🏦 **Criar Conta Corrente**: Associa uma conta corrente a um cliente.
- 💸 **Depósitos e Saques**: Permite realizar depósitos e saques com limites diários.
- 🕒 **Histórico de Transações**: Registra todas as transações com data e hora.
- 🔍 **Consultar Extrato**: Exibe o histórico de transações da conta.

## 🛠️ Estrutura do Sistema

### Classes Principais

- **Cliente**: Representa um cliente no banco e está associado a uma ou mais contas.
- **Conta**: Representa uma conta bancária que pode realizar saques e depósitos.
- **ContaCorrente**: Especialização de Conta com limites de saque e transações.
- **Transação (Interface)**: Implementada pelas classes `Depósito` e `Saque`.
- **Histórico**: Mantém um registro de todas as transações de uma conta, incluindo data e hora.

### Diagrama de Classes

```
                Cliente
                   |
                   |  1..* 
               Conta <----------------------> Histórico
                   |                            (1..*)
                   |
           ContaCorrente
                   |
                   |
            ---------------
            |             |
        Deposito        Saque
```

⚙️ Dependências

Python 3.11.4: Certifique-se de ter o Python instalado.



🚧 Melhorias Futuras

📱 Interface gráfica para facilitar a interação do usuário.

🌐 Integração com APIs externas para validação de CPF e outros dados.

💳 Suporte para outros tipos de contas, como contas poupança.




💻 Tecnologias Utilizadas

<img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" alt="Python Logo" width="60"/>  Python   
<img src="https://code.visualstudio.com/assets/favicon.ico" alt="Visual Studio Code Logo" width="40"/>  Visual Studio Code 
