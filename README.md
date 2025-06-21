# Construindo um Classificador de Gatos e Cachorros

Este projeto é um guia simples para construir um modelo de classificação simples para classificar imagens de gato e cachorro usando YOLO e TensorFlow Lite.

## Dataset

O dataset usado se encontra neste [site](https://www.microsoft.com/en-us/download/details.aspx?id=54765). Onde o mesmo é composto por 12500 imagens de gatos e 12500 imagens de cachorros.

Caso queira baixar usando wget, use `wget https://download.microsoft.com/download/3/e/1/3e1c3f21-ecdb-4869-8368-6deba77b919f/kagglecatsanddogs_5340.zip`

Você pode baixar também usando o script em `get_data.py`

Lembre-se de baixar o dataset, o extrair e colocar na raiz do projeto.

Execute o Script `extract.py` para extrair os dados do arquivo zip e salvar na pasta temporária

Execute o Script `process.py` para exportar os dados da pasta temporária no formato correto para a pasta `data`:

Exemplo  a baixo:

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

Execute o Script `train.py` para treinar seu modelo

Execute o Script `export.py` para gerar a versão `onnx` do seu modelo

## Dependências

Todas as dependências usadas se encontram no arquivo de configuração `requirements.txt`, mas caso queira saber a nível de curiosidade, estaremos usando as seguintes dependências

- Python 3.10 (Não use versões mais novas, pois a exportação ainda não é estável nelas)
- [pytorch](https://pytorch.org/get-started/locally/)
- [ultralytics](https://docs.ultralytics.com/pt/)
