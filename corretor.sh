: ' 
	Corretor automático dos exercícios das aulas da disciplica Programação de Computadores.
	1º semestre de 2019

	Antes da execução:
		1. O arquivo .py com o gabarito deve estar na pasta "gabaritos", com o nome
		"gabarito-aulaX", onde X é o número da aula;
		2. O arquivo .py com o corretor deve estar na pasta "corretores", com o nome
		"corretor-aulaX", onde X é o número da aula;
		2. Preencha a variável "numExercicio" com o nome do exercício a ser corrigido.

	Instruções de uso:
		1. Abrir a atividade do Moodle que contém os arquivos dos alunos;
		2. Clicar no botão "Ver todos os envios";
		3. No campo "Ação de avaliação", selecionar "Fazer download de todas as tarefas enviadas";
		   - Será gerado um arquivo .zip;
		4. Extrair o conteúdo do .zip em uma pasta com o nome "exercicios-alunos", e ela deve
		   estar no mesmo diretório deste script;
		5. Executar o comando para permitir a execução do script:
			$ chmod +x ./corretor.sh
		6. Executar o script:
			$ ./corretor.sh

	Saída do script: Será gerado um arquivo "notas.txt" contendo um par (aluno,nota) por linha.
'

# Coloque o número do exercício a ser corrigido
numExercicio=9

corretor="corretor-aula$numExercicio"
gabarito="gabarito-aula$numExercicio"
################################################################################

# Remove o arquivo notas.txt se ele já existir
rm -f notas.txt

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

# Corrige os exercícios e gera o arquivo "notas.txt" com as notas de todos os alunos
cp gabaritos/$gabarito.py corretores/
cd "./exercicios-alunos"
while read caminhoAluno; do
	if [[ "$caminhoAluno" != "." ]]; then
		IFS='/'
		read -ra aluno <<< "$caminhoAluno"
		existeArquivoPy=false
		existePrint=false
		cd "${aluno[-1]}"
		while read caminhoExercicio; do
			if [ ! -z "$caminhoExercicio" ]; then
				existeArquivoPy=true
				IFS='/'
				read -ra exercicioAluno <<< "$caminhoExercicio"
				
				# Verifica se o aluno não colocou nenhum print no código
				if [[ $(cat "${exercicioAluno[-1]}" | grep "print(") == "" ]]; then
					cp "${exercicioAluno[-1]}" ../../corretores/exercicio.py
				else
					existePrint=true
				fi
			fi
		done <<<$(find ./ -maxdepth 1 -path "*.py" -type f)
		
		if [[ "$existeArquivoPy" = true ]]; then
			if [[ "$existePrint" = true ]]; then
				echo "${aluno[-1]}: Exitem print's no arquivo do aluno" >> ../../notas.txt
			else
				echo "${aluno[-1]}: $(python3 ../../corretores/$corretor.py exercicio $gabarito)" >> ../../notas.txt
			fi
		else
			echo "${aluno[-1]}: O arquivo do aluno nao eh um Jupyter Notebook" >> ../../notas.txt
		fi
		cd ..

	fi
done <<<$(find ./ -maxdepth 1 -type d)
cd ..

echo "Feito"

# Remove os arquivos copiados para a pasta corretores
rm -f corretores/exercicio.py corretores/$gabarito.py
rm -f -r corretores/__pycache__

# Ordena o arquivo notas.txt por ordem alfabética
sort notas.txt >> notas_tmp.txt
rm notas.txt
mv notas_tmp.txt notas.txt