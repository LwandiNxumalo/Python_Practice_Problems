"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
actual_min = 30

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(actual_min):
    """Calculate the bake cooking time.
    
    Parameters:
        actual_time: The time it takes for baking.
    
    Returns:
        int: The total time elapsed (in minutes) baking.

    This function takes one integer representing the the actual minuutes the lasagna
    should be baked and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    elapsed_bake_time = EXPECTED_BAKE_TIME - actual_min    
    return elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the Preparation time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    
    Returns:
        int: The expected time (in minutes) preparing and baking.

    This function takes one integer representing the number of lasagna 
    layers. It calculates how many minutes you would spend making them.
    
    """
    expected_time = PREPARATION_TIME * number_of_layers

    return expected_time

# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.

# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.

# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    expected_bake_time = PREPARATION_TIME * number_of_layers
    total_bake_time = expected_bake_time + elapsed_bake_time

    return total_bake_time

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
