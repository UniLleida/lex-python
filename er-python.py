import os
import re

class ExpReg(object):

    def ex1(self, fname):
        f = open(fname)
        line = f.readline()
        while (line != ""):
            if not(line == "" or line[:-1] == ""):
                if line[-1] == "\n":
                    self.ex1_check_line(line[:-1])
                else:
                    self.ex1_check_line(line)
            line = f.readline()
        f.close()
        pass

    def ex1_check_line(self, line):
        # Nom: nom de l’usuari
        # email: nom@domini
        # Telf: tel`efon
        # Haureu de verificar que tots tres camps son correctes. El nom d’usuari ser ´ a un conjunt `
        # de tres paraules com a maxim que comencen per maj ` uscula, l’adrec¸a de correu haur ´ a`
        # de contenir una arrova i un domini i nom correctes, i el telefon haur ` a de contenir 9 `
        # d´ıgits o el s´ımbol + seguit de 11 d´ıgits.
        pattern1 = re.compile("Nom:(( )+[A-Z][a-z]+){1,3}") # de 1 a 3 camps de lletres separats amb espais començant amb majuscules
        pattern2 = re.compile("email:( )+([A-Za-z0-9._-]*@[a-zA-z]*(.)[a-z]{3})") # format de email
        pattern3 = re.compile("Telf:( )+(\+[0-9]{2})?[0-9]{9}") # 9 digits precedits opcionalment per un simbol '+' seguit de dos digits.
        case1 = pattern1.match(line)
        case2 = pattern2.match(line)
        case3 = pattern3.match(line)
        if case1 != None and case1.group()==line:
            print("OK (name field):    "+line)
        else:
            case1 = None
        if case2 != None and case2.group()==line:
            print("OK (email field):   "+line)
        else:
            case2 = None
        if case3 != None and case3.group()==line:
            print("OK (phone field):   "+line)
        else:
            case3 = None
        if case1 == None and case2 == None and case3 == None:
            print("!! (invalid field): "+line)
        pass



    def ex2(self, fname):
        f = open(fname)
        line = f.readline()
        while (line != ""):
            if not(line == "" or line[:-1] == ""):
                if line[-1] == "\n":
                    self.ex2_check_line(line[:-1])
                else:
                    self.ex2_check_line(line)
            line = f.readline()
        f.close()
        pass


    def ex2_check_line(self, line):
        # Creeu una mini calculadora que doni el resultat d’operacions de la forma:
        # Calc <n´um1> <operaci´o> <n´um2>;
        # on <num1> i <n´um2> poden ser enters o nombre de punt flotant i <operaci´o>
        # es un dels seg ´ uents car ¨ acters +, -, *, /. Permeteu que hi pugui haver espais entre els `
        # elements de l’operacio, i que hi pugui haver m ´ es d’una operaci ´ o per l ´ ´ınia. El format
        # de sortida es: ´
        # La <nom-operaci´o> de <n´um1> i <n´um2> ´es <n´um3>.
        # On <nom-operaci´o> es una de les seg ´ uents paraules: suma, resta, multiplicaci ¨ o,´
        # divisio; i ´ <n´um3> es el resultat de l’operaci ´ o. ´
        # El resultat haura de ser en punt flotant nom ` es si algun dels par ´ ametres ` es en p
        pattern1 = re.compile("(Calc)( )+(-)?([0-9]+)( )+([-+*/])( )+(-)?([0-9]+)") # 2 enters
        pattern2 = re.compile("(Calc)( )+(-)?([0-9]+\.[0-9]+)( )+([-+*/])( )+(-)?([0-9]+\.[0-9]+)") # 2 flotants
        pattern3 = re.compile("(Calc)( )+(-)?([0-9]+)( )+([-+*/])( )+(-)?([0-9]+\.[0-9]+)") # 1 enter i 1 flotant
        pattern4 = re.compile("(Calc)( )+(-)?([0-9]+\.[0-9]+)( )+([-+*/])( )+(-)?([0-9]+)") # 1 flotant i un enter
        case1 = pattern1.match(line)
        case2 = pattern2.match(line)
        case3 = pattern3.match(line)
        case4 = pattern4.match(line)
        if case1 != None and case1.group()==line:
            self.int_case(case1)
        else:
            case1 = None
        if case2 != None and case2.group()==line:
            self.float_case(case2)
        else:
            case2 = None
        if case3 != None and case3.group()==line:
            self.float_case(case3)
            pass
        else:
            case3 = None
        if case4 != None and case4.group()==line:
            self.float_case(case4)
            pass
        else:
            case4 = None
        if case1 == None and case2 == None and case3 == None and case4 == None:
            print("!! (invalid operation): "+line)
        pass

    def print_int_operation(self, operator, operand1, operand2):
        if operator == "+":
            print("la suma de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1+operand2))
        elif operator == "-":
            print("la resta de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1-operand2))
        elif operator == "*":
            print("la multiplicacio de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1*operand2))
        else:
            print("la divisio de "+str(operand1)+" i "+str(operand2)+" es "+str(int(operand1/operand2)))

    def print_float_operation(self, operator, operand1, operand2):
        if operator == "+":
            print("la suma de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1+operand2))
        elif operator == "-":
            print("la resta de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1-operand2))
        elif operator == "*":
            print("la multiplicacio de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1*operand2))
        else:
            print("la divisio de "+str(operand1)+" i "+str(operand2)+" es "+str(operand1/operand2))


    def int_case(self, case):
        minus1 = case.group(3) # 1er operand negatiu (opcional)
        minus2 = case.group(8) # 2on operand negatiu (opcional)
        if minus1 == "-":
            operand1 = -int(case.group(4))
        else:
            operand1 = int(case.group(4))
        if minus2 == "-":
            operand2 = -int(case.group(9))
        else:
            operand2 = int(case.group(9))
        operator = case.group(6)
        self.print_int_operation(operator,operand1,operand2)

    def float_case(self, case):
        minus1 = case.group(3) # 1er operand negatiu (opcional)
        minus2 = case.group(8) # 2on operand negatiu (opcional)
        if minus1 == "-":
            operand1 = -float(case.group(4))
        else:
            operand1 = float(case.group(4))
        if minus2 == "-":
            operand2 = -float(case.group(9))
        else:
            operand2 = float(case.group(9))
        operator = case.group(6)
        self.print_int_operation(operator,operand1,operand2)


if __name__ == '__main__':
    print("ex1")
    ExpReg().ex1("demo1.dat")
    print("\nex2")
    ExpReg().ex2("demo2.dat")