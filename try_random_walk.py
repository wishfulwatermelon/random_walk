from add_other_modules import add_all, valid_mod
from filter_clickable_mods import check_clickable, only_clickable
from get_mod_data import get_mod_data
import random

which_mod = False

def get_valid_mod():
    global which_mod
    while not which_mod or not valid_mod(which_mod) or not check_clickable(which_mod):
        which_mod = input("Input mod here: ")

get_valid_mod()

all_visited_mods = [which_mod]
random_mod = get_mod_data(which_mod)
random_mod = only_clickable(random_mod)

def get_path(module, steps):
    related_mods = []
    add_all(related_mods, get_mod_data(module))

    related_mods = only_clickable(related_mods)


    current_mod_list = [module]



    def random_walk(related_mods, steps):
        # print("at recursive call")
        # print("Current mod list:")
        # print(current_mod_list)
        # print("related mods")
        # print(related_mods)
        # print(steps != 0)
        # print(current_mod_list == [])
        # print(list(filter(lambda x: x not in all_visited_mods, related_mods)))


        if steps == 0:
            return True

        # if max chain > no of steps
        # means steps will not be 0 when
        # all the possible mods when at the first related mods have been visited
        # check if all the related mods are in all_visited_mods. Remove if they are
        elif steps != 0 and current_mod_list == [module] and not list(filter(lambda x: x not in all_visited_mods, related_mods)):
            print("Chain length shorter than max depth")
            return False

        # see if there's anything in the related mods first? then if not go up again
        elif not related_mods:
            # back up from current_mod_list
            current_mod_list.pop()

            # print("nothing in related mods")
            # print(related_mods)

            # get the possible mods the next thing in the list instead
            current_mod = current_mod_list[-1]
            related_mods = []
            add_all(related_mods, get_mod_data(current_mod))
            related_mods = only_clickable(related_mods)

            return random_walk(related_mods, steps + 1)

        else:
            foo = random.randint(0, len(related_mods) - 1)
            possible_mod = related_mods[foo]
            related_mods.pop(foo)
            all_visited_mods.append(possible_mod)
            current_mod_list.append(possible_mod)
            # now related_mods won't have that module
            # is there a way to keep track?
            # keep track in all_visited_mods
            # if i backtrack and see that all the possible mods are in visited, then i backtrack again. :D

            possible_new_list = []
            add_all(possible_new_list, get_mod_data(possible_mod))
            possible_new_list = only_clickable(possible_new_list)
            possible_new_list = list(filter(lambda x: x not in all_visited_mods, possible_new_list))

            # need a boolean to check if the current related_mods got anything as well
            # check if related_mods
            unvisited_related_mods = list(filter(lambda x: x not in all_visited_mods, related_mods))

            # print("possible new list")
            # print(possible_new_list)
            # print("steps: " + str(steps))
            # print("All visited mods:")
            # print(all_visited_mods)
            # print("related mods")
            # print(related_mods)
            # print("univisited related mods: ")
            # print(unvisited_related_mods)

            # if there is nothing in the current list, try the related mods?
            if not possible_new_list:
                # if nothing inside, then repeat
                current_mod_list.pop()
                return random_walk(unvisited_related_mods, steps)

            else:
                return random_walk(possible_new_list, steps - 1)

    random_walk(related_mods, steps)
    return current_mod_list



no_steps = int(input("How many steps: "))

print(get_path(which_mod, no_steps))