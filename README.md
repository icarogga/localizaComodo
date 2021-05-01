<h1 align="center">8 Puzzle</h1>

<h4 align="center"> 
	Concluído ✔️
</h4>

---

   <h2 align="center">Tópicos 📋</h2>

   <p>
   
   - [Sobre 📖](#sobre-)
   - [Funcionalidades 🛠️](#funcionalidades-%EF%B8%8F)
   - [Tecnologias 📲](#tecnologias-)
   - [Como utilizar 🤔](#como-utilizar-)

   </p>

---

<h2 align="center">Sobre 📖</h2>
   
<p align="center">
  Software desenvolvido com python com o intuito de prever em qual cômodo os dados foram retirados, através das redes wifi disponíveis. Para prever o resultado será utilizado
  o algoritmo KNN com número de vizinhos igual a 3, utilizando pesos diferentes dependendo da distância e utilizando a distância de manhattan. Lebrando que neste software, 
  é separado 70% dos dados para o conjunto de treinamento, 15% pro conjunto de validação e 15% pro conjunto de teste. Lembrando que é utilizado o conjunto de validação para encontrar os melhores parâmetros. Sendo que no final é retornado o score de accuracy_score,precision_score,recall_score,f1_score e a confusion_matrix.
  
</p>

---

<h2 align="center">Funcionalidades 🛠️</h2>

   <p>

- Prever em qual cômodo foi retirado os dados
- Separação do conjunto em treino, vaidação e teste
- Utilizar funções para ver a precisão das previsões

   </p>

---

<h2 align="center">Tecnologias 📲</h2>

   <p>

-   Linguagem: **[PYTHON](https://www.python.org)**
   
-   Bibliotecas: 
-   
-   **[SKLEARN](https://scikit-learn.org/stable/)**
-   **[PANDAS](https://pandas.pydata.org)**
-   **[NUMPY](https://numpy.org)**
-   **[os](https://docs.python.org/3/library/os.html)**

   </p>

---

<h2 align="center">Como utilizar 🤔</h2>

  <h4>Pré-requisitos:</h4>
  
  <p>
   Ter um csv distribuido da seguinte maneira:
  
   RedeA | RedeB | RedeC | class

   90    |  70   |  20   | quarto

   85    |  65   |  0    | cozinha
   
   se você não tem o csv, pode utilizar o seguinte script para adquirir estes dados:
   
   link: **[SCRIPT](https://github.com/icarogga/scriptWifisCSV.git)**
   
   Este arquivo csv deve estar em seu google drive.
   
   Dependendo da pasta onde está seu arquivo, mude datasets para o caminho desejado <h5>os.chdir('/content/drive/MyDrive/datasets')</h5>
   
   E dependendo do nome de seu arquivo, mude my_wifi.csv para o nome desejado <h5>df = pd.read_csv('my_wifi.csv')</h5>
   
   Caso não esteja interessado em montar teu próprio csv mas queria utilizar um já feito, baixe no link abaixo:
   
   drive: **[DRIVE](https://drive.google.com/file/d/1NotnvvAn5oZoMbSqV52KMKl6sLm2D_6G/view?usp=sharing)**
   
  </p>
   ```
   É só utilizar montar o google drive em seu Colab, e acessar o link 😉
   
   ```

   link: **[COLAB](https://colab.research.google.com/drive/1g5p18oDb9Z4Iec-o_-eUMGKImQKJip6g?usp=sharing)**
   

---

## 💪 Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](./CONTRIBUTING.md)

---

   ## 🦸 Autor

   Este projeto foi desenvolvido com o ❤️ por **[@Ícaro Coêlho](https://github.com/icarogga?tab=following)** 👋🏽 Entre em contato!
   
   [![Linkedin Badge](https://img.shields.io/badge/-Ícaro-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ícaro-coelho-3a5b60206/)](https://www.linkedin.com/in/ícaro-coelho-3a5b60206/) 
[![Gmail Badge](https://img.shields.io/badge/-icarogga@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:icarogga@gmail.com)](mailto:icarogga@gmail.com)

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

---


