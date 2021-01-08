def valid_mod(mod):
    if len(mod) == 6:
        return mod[:2].isalpha() and mod[2:].isdigit()
    elif len(mod) == 7:
        if mod[:3].isalpha():
            return mod[3:].isdigit()
        elif mod[:2].isalpha():
            return mod[2:-1].isdigit() and mod[-1].isalpha()
        else:
            return False
    elif len(mod) == 8:
        return mod[:3].isalpha() and mod[3:-1].isdigit() and mod[-1].isalpha()
    return False

def add_preclusions(curr_mods, random_mod):
    try:
        curr_mods.extend(list(filter(lambda x: valid_mod(x), map(lambda x: x[:-1] if x[-1] ==',' or x[-1] =='.' \
        else x, random_mod['preclusion'].split()))))
    except:
        pass

def add_prerequisites(curr_mods, random_mod):
    try:
        curr_mods.extend( \
        list(filter(lambda x: valid_mod(x), map(lambda x: x[:-1] if x[-1] == ',' or x[-1] == '.' \
            else x, random_mod['prerequisite'].split()))))
    except:
        pass

def add_corequisites(curr_mods, random_mod):
    try:
        curr_mods.extend(list(filter(lambda x: valid_mod(x), map(lambda x: x[:-1] if x[-1] == ',' or x[-1] == '.' \
            else x, random_mod['corequisite'].split()))))
    except:
        pass

def add_fulfillReq(curr_mods, random_mod):
    try:
        curr_mods.extend(random_mod['fulfillRequirements'])
    except:
        pass

def add_all(curr_mods, random_mod):
    add_prerequisites(curr_mods, random_mod)
    add_preclusions(curr_mods, random_mod)
    add_corequisites(curr_mods, random_mod)
    add_fulfillReq(curr_mods, random_mod)