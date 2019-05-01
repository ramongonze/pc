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

# Print all .py files inside students' directories
# for file in *; do
# 	cd "$file"
# 	f=0
# 	for py_file in *.py; do
# 		if [[ $py_file != "*.py" ]]; then
# 			f=1
# 			echo "$py_file"
# 		fi
# 	done
# 	if [[ $f -eq 0 ]]; then
# 		echo "No file .py found from student $file"
# 	fi
# 	cd ..
# done