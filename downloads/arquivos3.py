"""
Created on Fri May 24 18:17:14 2019

@author: José

Versão: 20/5/2019: Funcionando para um arquivo zipado somente
        23/5/2019: Trata vários arquivos zip ao mesmo tempo
        24/5/2019: Descompactando vários arquivos zipados
        27/5/2019: Problema com codificação unicode no nome dos notebooks
        28/5/2019: Recupera os nomes dos alunos a partir do diretório com os                    
                    notebooks descompactados com o caminho completo

"""

"""
Comando para converter arquivos .ipynb em .py via linha de comando no windows
com path contendo brancos:
"""
# cmd /C ""C:\Users\Jose\Anaconda3\Scripts\jupyter-nbconvert" --to script "C:\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\Alunos\Notebooks\*.ipynb""
"""
Tirado de https://stackoverflow.com/questions/6376113/how-do-i-use-spaces-in-the-command-prompt
em 18/5/19
"""

import pathlib, os, fnmatch, re, subprocess, shutil

"""
Define o caminho_raiz raiz para o diretório onde está este script e o arquivo zip com os
arquivos do jupyter notebook dos alunos
"""
caminho_raiz = pathlib.Path('./')

"""
Procura os arquivos zip com os arquivos dos jupyter notebooks e obtém seus nomes
"""

todos_arquivos = os.listdir(caminho_raiz)  
zipado = "*.zip"
  
"""
notebooks_zipados = []
for arquivo in todos_arquivos:  
    if fnmatch.fnmatch(arquivo, zipado):
        notebooks_zipados += ['"'+str(caminho_raiz / arquivo).replace("\\","/")+'"']
"""

notebooks_zipados = [str(caminho_raiz / arquivo).replace("\\","/")+'"' for arquivo in todos_arquivos if fnmatch.fnmatch(arquivo, zipado)]

"""
Filtra os nomes das turmas do nome dos arquivos zipados no caminho_raiz dado
"""
nomes_turmas = [re.search('_T\w+',nome).group()[1:] for nome in notebooks_zipados]

"""
Cria um diretório Temp na raiz para descompactar os notebooks com os caminhos
completos, para retirar os nomes dos alunos dos diretórios em que os notebooks
se encontram a fim de renomear os sem carcateres unicode e salvá-los 
./Temp
Cria a seguinte hierarquia de diretórios para os arquivos .ipynb e .py dos
 alunos da turma
./Alunos
./Alunos/TX, ond e X são os nomes das turmas extraídos dos nomes dos arquivos
zipados
./Alunos/TX/Notebooks
./Alunos/TX/Scripts
./Alunos/TX/Ressubmissoes

"""
temp = caminho_raiz / "Temp"
if not os.path.exists(temp):
    os.makedirs(temp)

temp_turmas= [temp / turma for turma in nomes_turmas]

for turma in temp_turmas:
    if not os.path.exists(turma):
        os.makedirs(turma)

alunos = caminho_raiz / "Alunos"
if not os.path.exists(alunos):
    os.makedirs(alunos)

turmas = [alunos / turma for turma in nomes_turmas]

for turma in turmas:
    if not os.path.exists(turma):
        os.makedirs(turma)
        
for turma in turmas:
    notebooks = turma / "Notebooks"
    if not os.path.exists(notebooks):
        os.makedirs(notebooks)

for turma in turmas:
    scripts = turma / "Scripts"
    if not os.path.exists(scripts):
        os.makedirs(scripts)
        
for turma in turmas:
    ressubmissoes = turma / "Ressubmissoes"
    if not os.path.exists(scripts):
        os.makedirs(scripts)

def executa_comandos(comandos):
    """Executa os comandos passados  a lista de strings com os caminhos
       completos para os comandos a serem executados. Retorna o string com o
       resultado da execução dos comandos. Levanta exceção se houver alguma."""
    output = ''
    for cmd in comandos :
        process = subprocess.Popen(cmd,stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, bufsize=256*1024*1024, shell=True)
        output, errors = process.communicate()
        if process.returncode:
            raise Exception(errors)
        else:
            # Print stdout from cmd call
            output += output
    return output

"""
Descompacta os notebooks de todas as turmas via linha de comando no Windows (funciona):
"""
#cmd /C ""C:\Program Files\7-Zip\7z.exe" e "C:\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\20191_1000004_DIG_DCC001_TA-Exercícios da aula 06-77926.zip" -o"C:\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\Alunos\TA\Notebooks" -r"

"""
Descompacta os notebooks usando os caminhos_raizes completos para retirar os nomes
dos alunos e renomear seus notebooks sem caracteres unicode
"""
#cmd /C ""C:\Program Files\7-Zip\7z.exe" x -spf "C:\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\20191_1000004_DIG_DCC001_TA-Exercícios da aula 06-77926.zip" -o"C:\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\Temp" "

notebooks_zipados = ['"'+str(caminho_raiz / arquivo).replace("\\","/")+'"'
                       for arquivo in todos_arquivos 
                          if fnmatch.fnmatch(arquivo, zipado)]

notebooks_temp = [str(temp / turma).replace("\\","/")
                    for turma in nomes_turmas]

nb_temp = [str(temp / turma) for turma in nomes_turmas]

# caminho_cmd_7zip_exe = '"C:/Program Files/7-Zip/7z.exe"'
caminho_cmd_7zip_exe = "unzip"

"""
Combina os nomes dos arquivos zipados de cada turma com os caminhos Temp da
turma 
"""
# unzip_cmds = ["cmd /C "+'"'+caminho_cmd_7zip_exe+" x -spf "+ \
#               notebooks_zipados[i]+" -o"+ \
#               notebooks_temp[j]+'"' for i in range(len(notebooks_zipados)) \
#               for j in range(len(notebooks_temp)) if i == j]

unzip_cmds = [caminho_cmd_7zip_exe+" "+ \
              notebooks_zipados[i]+" -d "+ \
              notebooks_temp[i] for i in range(len(notebooks_zipados))]

""" Executa os comandos de descompactação dos notebooks, se os diretórios
    com os notebooks não existem."""

if os.listdir(nb_temp[0]) == []:
    print('*** unzip ***')
    print(executa_comandos(unzip_cmds))

"""
Coleta os nomes dos alunos em dirs_turma a partir dos diretórios onde se
encontram os notebooks dos alunos."""

dirs_turmas = []
temp_turmas = [notebooks_temp[i].replace('"', "") for i in range(len(notebooks_temp))]
for turma in temp_turmas:
    for _, dirs, _ in os.walk(turma, topdown = True):
        if dirs != []:
            dirs_turmas += [dirs]
            
#The [^<char>] is a character class, it matches everything but <char>. 
novos_nomes = [[re.search('\w[^_]+',nome).group()[0:] for nome in turma]
                  for turma in dirs_turmas]
""" Troca os nomes dos notebooks dos alunos em notes_turmas pelos nomes
    capturados dos diretórios onde os notebooks foram descompactados em
    novos_nomes. Passa cada um dos notebooks com os novos nomes de
    ./Temp/Turmas em temp_turmas para ./Alunos/TX/Notebooks em turmas.
    O arquivo original é apagado na origem. Coleta os nomes dos notebooks
    para comvertê-los em scripts. Verifica se dirs_turmas, lista dos nomes 
    dos diretórios com os notebooks, não é vazia. Registra os erros em 
    registro.txt"""

"""reg_turmas contém os manipuladores de arquivos de registros_TX.txt que
   ficam no caminho raiz"""

reg_turmas = []
# for i in range(len(nomes_turmas)):
#     if not os.path.exists(str(caminho_raiz)+ \
#                             '\\registro_'+str(nomes_turmas[i])+'.txt'):
#         reg_turmas.append(open(str(caminho_raiz)+ \
#                              '\\registro_'+str(nomes_turmas[i])+'.txt','a'))

for i in range(len(nomes_turmas)):
    if not os.path.exists(str(caminho_raiz)+ \
                            '/registro_'+str(nomes_turmas[i])+'.txt'):
        reg_turmas.append(open(str(caminho_raiz)+ \
                             '/registro_'+str(nomes_turmas[i])+'.txt','a'))

for i in range(len(reg_turmas)):
    reg_turmas[i].write("*** Erros de conversão ***\n")

if dirs_turmas != []:
    erro = False
    nomes_notebooks_turmas = []
    for i in range(len(temp_turmas)):
        notes_turma = []
        for j in range(len(dirs_turmas[i])):
            pasta = dirs_turmas[i][j]
            #Como só há um notebook dentro de cada diretório, pega só o nome do arquivo
            print("temp_turmas: " + str("|"+temp_turmas[i] +"/"+ pasta+"|"))
            [arq] = os.listdir(temp_turmas[i] +"/"+ pasta)
            """Testa se arq é .ipynb; se não for, não renomeia"""
            fim_arq = str(arq).split('.')
            if len(fim_arq) == 1:
                reg_turmas[i].write("Arquivo não tem tipo especificado: "+ \
                                     str(arq)+"\n")
                erro = True
            elif len(fim_arq) > 2: #separaram o nome com ponto...
                reg_turmas[i].write("Advertência - Nome separado com ponto: "+ \
                                     str(arq)+"\n")
                #Não é erro é facepalm warning
            elif fim_arq[1] != 'ipynb': #arquivo não é notebook
                reg_turmas[i].write("Não é notebook: "+str(arq)+"\n")
                erro = True
            if not erro:#converte o nome do notebook    
                nome_novo = str(novos_nomes[i][j])+'.ipynb'
                os.rename(os.path.join(temp_turmas[i] / pasta, arq),
                          os.path.join(turmas[i] / 'Notebooks', nome_novo))
                notes_turma += [nome_novo]
            erro = False
        nomes_notebooks_turmas += [notes_turma]
        reg_turmas[i].close() 
        
""" Elimina Temp/TX/Dir_NB vazios, já que os arquivos que são notebooks
    foram transladados para Alunos/TX/Notebooks para serem convertidos.
    Mantém só os diretórios que não estão vazios, porque os arquivos submetidos
    contém erros"""

for turma in temp_turmas:
    for folder in os.listdir(turma):
        arqs = [f for f in os.listdir(turma / folder) if not f.startswith('.')]
        if  arqs == []:
            shutil.rmtree(turma / folder,ignore_errors=True)

# """
# Converte os notebooks de todas as turmas para script Python nas pastas Scripts 
# """
# """
# Comando de conversão testado e que funciona na linha de comando do Windows 10:
# """
# #\Users\Jose\Anaconda3\Scripts\jupyter-nbconvert.exe --to script --output-dir="\Users\Jose\Dropbox\DCC\Cursos\Python\Programas\Corretor automatico de exercicios Python\Alunos\TA\Scripts" *

# scripts_turmas = ['"'+str(turma / "Scripts").replace("\\","/")+'"'
#                      for turma in turmas]
# notebooks_turmas = ['"'+str(turma / "Notebooks/*").replace("\\","/")+'"'
#                      for turma in turmas]
# cmd_nb_convert = '"C:/Users/Jose/Anaconda3/Scripts/jupyter-nbconvert.exe"'

# convert_cmds = ["cmd /C"+'"'+cmd_nb_convert+" --to script --output-dir="+ scripts_turmas[j]+' '+str(notebooks_turmas[i])+'"' for i in range(len(notebooks_turmas)) \
#               for j in range(len(scripts_turmas)) if i == j]

# #print(f'convert_cmds: {convert_cmds}')

# # print('*** conversão de notebooks ***')
# # print(executa_comandos(convert_cmds))


# #Um único loop para fazer o seguinte abaixo:
# #1- Troca os nomes dos notebooks dos alunos pelos nomes tirados dos diretórios
# #   que os contém;
# #2- converte os notebooks em scripts Python, salvando-os em Scripts de cada
# #   turma
# #3- Roda o Jplag em Scripts, salvando os resultados em Plágio
# #4- Verifica quais resultados do JPlag estão acima de 50% por cento, escrevendo
# #   em um arquivo resultados-jplag-acima-de-50-por-cento.txt
# #5- Roda o corretor automático nos scripts, salvando o resultado em outro
# #   arquivo resultados-correção.txt

