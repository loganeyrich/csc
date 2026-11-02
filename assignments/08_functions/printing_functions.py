'''
Logan Eyrich
Chapter 8
Difficulty: 7/10
'''
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("These models have been printed:")
    for completed_model in completed_models:
        print(completed_model)