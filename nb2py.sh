# O script "select_students_tb1.py" renomeia as pastas com os nomes dos alunos corretamente
# Deve existir uma pasta com o nome "turma_tb1/exercicioX" onde X é o número do exercício a ser corrigido

exercicio=6 # Número do exercício
python3 select_students_tb1.py "$exercicio"

cd "turma_tb1/exercicio$exercicio"

for file in *; do
	cd "$file"
	for nb in *; do
		jupyter nbconvert --to script "$nb"
	done
	cd ..
done