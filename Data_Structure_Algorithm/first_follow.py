import sys
sys.setrecursionlimit(60)     #program excution in 60times otherwise system overflow 

def first(string):            #fist function with data type string for finding first 
                              #print("first({})".format(string))
    first_ = set()
    if string in non_terminals:     #if first element in nonterminal example E->TB
        alternatives = productions_dict[string] #Use alternative

        for alternative in alternatives: # loop use for dependency alternative
            first_2 = first(alternative)
            first_ = first_ |first_2    #resurssion

    elif string in terminals:         #found terminal symbol
        first_ = {string}
    elif string=='' or string=='@':     #found null or space
        first_ = {'@'}

    else:
        first_2 = first(string[0])            #if found null in index zero in following production
        if '@' in first_2:
            i = 1
            while '@' in first_2:                      #print("inside while")

                first_ = first_ | (first_2 - {'@'})    #print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2  #print("returning for first({})".format(string),first_)
    return  first_


def follow(nT):                            #follow function with data type string for finding follow
                                           #print("inside follow({})".format(nT))
    follow_ = set()                        #print("FOLLOW", FOLLOW)
    prods = productions_dict.items()
    if nT==starting_symbol:                #starting symbol follow startwith $ symbol
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:                   #print("nt to rhs", nt,rhs)
        for alt in rhs:   
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2    #print("returning for follow({})".format(nT),follow_)
    return follow_





no_of_terminals=int(input("Enter no. of terminals: "))   #Enter number of terminal symbol

terminals = []                                  # balnk list use for store terminal symbol

print("Enter the terminals :")                  #print Terminal Symbol
for _ in range(no_of_terminals):                #loop use for terminal symbollimit 
    terminals.append(input())                   #Store and add terminal symbol one by one in blank list terminal[]

no_of_non_terminals=int(input("Enter no. of non terminals: "))  #Enter number of non terminal symbol

non_terminals = []                                 #balnk list use for store nonterminal symbol

print("Enter the non terminals :")                 #loop use for nonterminal symbollimit 
for _ in range(no_of_non_terminals):
    non_terminals.append(input())                  #Store and add nonterminal symbol one by one in blank list terminal[]

starting_symbol = input("Enter the starting symbol: ") #Enter starting symbol in a production 

no_of_productions = int(input("Enter no of productions: ")) # number Of production

productions = []                                   #list use for store production

print("Enter the productions:")               #print("terminals", terminals)
for _ in range(no_of_productions):
    productions.append(input())               #print("non terminals", non_terminals)
 
                                              #print("productions",productions)



productions_dict = {} #blank dictionatry

for nT in non_terminals:
    productions_dict[nT] = [] 


#print("productions_dict",productions_dict)

for production in productions:
    nonterm_to_prod = production.split("->")      #separte production and starting symbol
    alternatives = nonterm_to_prod[1].split("/")  #found or in production
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)  #alternative or dependency 

#print("productions_dict",productions_dict)

#print("nonterm_to_prod",nonterm_to_prod)
#print("alternatives",alternatives)


FIRST = {}                 #blank dictionary first
FOLLOW = {}                #blank dictionary use for follow

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()      # for finding first function call set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()     #for finding follow function call set()

#print("FIRST",FIRST)

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal) #print("FIRST",FIRST)


FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal) #print("FOLLOW", FOLLOW)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow')) #print {:^20} use for formating ,left-aligned with width 20 
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal]))) # print