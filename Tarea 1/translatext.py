import re
def expresiones(linea):
        Exp_Expresion_matematica = r"(SUM\s+|SUBTRACT\s+|MULTIPLY\s+|DIVIDE\s+)*(\d+\s*|(?!PROCEDURE|INITIALIZE|SET|SUM|SUBSTRACT|MULTIPLY|DIVIDE|TO|BY|OR|AND|GREATER|SMALLER|THAN|NO|EQUAL|DIFFERENT|THEN|IF|ELSE|END|WHILE|READ|PRINT)[A-Za-z]\w*\s*)*(TO\s+|BY\s+)*"
        Exp_Expresion_booleana = r"((IF\s+)((NOT\s+)?((GREATER\s+|SMALLER\s+)(\d+\s+|[A-Za-z]\w*\s+)THAN\s+(\d+\s+|[A-Za-z]\w*\s+)|(\d+\s+)|([A-Za-z]\w*\s+)|TRUE\s+|FALSE\s+)(AND\s+|OR\s+|DIFFERENT\s+TO\s+|EQUAL\s+TO\s+)?)+(THEN\s*))"
        Exp_Expresion_loop = r"(WHILE\s+)((NOT\s+)?((GREATER\s+|SMALLER\s+)(\d+\s+|[A-Za-z]\w*\s+)THAN\s+(\d+\s+|[A-Za-z]\w*\s+)|(\d+\s+)|([A-Za-z]\w*\s+)|TRUE\s+|FALSE\s+)(AND\s+|OR\s+|DIFFERENT\s+TO\s+|EQUAL\s+TO\s+)?)+"
        if re.fullmatch(Exp_Expresion_matematica,linea):
                return True
        elif re.fullmatch(Exp_Expresion_booleana,linea):
                return True
        elif re.fullmatch(Exp_Expresion_loop,linea):
                return True
        else:
                return False
"""La función expresiones verifica, a través de expresiones regulares, cuáles líneas presentan error y cuáles no, retornando True o False dependiendo del caso."""




def validar(linea1,techo,piso,code):
        if linea1 < piso and linea1 >= techo:
                if re.match(Exp_While,code[linea1]):
                        p = expresiones(code[linea1])
                        if p == True:
                                #trad = traducir(code[linea1])
                                lineasValidas.append(code[linea1])
                                # lineasValidasTraducidas.append(trad)
                elif re.match(Exp_If,code[linea1]):
                        p = expresiones(code[linea1])
                        if p == True:
                                #trad = traducir(code[linea1])
                                lineasValidas.append(code[linea1])
                                #lineasValidasTraducidas.append(trad)
                elif re.match(Exp_Pro,code[linea1]):
                        #trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                        #lineasValidasTraducidas.append(trad)
                elif re.match(Exp_End_Pro,code[linea1]):
                        #trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                        #lineasValidasTraducidas.append(trad)
                        return True
                elif re.match(Exp_Set,code[linea1]):
                        p = re.match(Exp_Set,code[linea1])
                        if expresiones(p.group(4)) == True:
                                #trad = traducir(code[linea1])
                                lineasValidas.append(code[linea1])
                                #lineasValidasTraducidas.append(trad)
                elif re.match(Exp_Ini,code[linea1]):
                       # trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                        #lineasValidasTraducidas.append(trad)
                elif re.match(Exp_Read_Print,code[linea1]):
                       # trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                        #lineasValidasTraducidas.append(trad)
                elif re.match(Exp_Else,code[linea1]):
                       # trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                       # lineasValidasTraducidas.append(trad)
                elif re.match(Exp_End_If,code[linea1]):
                       # trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                      #  lineasValidasTraducidas.append(trad)
                        return True
                elif re.match(Exp_End_While,code[linea1]):
                        #trad = traducir(code[linea1])
                        lineasValidas.append(code[linea1])
                       # lineasValidasTraducidas.append(trad)
                        return True
               # elif re.match(r"(((SUM\s+|SUBTRACT\s+|MULTIPLY\s+|DIVIDE\s+)*(\d*|[A-Za-z]\w*)\s+(TO\s+|BY\s+))*(\d*|[A-Za-z]\w*))",code[linea1]):
                        #trad = traducir(code[linea1])
                       # lineasValidas.append(code[linea1])
                        #lineasValidasTraducidas.append(trad)
        validar(linea1+1,techo,piso,code)
"""La función validar, recibe la línea con su contenido (code) y el programa en el cual está trabajando (el rango de Procedure-EndProcedure en el que está contenida la línea. Verifica las líneas que están correctas mediante expresiones regulares y las agrega a una lista para posteriormente ser traducidas"""




def traducir(linea2):
        if re.search("IF",linea2):
                trad = re.sub("IF","SI",linea2)
                trad = re.sub("THEN","ENTONCES",linea2)
        if re.search("IF",linea2):
                trad = re.sub("IF","SI",linea2)
        if re.search("ELSE",linea2):
                trad = re.sub("ELSE","SINO",linea2)
        if re.search("SET",linea2):
                trad = re.sub("SET","FIJA",linea2)
                trad = re.sub("TO","EN",linea2)
        if re.search("SUM",linea2):
                trad = re.sub("SUM","SUMA",linea2)
                trad = re.sub("TO","A",linea2)
        if re.search("SUBTRACT",linea2):
                trad = re.sub("SUBTRACT","RESTA",linea2)
                trad = re.sub("TO","A",linea2)
        if re.search("DIVIDE",linea2):
                trad = re.sub("DIVIDE","DIVIDE",linea2)
                trad = re.sub("BY","POR",linea2)
        if re.search("MULTIPLY",linea2):
                trad = re.sub("MULTIPLY","MULTIPLICA",linea2)
                trad = re.sub("BY","POR",linea2)
        if re.search("WHILE",linea2):
                trad = re.sub("WHILE","MIENTRAS",linea2)
        if re.search("WHILE",linea2):
                trad = re.sub("WHILE","MIENTRAS",linea2)
        if re.search("READ",linea2):
                trad = re.sub("READ","LEER",linea2)
        if re.search("PRINT",linea2):
                trad = re.sub("PRINT","IMPRIME",linea2)
        if re.search("AND",linea2):
                trad = re.sub("AND","Y",linea2)
        if re.search("OR",linea2):
                trad = re.sub("OR","O",linea2)
        if re.search("EQUAL",linea2):
                trad = re.sub("EQUAL","IGUAL",linea2)
                trad = re.sub("TO","A",linea2)
        if re.search("DIFFERENT",linea2):
                trad = re.sub("DIFFERENT","DIFERENTE",linea2)
                trad = re.sub("TO", "A",linea2)
        if re.search("PROCEDURE",linea2):
                trad = re.sub("PROCEDURE","PROCEDIMIENTO",linea2)
        if re.search("GREATER",linea2):
                trad = re.sub("GREATER","MAYOR",linea2)
                trad = re.sub("THAN","QUE",linea2)
        if re.search("SMALLER",linea2):
                trad = re.sub("SMALLER","MENOR",linea2)
                trad = re.sub("THAN","QUE",linea2)
        if re.search("INITIALIZE",linea2):
                trad = re.sub("INITIALIZE","INICIALIZA",linea2)
        if re.search("END",linea2):
                trad = re.sub("END", "FIN",linea2)
        return trad
"""La función traducir recibe una linea y verifica si en dicha linea calza cierto patrón y mediante este reemplazar por su respectiva traducción"""




nombre = input("Ingrese nombre del texto ")+".txt"
Procedure = []
End_Procedure = []
If = []
Else = []
End_If = []
While =[]
End_While = []
numlin = 0
Exp_Pro = r"(PROCEDURE\s+)([0-9A-Za-z]+\s*)"
Exp_End_Pro = r"(END\s+PROCEDURE\s*)"
Exp_Ini = r"(INITIALIZE\s+)([A-Za-z]\w+\s*)"
Exp_Set = r"(SET\s+)([A-Za-z]\w*\s*)(TO\s+)(.+)"
Exp_If = re.compile("(\s*IF\s+)(.+)(THEN\s*)")
Exp_Else = re.compile("(\s*ELSE\s*)")
Exp_End_If = re.compile("(\s*END\s+IF\s*)")
Exp_While = re.compile("(\s*WHILE\s*)(.+)")
Exp_End_While = re.compile("(\s*END\s+WHILE\s*)")
Exp_Read_Print = r"(READ\s+|PRINT\s+)(.+\s*)"

with open(nombre) as codigo:
        code = codigo.read().splitlines()
        for linea in code:
                if re.match(Exp_Pro,linea):
                        Procedure.append(numlin)
                elif re.match(Exp_End_Pro,linea):
                        End_Procedure.append(numlin)
                elif re.match(Exp_If,linea):
                        If.append(numlin)
                elif re.match(Exp_Else,linea):
                        Else.append(numlin)
                elif re.match(Exp_End_If,linea):
                        End_If.append(numlin)
                elif re.match(Exp_While,linea):
                        While.append(numlin)
                elif re.match(Exp_End_While,linea):
                        End_While.append(numlin)
                numlin += 1
entrega = open("pseudocodigo.txt",'w')
if len(Procedure) == 0 and len(End_Procedure) == 0:
        entrega.write("NO HAY PROGRAMA")
else:
        Cor_Pro = Cor_End_Pro = numlin = Cor_If = Cor_Else = Cor_EndIf = 0
        codigos_validos = []
        codigosIf_validos = []
        for k in End_Procedure:
                for i in Procedure:
                        if i < k:
                                if Cor_Pro != i:
                                        Cor_Pro = i
                                Cor_End_Pro = k
                valid = (Cor_Pro,Cor_End_Pro)
                codigos_validos.append(valid)
        
        codigo_traducido= ''
        lineasValidas = list()
        lineasValidasTraducidas = list()
        rangoIF=min(len(If),len(Else),len(End_If))
        for l,m in codigos_validos:
                for j in range(l,m+1):
                        if  j>= l and j<= m:
                                validar(j,l,m+1,code)
        for index in range(len(code)):
                if code[index] in lineasValidas:
                        codigo_traducido += code[index]+"\n"
                else:
                        codigo_traducido += code[index]+" #Error\n"

        print(codigo_traducido)