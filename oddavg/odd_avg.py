# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases


def odd_average(list_of_numbers):
    try:
        odd_counter = 0
        odd_sum = 0
        for number in list_of_numbers:
            if number % 2 != 0:
                odd_counter += 1
                odd_sum += number
        return odd_sum/odd_counter
    except ZeroDivisionError:
        return 0