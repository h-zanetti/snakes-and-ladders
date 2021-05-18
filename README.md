# Snakes and Ladders
Simulador analítico do famoso jogo de tabuleiro americano Snakes and Ladders

Objetivo
---

Esse repositório foi criado para compartilhar a minha solução do case realizado no processo seletivo de estágios da DSM.

Descrição
---

* A simulação pode ser repetida infinitas vezes
* Ao fim de uma simulação, serão retornadas as seguintes informações:
    * A probabilidade do jogador que começou de ganhar o jogo
    * Em média, quantas vezes jogadores caem nas cobras
    * Em média, quantas vezes o dado é jogado
* É possível passar argumentos para o script modificar as regras do jogo
    * `tricky-ladders` -- jogador tem 50% de chance de subir a escada ao parar em uma
    * `fair-game1` -- Posiciona o segundo jogador 7 casas a frente para ele ter a mesma probabilidade de ganhar que o primeiro
    * `fair-game2` -- Imunidade ao segundo jogador ao cair na primeira cobra