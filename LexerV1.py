#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Analizador de Lexico Version 1.0 

#Library and import

from os import error
import re as regex
from typing import DefaultDict

#HTML SAMPLE START

html_samp_start = '''
<html>
    <title> LexerScheme </title>
        <head>

            <link href = "styles/style.css" rel = "stylesheet" type = "text/css">

        </head>
            <body>
                <h2> LexerScheme V1.0 </h2>
                <h4>Informacion de color y de estilos</h4>
                <br>
                <span class = 'box_rounded_1'> Identificadores &nbsp; </span> <span class = 'box_rounded_2'> Palabras Reservadas &nbsp;</span> <span class = 'box_rounded_3'> Constantes Decimales &nbsp; </span> <span class = 'box_rounded_4'> Constantes Enteras Punto Flotante &nbsp; </span> <span class = 'box_rounded_5'> Simbolos Especiales &nbsp; </span> <span class = 'box_rounded_6'> Comentarios &nbsp; </span> <span class = 'box_rounded_7'> Errores &nbsp; </span> <br><br>

'''

html_samp_end = '''

        </body>

</html>

'''



#Regular Expresions

identifiers = regex.compile(r"[^;,'#\(\)\{\}]+")
constant = regex.compile(r"^\-?[0-9]+\d*")
constant_float = regex.compile(r"^\-?[0-9]+\d*(\.\d*)?[Ee]?(\-?\d*)")
special_simbols = regex.compile(r"(<>)|(<=)|(>=)|[\+\-\*/<=>\(\)]")
commentary = regex.compile(r"^\;.+")

#Current character to read
character_number = 0

#Current sequence of characters
sequence = ""

#Regresion variable
regresion = False

#Check
check = False

#Comment Line
comment = False

#End of file variable
end_of_file = False

#Tokens

tokens = {        "define"   : '<span class = "reserved"> define </span>', 
                  "lambda"   : '<span class = "reserved"> lambda </span>', 
                  "if"       : '<span class = "reserved"> if </span>',
                  "cond"     : '<span class = "reserved"> cond </span>',
                  "else"     : '<span class = "reserved"> else </span>',
                  "true"     : '<span class = "reserved"> true </span>',
                  "false"    : '<span class = "reserved"> false </span>',
                  "nil"      : '<span class = "reserved"> nil </span>',
                  "car"      : '<span class = "reserved"> car </span>',
                  "cdr"      : '<span class = "reserved"> cdr </span>',
                  "cons"     : '<span class = "reserved"> cons </span>',
                  "list"     : '<span class = "reserved"> list </span>',
                  "apply"    : '<span class = "reserved"> apply </span>',
                  "map"      : '<span class = "reserved"> map </span>',
                  "let"      : '<span class = "reserved"> let </span>',
                  "begin"    : '<span class = "reserved"> begin </span>',
                  "null?"    : '<span class = "reserved"> null? </span>',
                  "eq?"      : '<span class = "reserved"> eq? </span>',
                  "set!"     : '<span class = "reserved"> set! </span>',
                  20         : "Secuencia de caracteres invalidos",
                  21         : "Identificador",
                  22         : "Constante decimal",
                  23         : "Constante entera punto flotante",
                  24         : "Simbolo Especial",
                  25         : "Comentario"}

#Default value for keys that arent in dictionary
tokens = DefaultDict(lambda: "Token no encontrado", tokens)

#Function to check if a string is a number
def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

#Function to receive current character, total of characters and the list of characters
def get_token(number_of_characters,list_of_characters):

    #Current number of character 
    global character_number
    #Current Sequence of characters
    global sequence
    #Checker
    global check
    #Regresion Variable
    global regresion
    #Comment verificator variable
    global comment
    #Variable End of File
    global end_of_file
    #Sequence of the HTML output file
    global html_sequence

    #Check if the character counter has surpassed the character list lenght
    if character_number == number_of_characters:
        check = "EOF"
        end_of_file = True
        return True

    char = list_of_characters[character_number]

    #Delimiters
    
    if char == " ":

        if comment == True:
            sequence = sequence + char
            character_number = character_number + 1
            check = False
            return check

        else:            

            character_number = character_number + 1
            check = True
            html.write("&nbsp;&nbsp;")
            return check

    if char == "\n":
        
        character_number = character_number + 1
        comment = False
        check = True
        html.write("<br>")
        return check
        
    elif regresion == True:
        
        regresion = False
        sequence = sequence + char
        character_number = character_number + 1
        check = True
        return check
    
    elif char == "+" or char == "-" or char == "*" or char == "/" or char == "<" or char == ">" or char == "=" or char == "(" or char == ")" or char == "'" and regresion == False:

        if list_of_characters[character_number - 1] == " " or list_of_characters[character_number - 1] == "\n" and list_of_characters[character_number + 1] == " " or list_of_characters[character_number + 1] == "\n":

            if comment == True:
                character_number = character_number + 1
                check = False
                return check
            
            else:
                regresion = True
                check = True
                return check
        
        else:

            if char == "<" or char == ">" or char == "=" or char == "-" or char == "+":

                sequence = sequence + char
                character_number = character_number + 1
                check = False
                return check
            

            else:

                character_number = character_number + 1
                check = False
                return check

    else:

        sequence = sequence + char
        if sequence[0] == ";":
            comment = True
            pass
        character_number = character_number + 1
        check = False
        return check
    
#Function to receive a token and compare it with a regex
def regular_expresion(token):

    
    #Check if the token is a constant 
    if regex.fullmatch(constant, token):

        return 22
    
    #Check if the token is a constant float
    elif regex.fullmatch(constant_float, token):

        return 23

    #Check if the token is a special symbol
    elif regex.fullmatch(special_simbols, token):
        
        return 24

    #Check if the token is a comment
    elif regex.fullmatch(commentary, token):

        return 25

    #Check if the token is an identifier
    elif regex.fullmatch(identifiers, token):
        
        if token in tokens:
            return token
        
        else:
            return 21
    
    #Token does not match any regex expresion
    else:
        return 20







#-----------------------------------MAIN-----------------------------------

#Path of the file to read
filepath = "code.sch"

#Read every Character of the file and append in a list
characters = [ch for ch in open(filepath).read()]
characters_in_file = len(characters)

#HTML FILE
filepath_html = "index.html"
html = open(filepath_html, "r+")
html.write(html_samp_start)

#Check while the file doesnt finish
while check != "EOF":
    
    #Check Token until break
    while True:

        #Number or Value of token
        token = get_token(characters_in_file,characters)

        #If the token generated succesfully 
        if token == True:
            #End of file token
            if sequence == "" and end_of_file == True:
                sequence == "EOF"
                break
            #New Line token in a file
            if sequence == "" and end_of_file == False:
                pass
            #Token
            else:
                #Number or value of token
                ver_tk = regular_expresion(sequence)
                #Check if token is numeric or is reserved
                if is_numeric(ver_tk):
                    #Write the token not reserved in the HTML File
                    if ver_tk == 20:
                        tkn = "<span class = 'notvalid'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""
                    elif ver_tk == 21:
                        tkn = "<span class = 'identifier'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""
                    elif ver_tk == 22:
                        tkn = "<span class = 'cons_int'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""
                    elif ver_tk == 23:
                        tkn = "<span class = 'cons_float'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""
                    elif ver_tk == 24:
                        tkn = "<span class = 'special'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""
                    elif ver_tk == 25:
                        tkn = "<span class = 'comment'>" + sequence + "</span>"
                        html.write(tkn)
                        sequence = ""

                else:
                    #Writes a reserved token in the HTML file
                    html.write(tokens[regular_expresion(sequence)])
                    sequence = ""
                
                break

#Add the end of a generic HTML File
html.write(html_samp_end)
#Close Files
html.close()


print("\n\nDone! file export succesful!, the file name is \"index.html\"")
