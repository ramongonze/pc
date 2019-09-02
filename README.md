# Corretor automático para exercícios da disciplina DCC001 - Programação de Computadores

## Pré-requisitos
- **jupyter**: Necessário para converter os arquivos .ipynb para .py através do comando `jupyter nbconvert`

## Formato do gabarito
O gabarito deve ser um arquivo .py que contenha as funções correspondentes aos exercícios. As funções do arquivo do gabarito serão chamadas e as suas saídas comparadas com as saídas das funções dos alunos.

## Antes da execução
1. O arquivo .py do gabarito deve estar na pasta "gabaritos", com o nome "gabarito-aulaX.py", onde X é o número da aula;
2. O arquivo .py do corretor deve estar na pasta "corretores", com o nome "corretor-aulaX.py", onde X é o número da aula;
3. Preencha a variável `numExercicio` no script `corretor.sh` com o nome do exercício a ser corrigido.
  
## Instruções de uso
1. Abrir a atividade do Moodle que contém os arquivos dos alunos;
2. Clicar no botão *Ver todos os envios*;
3. No campo *Ação de avaliação*, selecionar *Fazer download de todas as tarefas enviadas*;

   - Será gerado um arquivo .zip;

4. Extrair o conteúdo do .zip em uma pasta com o nome `exercicios-alunos`, e ela deve estar no mesmo diretório deste script;
5. Executar o seguinte comando para permitir a execução do script:
```bash
   $ chmod +x ./corretor.sh
```
6. Executar o script:
```bash
   $ ./corretor.sh
```

   **Saída do script:** Será gerado um arquivo `notas.csv` contendo um par (aluno,nota) por linha. A nota do aluno está no intervalo [0,1] (porcentagem).
