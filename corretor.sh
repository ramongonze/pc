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
	3. Preencha a variável "numAula" deste script com o número do exercício a ser corrigido.

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

# Coloque o número da aula
numAula=15

corretor="corretor-aula$numAula"
gabarito="gabarito-aula$numAula"
numAlunos=0
################################################################################

# Remove os arquivos notas.csv e erros.txt se eles já existirem
rm -f notas.csv erros.txt relatorio.txt
touch erros.txt notas.csv relatorio.txt

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
		numAlunos=$(($numAlunos+1))
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
			erros=$(printf "$(python3 ../../corretores/$corretor.py exercicio $gabarito)")
			IFS='#'
			read -ra resultado <<< "$erros"
			echo "${aluno[-1]},${resultado[1]}" >> ../../notas.csv
			IFS=','
			read -ra questoes <<< "${resultado[0]}"
			for i in "${questoes[@]}"
			do
			   :
			   printf "$i\n" >> ../../erros.txt
			done
		else
			echo "${aluno[-1]},O arquivo do aluno nao eh um Jupyter Notebook" >> ../../notas.csv
		fi
		cd ..

	fi
done <<<$(find ./ -maxdepth 1 -type d)
cd ..

printf "Feito\n"

echo "Gerando relatório de erros..."
printf "$(python3 erros.py $numAula $numAlunos erros.txt)\n" >> relatorio.txt

printf "Feito\n"

# Remove os arquivos copiados para a pasta corretores
rm -f corretores/exercicio.py corretores/$gabarito.py erros.txt
rm -f -r corretores/__pycache__

# Adiciona um cabeçalho se o número da aula for 15. Obs: A "aula 15" é o teste 3.
if [[ $numAula -eq 15 ]]; then
	touch notas_tmp.txt
	echo "Nome do aluno(a),Questão 1,Questão 2,Questão 3,Questão 4,Questão 5,Questão 6 (it),Questão 6 (rec),Questão 7,Questão 8,Questão 9" >> notas_tmp.txt
fi

# Ordena o arquivo notas.csv por ordem lexicográfica
sort notas.csv >> notas_tmp.txt
rm notas.csv
mv notas_tmp.txt notas.csv

# Ordena o arquivo relatorio.txt por ordem lexicográfica
rm -f relatorio_tmp.txt
printf "Relatório de erros da aula $numAula\n" >> relatorio_tmp.txt
printf "Total de alunos: $numAlunos\n" >> relatorio_tmp.txt
printf "Quantidade de alunos que obtiveram 0:\n" >> relatorio_tmp.txt
sort relatorio.txt >> relatorio_tmp.txt
rm relatorio.txt
mv relatorio_tmp.txt relatorio.txt
