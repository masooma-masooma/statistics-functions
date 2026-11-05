import math

import matplotlib.pyplot as plt
import pandas as pd


# Task 01
def find_minimum(grades):
    """
    Find the minimum value in a list of numbers.

    :param grades: A list of grades.
    :return: The minimum value in a list of numbers.
    """
    if not grades:
        raise ValueError("List cannot be empty.")

    minimum = grades[0]

    for grade in grades:
        if grade < minimum:  # if grade is less than minimum then update minimum
            minimum = grade
    return minimum


def find_maximum(grades):
    """
    Find the maximum value in a list of numbers.

    :param grades: A list of grades.
    :return: The maximum value in a list of numbers.
    """
    if not grades:
        raise ValueError("List cannot be empty.")

    maximum = grades[0]
    for grade in grades:
        if grade > maximum:  # if grade > maximum then update the maximum
            maximum = grade
    return maximum


def find_mean(grades):
    """
    Find the mean value in a list of numbers.

    :param grades: A list of grades.
    :return: The mean, rounded to 3 decimal places.
    """
    if not grades:
        raise ValueError("List cannot be empty.")

    total_sum = 0

    for grade in grades:
        total_sum += grade
    mean = total_sum / len(grades)  # Compute mean after summing all values

    return round(mean, 3)  # round the result up to 3 decimal places


def find_variance(grades):
    """Population variance (divide by n)."""
    if not grades:
        raise ValueError("List cannot be empty.")
    mean = find_mean(grades)

    squared_deviations_sum = sum((grade - mean) ** 2 for grade in grades)
    variance_value = squared_deviations_sum / len(grades)

    return round(variance_value, 2)


def find_sample_variance(grades):
    """Sample variance (divide by n - 1)."""
    if len(grades) < 2:
        raise ValueError("Need at least 2 values for sample variance.")

    mean = find_mean(grades)
    squared_deviations_sum = sum((grade - mean) ** 2 for grade in grades)

    # Divide by n - 1 for sample variance
    sample_variance = squared_deviations_sum / (len(grades) - 1)

    return sample_variance


def find_standard_deviation(grades, is_sample=False):
    """
    Calculates the standard deviation of the grades.
    """
    if not grades:
        raise ValueError("List cannot be empty.")
    if not is_sample:
        population_variance = find_variance(grades)
        standard_deviation = math.sqrt(population_variance)
        return round(standard_deviation, 2)
    else:
        sample_variance = find_sample_variance(grades)
        standard_deviation = math.sqrt(sample_variance)
        return round(standard_deviation, 2)


def sort_list(grades):
    """
    Sorts the list of grades in ascending order using the bubble sort algorithm.

    :param grades: A list of grades.
    :return: A new sorted list (the original list is not changed).
    """
    grades = list(grades)  # make a copy so the original list stays the same
    n = len(grades)

    # Bubble Sort Algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if grades[j] > grades[j + 1]:
                # Swap the elements
                grades[j], grades[j + 1] = grades[j + 1], grades[j]

    return grades


def find_median(grades):
    if not grades:
        raise ValueError("List cannot be empty.")
    sorted_grades = sort_list(grades)
    n = len(sorted_grades)
    if n % 2 == 0:
        middle1 = sorted_grades[n // 2 - 1]
        middle2 = sorted_grades[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_grades[n // 2]


def find_median_absolute_deviation(grades):
    # Step 1: Find the median of the list
    median_value = find_median(grades)
    # Step 2: Calculate the absolute deviations from the median
    deviations = []
    for grade in grades:
        deviation = abs(grade - median_value)
        deviations.append(deviation)
    # Step 3: Find the median of the absolute deviations
    mad_value = find_median(deviations)
    return mad_value


# Yeh hissa sirf tab chalega jab aap is file ko direct run karein
# (python stats_functions.py). Jab tests is file ko import karenge,
# tab yeh nahi chalega.
if __name__ == "__main__":
    # Task 2: use the functions created above on the grade list
    grades = [8, 6, 1, 7, 8, 9, 8, 7, 10, 7, 6, 9, 7]
    print(f"The list of grades : {grades} ")
    print(f"The Minimum grade in the grades list : {find_minimum(grades)}")
    print(f"The Maximum grade in the grades list : {find_maximum(grades)}")
    print(f"The mean grade in the grades list : {find_mean(grades)}")
    print(f"The variance in the grades list : {find_variance(grades)}")
    print(f"The standard deviation of the grades list : {find_standard_deviation(grades, False)}")
    print(f"The Median of the grades list : {find_median(grades)}")
    print(f"The Median Absolute Deviation MAD of the grades list : {find_median_absolute_deviation(grades)}")
    print(f"The sorted grades list : {sort_list(grades)}")

    # Task 3
    df = pd.read_csv("housing.csv")
    print(df.head(11))
    num_district = df.shape[0]
    print(num_district)

    # Task 4
    print("-------------------------------------- Task 4 Start here---------------")
    col = list(df["median_house_value"])
    mean_val = find_mean(col)
    print(mean_val)

    columns_to_plot = ["households", "median_income", "housing_median_age", "median_house_value"]
    df[columns_to_plot].hist(bins=50, figsize=(20, 15))
    plt.show()
