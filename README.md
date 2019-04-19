# Lista 3
Algoritmos de Ordenação O(n*log(n))  

## Alunos  
| Nome                  | Matrícula           | Github              |  
|--|-----------------------|---------------------|  
| Adailson Pinho dos Santos | 13/0140724 | [adailson2](https://github.com/adailson2) |  
| Eliseu Egewarth | 12/0029693 | [eliseuegewarth](https://github.com/eliseuegewarth) |  

## Algoritmos implementados
- [x] recursive_merge_sort  
	
	Faz o uso da recursividade para executar a ordenação dos elementos.

- [ ] iterative_merge_sort  
	
	Faz o uso da iteratividade para executar a ordenação dos elementos.
	
- [x] parallel_merge_sort  

	Faz o uso da estratégia de mergeSort recursivo utilizando o paralelismo computacional em máquinas com mais de um núcleo de processamento.
	
- [ ] quick_sort

	Faz o uso da recursividade para executar a ordenação dos elementos.
	Por conta da recursividade e da implementação original levar o último elemento como pivot, o pior caso O(n²) pode atingir o limit de recursões da máquina.
	Para casos de vetores que possam estar totalmente ordenados, a situação citada foi observada para 50.000, que para o volume de dados das aplicações atuais um número pequeno.
	
- [x] iterative_bucket_sort

	Realiza a iteração do método de ordenação dos elementos em baldes. Após baldes definidos, é feito o uso do método Selection Sort para cada balde.

## Estrutura do repositório
- merge_sort/  
	Implementações do algoritmo merge_sort
- bucket_sort/  
	Foi utilizado como refência o link (https://www.geeksforgeeks.org/bucket-sort-2/) e aprimorado para a utilização de valores inteiros e com vários dígitos.
- performance_report/  
	Resultado dos testes de performance dos algoritmos (arquivos CSV)

## Dependências do projeto
O projeto usa Python 3 e as bibliotecas utilizadas estão listadas no arquivo `requirements.txt`.  
A biblioteca `matplotlib` utilizada para plotar os resultados dos testes de performance depende do pacote `python3-tk` para linux.

## Instruções de uso

Execute o comando abaixo para baixar as dependências necessárias: 
```
$ pip3 install -r requirements.txt
```
Feito isso, rode o comando abaixo para mostrar no terminal quais dados de entradas são necessários para o funcionamento do algoritmo:
```
$ python3 sort.py
```
## Análise de performance dos algoritmos
Junto ao código dos algoritmos de ordenação, também estão dispostos neste repositório alguns códigos auxiliares como os algoritmos relacionados a testes de performance.  
A escrita desses testes segue um padrão que pode ser observado nos arquivos de resultados.  
Os resultados das análises estão armazenados no diretório `performance_report`.  
Para analisar os dados graficamente, basta executar o comando abaixo:
```
$ python3 plot_benchmark.py $(ls performance_report/*.csv)
```
## Outros algoritmos neste repositório
- benchmark.py
	Contém as funções que auxiliam na escrita de resultados de testes de algoritmos
- gera_vector.py
	Contém 2 funções para geração de vetores de inteiros randômicos
	- gera_vector  
		Retorna uma lista de inteiros gerada randomicamente.
	- gera_vector_rapido  
		Retorna uma lista de inteiros gerada randomicamente.
		Otimizado para utilizar paralelismo computacional.
- plot_benchmark.py
	Carrega dados de arquivos CSV e plota os gráficos de desempenho dos algoritmos.
