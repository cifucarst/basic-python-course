def spam():
    global eggs
    eggs = 'spam' # this is the global


def bacon():
    eggs = 'bacon' # this is a local
    


def ham():
    print(eggs) # this is the global


eggs = 42 # this is the global
spam()
print(eggs)