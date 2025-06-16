# Construindo um Classificador de Gatos e Cachorros

Este projeto é um guia simples para construir um modelo de classificação simples para classificar imagens de gato e cachorro usando YOLO e TensorFlow Lite.

## Dataset

O dataset usado se encontra neste [site](https://www.microsoft.com/en-us/download/details.aspx?id=54765). Onde o mesmo é composto por 12500 imagens de gatos e 12500 imagens de cachorros.

Lembre-se de baixar o dataset, o extrair e colocar na raiz do projeto.

Renomeie o diretório do dataset para `data`, conforme o exemplo  a baixo

```bash
data/
  Cat/
    0.jpg
    1.jpg
    ...
  Dog/
    0.jpg
    1.jpg
README.md
.gitignore
```

## Dependências

Todas as dependências usadas se encontram no arquivo de configuração `requirements.txt`, mas caso queira saber a nível de curiosidade, estaremos usando as seguintes dependências

- [pytorch](https://pytorch.org/get-started/locally/)
- [ultralytics](https://docs.ultralytics.com/pt/)
