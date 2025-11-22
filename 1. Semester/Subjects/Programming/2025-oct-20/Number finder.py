# Du skal lave et system der skal få tallet 100 til et andet tal.

# Du skal lave tre funktioner for at få det til at virke. Må ikke skrives ud i et. 

# For hver funktion må der kun bruges en operations metode af disse +, -, * eller /. 

# Det må ikke bruges den samme regne metode igen og tallene der må bruger er 1-10.

# Du skal få programmet til at regne det hele i main via funktions kald, argumenter og return værdier.

# Tallene der skal opnåes:
# 37

# 53

# 86

# et random tal i selv finder. (44)

def to_37_first_step(x):
    return x / 10
def to_37_second_step(x):
    return x * 3
def to_37_third_step(x):
    return x + 7


def to_53_first_step(x):
    return x + 6
def to_53_second_step(x):
    return x * 2   
def to_53_third_step(x):
    return x / 4


def to_86_first_step(x):
    return x / 2
def to_86_second_step(x): 
    return x - 7
def to_86_third_step(x):
    return x * 2


def to_44_first_step(x): 
    return x / 2
def to_44_second_step(x):
    return x + 3
def to_44_third_step(x):
    return x - 9



def main():
    
    result = to_37_third_step(to_37_second_step(to_37_first_step(100)))
    print(int(result))
    
    result = to_53_third_step(to_53_second_step(to_53_first_step(100)))
    print(int(result))
    
    result = to_86_third_step(to_86_second_step(to_86_first_step(100)))
    print(int(result))
    
    result = to_44_third_step(to_44_second_step(to_44_first_step(100))) 
    print(int(result))

main()
