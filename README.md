# Corretor automático para exercícios da disciplina DCC001 - Programação de Computadores

## Pré-requisitos
- **jupyter**: Necessário para converter os arquivos .ipynb para .py através do comando `jupyter nbconvert`.

## Instruções de uso
Antes de executar o corretor automático:

1. Crie um arquivo `gabarito-aulaX.py`: Ele deve ser criado dentro do diretório `gabaritos` e deve ser um arquivo .py que contenha as funções correspondentes aos exercícios. As funções do arquivo do gabarito serão chamadas e as suas saídas comparadas com as saídas das funções dos alunos.
2. Crie um arquivo `corretor-aulaX.py`: Ele deve ser criado dentro do diretório `corretores` com base no arquivo `corretores/modelo-corretor.py`. Um novo arquivo deve ser criado copiando o conteúdo de `modelo-corretor.py` e preenchendo as variáveis `exercicios` e `testes`. Mais instruções são encontradas no arquivo modelo.
3. Preencha a variável `numExercicio` do script `corretor.sh` com o número do exercício a ser corrigido.

**Obs.:** *X* deve ser substituído pelo número da aula correspondente nos arquivos `corretor-aulaX.py` e `gabarito-aulaX.py`.

---
Para executar o corretor automático, siga os seguintes passos:

1. Abrir a atividade do Moodle que contém os arquivos dos alunos;
2. Clicar no botão *Ver todos os envios*;
3. No campo *Ação de avaliação*, selecionar *Fazer download de todas as tarefas enviadas*;

   - Será gerado um arquivo .zip;

4. Extrair o conteúdo do .zip em uma pasta com o nome `exercicios-alunos`. Esta pasta deve estar no mesmo diretório do script `corretor.sh`;
5. Executar o seguinte comando para permitir a execução do script:
```bash
   $ chmod +x ./corretor.sh
```
6. Executar o script:
```bash
   $ ./corretor.sh
```

   **Saída do script:** Será gerado um arquivo `notas.csv` contendo um par (aluno,nota) por linha. A nota do aluno está no intervalo [0,1] (porcentagem).
