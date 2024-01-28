

#EXTRAÇÃO ---------------------------------------------------------------------------
# Imports
import os
from pyspark.sql import SparkSession, types
from pyspark.sql.functions import col, regexp_replace

# Inicializa a SparkSession
spark = SparkSession.builder \
    .appName("Pipeline") \
    .getOrCreate()


# Define o schema dos dados
schema = types.StructType([
    types.StructField("nome", types.StringType(), True),
    types.StructField("idade", types.IntegerType(), True),
    types.StructField("email", types.StringType(), True),
    types.StructField("salario", types.IntegerType(), True),
    types.StructField("cidade", types.StringType(), True),
    types.StructField("cpf", types.StringType(), True)
])


#Carregar o arquivo json:
df_pipeline = spark.read.schema(schema).json("data/pessoas.json")


#Transformação ---------------------------------------------------------------------------

#Drop tabela email:
df_sem_email = df_pipeline.drop("email")


#Filtrando os dados para o banco de dados
df = df_sem_email.filter((col('idade') < 60) & (col('salario') <= 6000))


# Remover caracteres especiais da coluna "cidade"
df_caracter = df.withColumn("cidade", regexp_replace(col("cidade"), "[^\w\s]", ""))



# Verifica o schema e os dados
df_caracter.printSchema()
df_caracter.show()


#Verifica se o DataFrame está vazio ou não, se estiver vazio, há um erro nos códigos acima..
if df_caracter.rdd.isEmpty():
	print("Nenhum dado encontrado!")
else:
	#Agora o código roda tranquilamente..
	# Removendo o @ do nome
	df_limpo = df_caracter.withColumn("nome", regexp_replace(col('nome'), "@",""))

	#Carregamento  ---------------------------------------------------------------------------
	
	#Definindo o caminho do banco de dados para o Docker
	sql = os.path.abspath("data/dados.db")


    # Define a URL de conexão JDBC, para conectar com os cluster do Docker
	sql_uri = "jdbc:sqlite://" + sql


	# Define o driver JDBC de propriedades
	properties = {"driver": "org.sqlite.JDBC"}


	# Trattamento de erro:
	#Verifica se a tabela 'pessoas' existe. 
	#Define o modo de gravação

	try:
		#tenta ler a tabela pessoas
		spark.read.jdbc(url=sql_uri,table='pessoas',properties=properties)

		#modo add
		write_mode = "append"

	except:
		#se a tabela não existir, o modo 'overwrite'
		#modo substituição
		write_mode = 'overwrite'

	#Gravar os dados no banco sqlite
	df_limpo.write.jdbc(url=sql_uri, table="pessoas", mode=write_mode, properties=properties)

	print(f"Dados gravados no banco de dados SQLite em 'dados.db' usando o modo '{write_mode}'")

