import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    results = {}

    #initialising an array from the list and shaping it into a matrix
    before_array = np.array(lst)
    after_array = before_array.reshape(3,3)
    flattened_matrix = after_array.flatten()

    #computing the mean
    row_mean = np.mean(after_array, axis=1)
    column_mean = np.mean(after_array, axis=0)
    mean = np.mean(flattened_matrix)
    results["mean"] = [list(column_mean), list(row_mean), mean]

    #computing the variance
    row_var = np.var(after_array, axis=1)
    column_var = np.var(after_array, axis=0)
    var = np.var(flattened_matrix)
    results["variance"] = [list(column_var), list(row_var), var]


    #computing the standard deviation
    row_std = np.std(after_array, axis=1)
    column_std = np.std(after_array, axis=0)
    std = np.std(flattened_matrix)
    results["standard deviation"] = [list(column_std), list(row_std), std]


    #computing the maximum
    row_max = np.max(after_array, axis=1)
    column_max = np.max(after_array, axis=0)
    max = np.max(flattened_matrix)
    results["max"] = [list(column_max), list(row_max), max]

    #computing the minimum
    row_min = np.min(after_array, axis=1)
    column_min = np.min(after_array, axis=0)
    min = np.min(flattened_matrix)
    results["min"] = [list(column_min), list(row_min), min]

    #computing the sum
    column_sum = np.sum(after_array, axis=0)
    row_sum = np.sum(after_array, axis=1)
    sum = np.sum(flattened_matrix)
    results["sum"] = [list(column_sum), list(row_sum), sum]

    return  results
