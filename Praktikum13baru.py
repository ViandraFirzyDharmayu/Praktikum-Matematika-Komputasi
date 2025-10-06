def define_sets():
    set_A = {1, 2, 3, 4, 5}
    set_B = set([3, 4, 5, 6, 7])
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    print("===========================================\n")

def representation_of_sets():
    set_C = {1, 2, 2, 3, 4} # Duplicates will be removed
    print(f"Set C (duplicates removed): {set_C}") # Output 
    print("===========================================\n")

def cardinality_of_set():
    set_D = {1, 2, 3, 4, 5}
    print(f"Cardinality of Set D: {len(set_D)}")
    print("===========================================\n")

def empty_set():
    empty_set = set()
    print(f"Empty set: {empty_set}")
    print("===========================================\n")

def check_subsets():
    set_E = {1, 2, 3}
    set_F = {1, 2, 3, 4, 5}
    is_subset = set_E.issubset(set_F) # Check if E is a subset of F
    print(f"Is Set E a subset of Set F? {is_subset}")
    print("===========================================\n")

def check_equal_sets():
    set_G = {1, 2, 3}
    set_H = {3, 2, 1}
    are_equal = set_G == set_H # Check if sets G and H ar equal
    print(f"Are Set G and Set H equal? {are_equal}")
    print("===========================================\n")

if __name__ == "__main__":
    define_sets()
    representation_of_sets()
    cardinality_of_set()
    empty_set()
    check_subsets()
    check_equal_sets()
