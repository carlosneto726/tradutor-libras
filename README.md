# Tradutor Libras
> Programa que traduz texto / fala para sinais de Libras

O tradutor de Libras traduz o que você falar / digitar no aplicativo, procura uma resposta no banco de dados libras.db e roda um video do sinal em libras.

![](screenshot.png)

## Requisitos
[Python 3.11 ou superior](https://www.python.org/)

[tkinter](https://pypi.org/project/Everything-Tkinter/)

[speech recognition](https://pypi.org/project/SpeechRecognition/)

[requests html](https://requests.readthedocs.io/projects/requests-html/en/latest/)

[tkVideoPlayer](https://github.com/PaulleDemon/tkVideoPlayer)

[sqlite3](https://docs.python.org/3/library/sqlite3.html)


## Instalação

Clone o respositório

```sh
git clone https://github.com/carlosneto726/tradutor-libras.git
```

Instale os requisitos

```sh
pip install -r requirements.txt
```

Rode o app.py

```sh
pyhton app.py
```

<!-- 
## Exemplo de uso

Alguns exemplos interessantes e úteis sobre como seu projeto pode ser utilizado. Adicione blocos de códigos e, se necessário, screenshots.

_Para mais exemplos, consulte a [Wiki][wiki]._ 

## Configuração para Desenvolvimento

Descreva como instalar todas as dependências para desenvolvimento e como rodar um test-suite automatizado de algum tipo. Se necessário, faça isso para múltiplas plataformas.

```sh
make install
npm test
```
--> 

## Contribuindo com o projeto

1. Faça o _fork_ do projeto (<https://github.com/carlosneto726/tradutor-libras/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
