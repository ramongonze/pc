# Input: All the files sent to one exercise", from class TB1
# Output: Remove all directories which are note sudents from id [29,57]

import sys
import os
import shutil

students = {"Luan Silva Tomaz",
"Lucas Marx Teixeira de Freitas",
"Lucas Millard Andrade Silva",
"Lucas Omar Fonseca Ferreira",
"Luiz Fernando Neves Guimarães",
"Luiza Guimaraes Raso",
"Marcos Vinicius Reis Guimaraes Leite",
"Mariana Nascimento de Souza",
"Matheus Pangella de Lana",
"Naiara Aparecida Martins Garcia",
"Otavio Gabriel Campos",
"Paulo Henrique Farah Leocadio e Silva",
"Paulo Igor Rodrigues",
"Pedro Henrique Bernardes Solha",
"Pedro Henrique Figueiredo Araujo",
"Pedro Streit Ferreira",
"Rafael Expedito de Almeida Rincon",
"Rafael Goulart Rosse",
"Rafaela Maria Farnezi Fagundes",
"Raissa Nepomuceno Freitas",
"Roberto Henrique Bastos Assis",
"Thais Ester Rodrigues Costa",
"Tiago Martires Gregorio",
"Victor Hugo Augusto Cezario Morais de Oliveira",
"Victor Hugo da Costa Soares de Oliveira",
"Vinicius Gabriel Mello Silva",
"Vitor Barreto Ribeiro",
"Vitor Maciel Rodrigues",
"Yasmini Kelly Gomes dos Santos"}

exercicio = sys.argv[1]
os.chdir("/home/ramon/Desktop/pc/turma_tb1/exercicio" + exercicio)

for directory in os.listdir():
	student = directory.split('_')[0]

	if student not in students:
		shutil.rmtree(directory) # Remove the directory and everything inside it
	else:
		os.rename(directory, student)

os.chdir("/home/ramon/Desktop/pc")