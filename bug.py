def function_with_uncommon_error(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Cannot divide by a non-number")
        return None
    return result

# The following line demonstrates an uncommon error:
result = function_with_uncommon_error("hello")
print(result)