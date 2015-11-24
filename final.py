#!/usr/bin/python
          # -*- coding: utf-8 -*-

# RECONHECEDOR DE EXPRESSÕES MATEMÁTICAS
# INSTITUIÇÃO: Universidade do Estado de Santa Catarina (UDESC)
# EQUIPE: Guilherme Kricheldorf
#         William Pereira
# DISCIPLINA: Linguagens Formais e Autômatos (LFA)
# DESCRIÇÃO: Trabalho final da disciplina de LFA.
#            Reconhecedor de expressões matemáticas utilizando o 
#            algorítimo de reconhecimento Cocke-Younger-Kasami (CYK)


# UTILIZAÇÃO DO ply.lex (FERRAMENTA DE ANÁLISE LÉXICA)
import lex

tokens = (
    'num',
    )
    
# Tokens
t_num              = r'\d+'

# Caracteres literais para reconhecimento
literals = ['+','-','/','*','(',')']

# Caracteres ignorados pelo lexer
t_ignore = " \t"

# Tratamento caso a entrada possua um caractere ilegal
erro = 0
def t_error(t):
    print("Caractere ilegal ignorado: '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construçao do lexer
lexer = lex.lex()

# Leitura da expressão
entrada = raw_input('Expressao: ')

# Entrada da expressão para o lexer
lexer.input(entrada)

# Criação de uma lista com os tipos dos tokens gerados
expressao = []
while True:
    tok = lexer.token()
    if not tok:
        break           # Entrada acabou
    expressao.append(tok.type)

# CYK

# Gramatica na Forma Normal de Chomsky
'''
G = (V,T,P,S) onde

V = {E, EOP, P, FP, OP, AP}

T = {num, +, -, *, /, (, )}

P = {
E -> EOP E | P FP | num ,    
OP -> + | - | * | / ,
EOP -> E OP ,
P -> AP E ,
AP -> ( ,
FP -> ) 
}

S = {E}
'''

# Lista com as produções da gramática
# Cada tupla representa uma produção 
# Exemplo produções tipo A -> B C: ('A', 'B', 'C')
# Exemplo produções tipo A -> a: ('A', 'a')
producoes = [('E', 'EOP', 'E'), ('E', 'P', 'FP'), ('E', 'num'), 
             ('OP', '+'), ('OP', '-'), ('OP', '*'), ('OP', '/'), 
             ('EOP', 'E', 'OP'), 
             ('P', 'AP', 'E'), 
             ('AP', '('), 
             ('FP', ')')
             ]

def printTable(tabela):
    for s in range(2):
        for r in range(1,n+1):
            print '{:10}'.format(tabela[r][s]),
        print "\n"
    
    for s in range(2,n+1):
        for r in range(1,(n-s+1)+1):
            if j <= 1:
                print '{:10}'.format(tabela[r][s]),
            else:
                print '{:10}'.format("{"+", ".join(str(e) for e in tabela[r][s])+"}"),
        print "\n"

n = len(expressao)
if n == 0:
    print ("Nenhum caractere pertencente ao conjunto de terminais encontrado na entrada")
else:

    # Criação da tabela
    tabela = []
    for i in range(n+1):
        linha = []
        for j in range(n+1):
            linha.append([])
        tabela.append(linha)

    # Preenche a linha 0 da tabela com a expressão
    for r in range(1,n+1):
        tabela[r][0] = expressao[r-1]

    # Implementação do Algorítimo CYK
    # Variáveis que geram diretamente terminais (A->a)
    for r in range(1,n+1):
        for producao in producoes:
            if len(producao) == 2 and expressao[r-1] == producao[1]:
                tabela[r][1] = producao[0]
    
    # Produção que gera duas variáveis (A->BC)
    for s in range(2,n+1):
        for r in range(1,(n-s+1)+1):
            tabela[r][s] = set([])
            for k in range(1,s):
                for producao in producoes:
                    if len(producao) == 3:
                        if producao[1] in tabela[r][k]:
                            if producao[2] in tabela[r+k][s-k]:
                                tabela[r][s].add(producao[0])
    
    printTable(tabela)
    
    # Condição da aceitação da entrada
    # Verifica se o símbolo inicial pertence ao vétice tabela[1][n]
    # (raiz da arvore de derivação de toda palavra)
    # Se pertencer, a entrada é aceita
    if "E" in tabela[1][n]: 
        print ("Aceita!")
    else:
        print ("Rejeita!")

raw_input("")
