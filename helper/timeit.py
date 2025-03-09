import time

def timeit(func):
    """
    A decorator to time the execution duration of a function

    Args:
        func (_type_): python function
    """
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Time taken: {total_time:.4f} seconds')
        return result
    return timeit_wrapper