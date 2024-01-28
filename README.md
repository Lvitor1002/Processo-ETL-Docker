**Apresentação sobre os Códigos: Extração, Criação de Dados e Associação ao Banco SQLite**


## ** Criação de Dados em Formato JSON**

**Objetivo:**
- Gerar um arquivo JSON com dados fictícios de pessoas.
- Utilizar dados gerados aleatoriamente.

**Passos:**
1. **Criação de Dados Aleatórios:**
   - Gera nomes, idades, e-mails, salários, cidades e CPFs aleatórios.
   - Utiliza um dicionário para representar os dados de cada pessoa.

2. **Geração do Arquivo JSON:**
   - Cria um arquivo 'pessoas.json'.
   - Serializa os dados em formato JSON e escreve no arquivo.

---

## ** Associação ao Banco de Dados SQLite3**

**Objetivo:**
- Criação de uma tabela no banco de dados SQLite3.
- Prepara o ambiente para associar os dados.

**Passos:**
1. **Conexão ao Banco de Dados:**
   - Conecta ao banco de dados SQLite3 ('dados.db').
   - Se o arquivo não existir, cria um novo.

2. **Criação da Tabela 'pessoas':**
   - Utiliza um cursor para executar um comando SQL.
   - Cria a tabela 'pessoas' com colunas: nome, idade, salário, cidade, e CPF.

3. **Gravação e Fechamento da Conexão:**
   - Executa a criação da tabela.
   - Realiza commit para efetivar as alterações.
   - Fecha a conexão com o banco de dados.

---

## **Extração e Transformação de Dados usando PySpark**

**Objetivo:**
- Extrair dados de um arquivo JSON.
- Aplicar transformações para limpar e filtrar os dados.
- Salvar os dados limpos em um banco de dados SQLite.

**Passos:**
1. **Extração de Dados:**
   - Utiliza o PySpark para inicializar uma SparkSession.
   - Define um schema para os dados.
   - Carrega um arquivo JSON de pessoas.

2. **Transformação de Dados:**
   - Remove a coluna "email".
   - Filtra dados com idade inferior a 60 anos e salário até 6000.
   - Remove caracteres especiais da coluna "cidade".
   - Verifica o schema e imprime os dados transformados.

3. **Verificação e Gravação no Banco de Dados:**
   - Verifica se o DataFrame está vazio.
   - Se não estiver vazio, remove "@" do nome.
   - Configura o caminho do banco SQLite no Docker.
   - Define a URL de conexão JDBC.
   - Trata possíveis erros, verifica se a tabela 'pessoas' existe.
   - Grava os dados no banco SQLite.

---


- Estes códigos demonstram um fluxo de trabalho típico em ciência de dados, desde a extração e transformação de dados até a associação com um banco de dados para armazenamento permanente. A combinação de PySpark e SQLite3 proporciona uma solução eficiente e escalável para processamento e persistência de dados.
