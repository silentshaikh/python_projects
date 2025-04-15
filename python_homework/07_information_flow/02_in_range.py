# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def num_in_High_low_range(num,low,high):
    if num<=high and num>=low:
        return True
    else:
       return  False

print(num_in_High_low_range(5,4,5))
print(num_in_High_low_range(3,4,5))