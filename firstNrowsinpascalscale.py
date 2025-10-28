def pascal_triangle(n):
    # Initialize the first row of Pascal's Triangle with value 1 as a starting point
    trow = [1]
    
    # Create a list 'y' filled with zeros to be used for calculations
    y = [0]
    
    # Iterate through a range starting from 0 up to the maximum of 'n' or 0 (taking the maximum to handle negative 'n')
    for x in range(max(n, 0)):
        # Print the current row of Pascal's Triangle
        print(trow)
        
        # Update the current row based on the previous row by calculating the next row using list comprehension
        # The formula for generating the next row in Pascal's Triangle is based on addition of consecutive elements
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    
    # Return True if 'n' is greater than or equal to 1, else return False
    return n >= 1

# Generate Pascal's Triangle up to row 6 by calling the 'pascal_triangle' function
pascal_triangle(6) 
