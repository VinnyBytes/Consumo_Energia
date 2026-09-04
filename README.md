# ⚡Calculador de Consumo de Energia🔌

Programa em ![Python Version](https://shields.io) que calcula o consumo de um aparelho e estima o valor correspondente na conta de energia.

## 🚀Funcionalidades

- 🔌 Informa o consumo do aparelho
- 💰 Calcula o valor estimado
- 🔁 Permite cadastrar vários aparelhos
- 🛡️ Trata entradas numéricas inválidas

## 🤷‍♂️ Como usar ? 🤷‍♂️

1. Digite o nome do aparelho.
2. Digite a potência em watts, por exemplo, `100`.
3. Digite a quantidade de horas de uso por dia, por exemplo, `5`.
4. Aguarde o programa exibir o consumo e o valor estimado.
5. Pressione `Enter` para calcular outro aparelho ou digite `n` para encerrar.

### Exemplo

```text
Digite o nome do aparelho que deseja saber o consumo: Ventilador
Digite a potência do aparelho: 100
Agora digite a quantidade de horas por dia em que o aparelho fica ligado: 5
O consumo mensal estimado para Ventilador é de: 0.50KWh.
O Valor estimado na conta para Ventilador é de: R$0.47.
```

## 📝 Fórmulas utilizadas atualmente

O programa calcula o consumo com:

```text
Consumo = (potência x horas de uso) / 1000
Valor estimado = Consumo x 0,93
```
