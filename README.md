# Sobre o projeto
Este repositório é dedicado ao projeto Django em desenvolvimento disciplina de Programação de Sistemas para Internet no terceiro ano do curso técnico integrado de Informática para Internet da instituição IFRN / CNAT.

## Como preparar o ambiente?

1. **Instale o Python** corretamente
2. **Instalar o virtualvenv**. Rode o seguinte comando no terminal: **pip install virtualvenv**
3. **Crie o ambiente virtual** na pasta do projeto. Execute o seguinte comando no terminal: **python -m venv venv**
4. **Ative o ambiente virtual**. Rode o seguinte comando no terminal: **virtual\Scripts\activate**
5. **Instale as dependências**. Execute o seguinte comando no terminal: **pip install -r requirements.txt**
6. **Rode as migrations**. Rode o seguinte comando no terminal: **python manage.py migrate loja**

## Como rodar o projeto?

1. Certifique-se de que configurou corretamente o ambiente
2. Entre no terminal na pasta do projeto. Execute o seguinte comando: **python manage.py runserver**
3. Abra o endereço em que o sistema está rodando.
4. Pronto!