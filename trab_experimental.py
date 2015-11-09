e = raw_input("Digite sua expressao:")
import lex
tokens = ('num','var',)
t_num = r"\d+"
t_var = r"[A-Z]+"
literals = ['+','-','*','/','(',')']
t_ignore = " \t"
def t_error(t):
    print "Erro '%s'" % t.value[0]
    t.lexer.skip(1)
   
lexer = lex.lex()
lexer.input(e)

exp = []

while True:
    tok = lexer.token()
    if not tok:
        break
    exp.append(tok.type)
    #print to

#print exp
tabela = []
n = len(exp)
for i in range(n+1):
    linha = []
    for j in range(n+1):
        linha.append([])
    tabela.append(linha)

# Imprime a tabela    
for i in range(n+1):
    print(tabela[i])
print("\n")
        
for r in range(1,n+1):
    tabela[r][0] = exp[r-1]
    
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

producoes = [('E', 'EOP', 'E'), ('E', 'P', 'FP'), ('E', 'num'), 
             ('OP', '+'), ('OP', '-'), ('OP', '*'), ('OP', '/'), 
             ('EOP', 'E', 'OP'), 
             ('P', 'AP', 'E'), 
             ('AP', '('), 
             ('FP', ')')
             ]
for r in range(1,n+1):
    for producao in producoes:
        if len(producao) == 2 and exp[r-1] == producao[1]:
            tabela[r][1] = producao[0]
            
            
    
