def learn_how_to_print_f_strings():
    choco_nbr = input("Combien de chocolatines?").upper()
    var = f"""Je mange {choco_nbr} chocolatines"""

    print(var)

def discover_basic_math():
    a = 2
    b = 3
    somme = a+b
    diff = a-b

    mult = a*b
    div = a/b
    div_entiere = a//b
    reste_div = a%b

    expo = a**b

    sentence = f"""Resultats pour a={a} et b={b}
        -somme = {somme}
        -diff = {diff}

        -mult = {mult}
        -div = {div}
        -div_entiere = {div_entiere}
        -reste_div = {reste_div}

        -expo = {expo}
    """

    print(sentence)



new_a = 4
new_b = 2

for _ in range(10):
    new_a += new_b
    print(new_a)

comparaison_1 = new_a==new_b #ON POSE LA QUESTION
comparaison_2 = new_a>=new_b #ON POSE LA QUESTION
comparaison_3 = new_a<new_b #ON POSE LA QUESTION

sentence_2 = f"""Pour new_a={new_a}, new_b={new_b}:
    -new_a==new_b : {comparaison_1}
    -new_a>=new_b : {comparaison_2}
    -new_a<new_b : {comparaison_3}
    
"""
print(sentence_2)
print("Coucou")