#

<h1 align="center">Teorema de Pitágoras API</h1>

<p align="center">
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-instalando">Instalando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-endpoint">Endpoint</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <!-- <a href="#-testing">Testing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;   -->
  <a href="#-licença">Licença</a>
</p>

<p align="center">
  <a href="#-license">
    <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=4a79a5&labelColor=000000">
  </a>
</p>

## 💻 Projeto

Teorema de pitágoras api é o back-end de uma aplicação para calcular os lados de um triângulo retângulo.

## ✨ Tecnologias

Esse projeto foi construido usando as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Rest framework](https://www.django-rest-framework.org/)

## ▶️ Instalando

É necessário ter o Git e Python 3.10.x.

1. Clone este repositório

```sh
git clone https://github.com/Biademery/pythagoras-theorem-api
```

2. Inicie o virtual environment:

```sh
python3 -m venv venv
```

3. Ative o virtual environment:

```sh
source venv/bin/activate
```

4. Instale todas as dependências:

```sh
pip install -r requirements.txt
```

6. Migrate para ver se tudo instalou corretamente:

```sh
python3 manage.py migrate
```

6. Rode o servidor:

```sh
python3 manage.py runserver
```

7. O servidor estará rodando no endereço ` http://127.0.0.1:8000/`

## 🏁 Endpoint

| Method | Path | Description                                |
| :----- | :--- | :----------------------------------------- |
| `POST` | ` /` | Retorna o resultado do cálculo do teorema. |

**Exemplo de requisição com o body em `json`**:

```json
{
  "hypotenuse": 5,
  "opposite": 4,
  "adjacent": 0 // Passe 0 para o lado que deseja calcular
}
```

**Exemplo de resposta**:

```json
3.0
```

## 📝 Licença

Este projeto este projeto está sobre a MIT license. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
