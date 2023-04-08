"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
# declare constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    # return a value
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers add to lasagna.
    :return: int - preparation time (in minutes)

    Function that takes the number of layers add to the lasagna as an
    argument and returns how many minutes spend making them.
    """

    # return a value
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time :int - the number of minutes the lasagna has been baking in the oven
    :return: int - preparation time (in minutes)

    This function return the total number of minutes cooking, or the sum of preparation time and the time the lasagna has already spent baking in the oven.
    """
# return a value
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
