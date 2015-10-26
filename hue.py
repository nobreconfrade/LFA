#EXEMPLOS 
#150+1
#1*9
#(814/9)
#000010-78979 * 494
#1021+(544-125)

'''
E -> EOP E
    | (E )
    | c
    
OP -> +
    | -
    | *
    | /
    
EOP -> E OP
(E -> ( E 
'''

'''
E
EOP E
E OP E
c OP E
c + E
c + (E )
c + ( E )
c + ( EOP E )
c + ( E OP E )
c + ( c OP E )
c + ( c - E )
c + ( c - c )
'''
