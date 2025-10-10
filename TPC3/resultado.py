
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<S>select)|(?P<LIMI>LIMIT \d{4})|(?P<W>where)|(?P<START>\{)|(?P<END>\})|(?P<VAR>\?[A-Za-z_]\w*)|(?P<ID>\w+:\w+(?:\s+"[^"]+")?(?:@\w+)?)|(?P<terminador>\.)|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['S']:
            t = ("S", dic['S'], linha, m.span())

        elif dic['LIMI']:
            t = ("LIMI", dic['LIMI'], linha, m.span())
    
        elif dic['W']:
            t = ("W", dic['W'], linha, m.span())
    
        elif dic['START']:
            t = ("START", dic['START'], linha, m.span())
    
        elif dic['END']:
            t = ("END", dic['END'], linha, m.span())
    
        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['ID']:
            t = ("ID", dic['ID'], linha, m.span())
    
        elif dic['terminador']:
            t = ("terminador", dic['terminador'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    

