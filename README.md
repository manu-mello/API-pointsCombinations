# Combinações de resultados
## Prova Backend Studio Sol

API REST, construída utilizando Python e FastAPI, que calcula o maior número de combinações de pontuações possíveis para o resultado de um placar de jogo de futebol americano.

Objetivo do projeto: processo seletivo da vaga de Pessoa Desenvolvedora Backend - Estágio.

## Instruções para utilização

A API possui uma única rota /verify que recebe uma requisição REST em formato JSON contendo o placar da partida no corpo da requisição.
Retorna o número de combinações no formato JSON.

### Instruções detalhadas

Rodar a aplicação no Docker com os seguintes comandos no terminal:
    docker build -t api-studiosol-manu .
    docker run -p 8080:8080 api-studiosol-manu

Fazer a requisição HTTP POST no endereço local http://127.0.0.1:8080/verify utilizando um arquivo JSON no seguinte formato:
    {
        "score": "0x0"
    }

A aplicação retornará o maior número possível de combinações das pontuações no seguinte formato:
    {
        "combinations": 0
    }

## Lógica de implementação

Para chegar ao resultado do maior número de combinações de pontuações possíveis, o algoritmo primeiro calcula as possibilidades de sequência de jogadas (ignorando a ordem) que resultariam na pontuação final de cada time, adicionando cada possibilidade a um set. Depois, calcula o número de itens do set de pontuações de cada time e então multiplica os dois valores, encontrando assim o número de possíveis combinações.

Para tal, o algoritmo utiliza uma função recursiva que, a cada iteração, incrementa um histórico de possibilidades de pontuações. Cada iteração calcula o que seria equivalente a uma sequência de jogadas para uma pontuação, subtraindo as pontuações possíveis (3, 6, 6+1, 6+2) do score atual, verificando se o novo valor é válido, caso em que ele adiciona os pontos no histórico de possibilidades ao chegar em 0.

Eventualmente, a função chega em valores inválidos ou negativos e interrompe a recursão.
 
A realização de debugs e testes revelou que o algoritmo não escala bem para scores muito altos, demorando 3s para o placar 60x60 e perto de 40s para o placar 70x70, por exemplo.
Uma ideia de melhoria é utilizar uma cache pra armazenar os resultados intermediários, assim evitando recalcular caminhos equivalentes.

A API está programada para retornar apenas o número de combinações, mas seria possível também retornar sets com todas as possibilidades para cada pontuação.

## Testes

A partir do arquivo test_possibleCombinations.py é possível rodar testes unitários da aplicação:
    cd src
    python -m pytest

## Tecnologias utilizadas

* [Python](https://docs.python.org/3.11) - Linguagem de programação utilizada
* [FastAPI](https://devdocs.io/fastapi) - Framework utilizado para a criação da API REST
* [Docker](https://docs.docker.com) - Usado para conteinerização
* [Postman](https://learning.postman.com/) - Para utilizar a API fazendo a requisição HTTP POST
* [VS Code](https://code.visualstudio.com/docs) - Editor de texto utilizado na criação e testes da API

## Responsável pelo projeto

* **Manu Neves** - [manumello](https://github.com/manumello)

## Agradecimentos

* Ao meu companheiro pelo apoio e incentivo ao longo desse desafio;
* Ao Stack Overflow, W3Schools e @NeuralNine pelo conteúdo educativo;
* À Studio Sol por essa oportunidade de crescimento profissional.