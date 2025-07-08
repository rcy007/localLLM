# Define a function that takes two numbers as input arguments
def add_numbers(num1, num2):
    # Return the sum of the two numbers
    return num1 + num2

# Call the function with two sample numbers
result = add_numbers(3, 5)

# Print the result to the console
print(result)


def subtract_numbers(num1, num2):
    return num1 - num2


result = subtract_numbers(10, 4)
print(result)


def print_image(image_path):
    # Open and display an image from a specified path
    import matplotlib.pyplot as plt
    img = plt.imread(image_path)

    # Display the image using matplotlib's imshow function
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()


# Read a csv using pandas
import pandas as pd


def read_csv(file_path):
    # Use pandas to read a CSV file from a specified path
    df = pd.read_csv(file_path)
    # Return the DataFrame containing the data
    return df


# Call the function with a sample CSV file path
df = read_csv('data.csv')
# Print the first few rows of the DataFrame to the console

print(df.head())


def divide(a, b):
    if b == 0:
        return 'Error: Division by zero'
    else:
        return a / b


result = divide(10, 2)
print('Result:', result)


import subprocess
subprocess.run(["npm", "run", "dev"])
subprocess.run(["npm", "run", "dev"])
