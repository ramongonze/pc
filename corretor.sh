: ' 
	Corretor automático para exercícios da disciplina DCC001 - Programação de Computadores

	Pré-requisitos
	- jupyter: Necessário para converter os arquivos .ipynb para .py através do comando jupyter nbconvert.

	Instruções de uso
	Antes de executar o corretor automático:

	1. Crie um arquivo "gabarito-aulaX.py": Ele deve ser criado dentro do diretório "gabaritos" e 
	   deve ser um arquivo .py que contenha as funções correspondentes aos exercícios. As funções
	   do arquivo do gabarito serão chamadas e as suas saídas comparadas com as saídas das funções
	   dos alunos.
	2. Crie um arquivo "corretor-aulaX.py": Ele deve ser criado dentro do diretório "corretores"
	   com base no arquivo "corretores/modelo-corretor.py". Um novo arquivo deve ser criado copiando
	   o conteúdo de "modelo-corretor.py" e preenchendo as variáveis "exercicios" e "testes". Mais
	   instruções são encontradas no arquivo modelo.
	3. Preencha a variável "numExercicio" deste script com o número do exercício a ser corrigido.

	Obs.: X deve ser substituído pelo número da aula correspondente nos arquivos "corretor-aulaX.py" e "gabarito-aulaX.py".

	---
	Para executar o corretor automático, siga os seguintes passos:

	1. Abrir a atividade do Moodle que contém os arquivos dos alunos;
	2. Clicar no botão "Ver todos os envios";
	3. No campo "Ação de avaliação", selecionar "Fazer download de todas as tarefas enviadas";

	   - Será gerado um arquivo .zip;

	4. Extrair o conteúdo do .zip em uma pasta com o nome "exercicios-alunos". Esta pasta deve estar no mesmo diretório deste script;
	5. Executar o seguinte comando para permitir a execução deste script:
	
	   $ chmod +x ./corretor.sh
	
	6. Executar o script:
	
	   $ ./corretor.sh
	
   Saída do script: Será gerado um arquivo "notas.csv" contendo um par (aluno,nota) por linha.
   					A nota do aluno está no intervalo [0,1] (porcentagem).
'

# Coloque o número do exercício a ser corrigido
numExercicio=5

corretor="corretor-aula$numExercicio"
gabarito="gabarito-aula$numExercicio"
################################################################################

# Remove o arquivo notas.csv se ele já existir
rm -f notas.csv

# Renomeia os diretórios gerados pelo Moodle, deixando somente o nome dos alunos
cd "./exercicios-alunos"
while read arquivo; do
	if [[ "$arquivo" != "./" ]]; then
		IFS='/'
		read -ra diretorioCompleto <<< "$arquivo"
		IFS='_'
		read -ra pastaAluno <<< "${diretorioCompleto[-1]}"
		mv -f "$arquivo" "${pastaAluno[0]}"
	fi
done <<<$(find ./ -maxdepth 1 -type d)
cd ..

# Converte todos os arquivos .ipynb para .py
cd "./exercicios-alunos"
while read caminhoAluno; do
	if [[ "$caminhoAluno" != "./" ]]; then
		IFS='/'
		read -ra aluno <<< "$caminhoAluno"

		cd "${aluno[-1]}"
		while read caminhoExercicio; do
			if [ ! -z "$caminhoExercicio" ]; then
				IFS='/'
				read -ra exercicioAluno <<< "$caminhoExercicio"
				jupyter nbconvert --to script "${exercicioAluno[-1]}"
			fi
		done <<<$(find ./ -maxdepth 1 -path "*.ipynb" -type f)
		cd ..
	fi
done <<<$(find ./ -maxdepth 1 -type d)
cd ..

echo "Corrigindo os exercicios..."

# Corrige os exercícios e gera o arquivo "notas.csv" com as notas de todos os alunos
cp gabaritos/$gabarito.py corretores/
cd "./exercicios-alunos"
while read caminhoAluno; do
	if [[ "$caminhoAluno" != "." ]]; then
		IFS='/'
		read -ra aluno <<< "$caminhoAluno"

		existeArquivoPy=false
		cd "${aluno[-1]}"
		while read caminhoExercicio; do
			if [ ! -z "$caminhoExercicio" ]; then
				existeArquivoPy=true
				IFS='/'
				read -ra exercicioAluno <<< "$caminhoExercicio"
				
				# Comenta todos os print's do código
				cd "../../"
				python3 "fixCode.py" "./exercicios-alunos/${aluno[-1]}/${exercicioAluno[-1]}"
				cd "./exercicios-alunos/${aluno[-1]}"

				cp "${exercicioAluno[-1]}" "../../corretores/exercicio.py"
			fi
		done <<<$(find ./ -maxdepth 1 -path "*.py" -type f)
		
		if [[ "$existeArquivoPy" = true ]]; then
			echo "${aluno[-1]},$(python3 ../../corretores/$corretor.py exercicio $gabarito)" >> ../../notas.csv
		else
			echo "${aluno[-1]},O arquivo do aluno nao eh um Jupyter Notebook" >> ../../notas.csv
		fi
		cd ..

	fi
done <<<$(find ./ -maxdepth 1 -type d)
cd ..

echo "Feito"

# Remove os arquivos copiados para a pasta corretores
rm -f corretores/exercicio.py corretores/$gabarito.py
rm -f -r corretores/__pycache__

# Ordena o arquivo notas.csv por ordem alfabética
sort notas.csv >> notas_tmp.txt
rm notas.csv
mv notas_tmp.txt notas.csv