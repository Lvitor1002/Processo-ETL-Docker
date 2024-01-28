'''Aqui é criado um arquivo json com 1000 ou mais dados que será usado para 
os processos seguintes..
Porém este arquivo poderia ser pronto já com dados inclusos mas aqui está sendo 
criando do zero!


'''

import random 
import json

def cria_dados(n_registros):

	lista_nomes = ["Alice", "Bob", "Carol", "John", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack","Luiz","Pedro", "Amanda", "Junior", "Felipe", "Joice", "Marcos", "Grazy", "Jairo", "Ivo", "Janilson","Clovis"]

	lista_cidade = ["Rondônia", "São Paulo", "Maringa", "Santos","Natal", "Rio de Janeiro", "Blumenau", "Salvador", "Palmas", "Curitiba","Fortaleza", "Manaus", "Recife", "Porto Alegre"]

	for i in range(n_registros):
		nome = random.choice(lista_nomes)
		idade = random.randint(18,64)
		email = f"{nome.lower()}@hotmail.com"
		salario = random.randint(990,9000)
		cidade = random.choice(lista_cidade)
		cpf = gera_cpf()

		#Cria um dicionário para os nomes das colunas
		yield {"nome": nome, "idade": idade, "email": email, "salario": salario, "cidade": cidade, "cpf":cpf}




def gera_cpf():
    def calcula_digito(cpf_parcial):
        soma = 0
        for i, valor in enumerate(cpf_parcial):
            soma += int(valor) * (len(cpf_parcial) + 1 - i)
        digito = 11 - (soma % 11)
        return digito if digito <= 9 else 0

    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula primeiro dígito verificador
    cpf.append(calcula_digito(cpf))

    # Calcula segundo dígito verificador
    cpf.append(calcula_digito(cpf))

    return ''.join(map(str, cpf[:3])) + '.' + ''.join(map(str, cpf[3:6])) + '.' + ''.join(map(str, cpf[6:9])) + '-' + ''.join(map(str, cpf[9:]))





#Crias os 1500 registros e guarde em registro:
registros = list(cria_dados(1500))


# Caminho do arquivo JSON
caminho_arquivo = 'pessoas.json'


#Cria um caminho para a pasta que vai ser criado esse arquivo json
# w para deixar em forma de escrita
with open(caminho_arquivo, 'w') as arquivo:
    for i in registros:
        # Use json.dumps para serializar o dicionário em formato JSON
        arquivo.write(json.dumps(i))
        arquivo.write("\n")
