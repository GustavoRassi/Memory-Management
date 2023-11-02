# ====================================
# Name: Gustavo A. Rassi
# Project: Swift's Memory Management using python
# CCOM4025-LB5
# ====================================

import platform
import os
import random

class Memory:

    # Constructor
    def __init__(self):
        self.rows = 10 # 10 rows for 2d array (matrix)
        self.columns = 10 # 10 columns for 2d array (matrix)
        self.original_array_1d = [] # Original Vector
        self.original_array_2d = [] # Original Matrix
        self.modified_array_1d = [] # Vector used for swapping
        self.modified_array_2d = [] # Matrix used for swapping

#==========================================

    # Menu of options
    def displayMenu(self):
        print("Menu:")
        print("========================================================")
        print("1. Create and initialize matrix")
        print("2. Print matrix")
        print("3. Access and print element from matrix and equivalent in vector")
        print("4. Access and replace element from matrix and equivalent in vector")
        print("5. Swap arrays")
        print("0. Exit program")
        print("========================================================")

#==========================================

    # Initialize vector
    def initializeArray1D(self):
        for row in self.original_array_2d:
            for element in row:
                self.original_array_1d.append(element) 
        self.modified_array_1d = self.original_array_1d

#==========================================

    # Initialize matrix
    def initializeArray2D(self):
        for _ in range(self.rows):
            row = []
            for _ in range(self.columns):
                random_integer = random.randint(1,100)
                row.append(random_integer)
            self.original_array_2d.append(row)
        self.modified_array_2d = self.original_array_2d

#==========================================

    def _accessAndPrintElement(self, row, col):
        # Access and print element in the 2D array
        print(f"Matrix: Element in 2D array at ({row}, {col}) is {self.original_array_2d[row][col]}.")
        self.getArray2D()

        # Calculate index for 1D array equivalent
        index = row * len(self.original_array_2d[0]) + col

        # Access and print element in the 1D array
        print(f"\nVector: Equivalent element in 1D array is {self.original_array_1d[index]}.")

        # Print 1D array
        print(self.getArray1D())

#==========================================
    # Access and swap elements
    def _accessAndReplaceElement(self, row, col):
        # Extract element from 2d array (matrix)
        element = self.original_array_2d[row][col]

        # Calculate index to find the same element in both 2d & 1d arrays
        index = row * len(self.original_array_2d[0]) + col

        self.original_array_2d[row][col] = self.original_array_1d[index]
        self.original_array_1d[index] = element

#==========================================

    # Prints vector
    def getArray1D(self):
        return self.modified_array_1d
    
#==========================================

    # Print matrix
    def getArray2D(self):
        for row in self.modified_array_2d:
            print(row)

#==========================================

    # Swap all the elements between matrix and vector
    def swapElements(self):

        print("2D array before swap:\n")
        self.getArray2D()
        input("press any key to continue...")
        print("1D array before swap:\n")
        print(self.getArray1D())
        input("press any key to continue...")

        # Copies elements from 2d array (matrix) to temporary 1D array by rows
        temp_array = []
        for row in self.modified_array_2d:
            temp_array += row
        
        # Elements from 1d array (vector) are copied to the 2d array (matrix)
        index = 0
        for i in range(self.rows):
            for j in range(self.columns):
                self.modified_array_2d[i][j] = self.modified_array_1d[index]
                index += 1
        
        # Elements from temporary array are passed to the 2d array (vector)
        _index = 0
        for element in temp_array:
            self.modified_array_1d[_index] = element
            _index += 1

        print("2D array after swap:\n")
        self.getArray2D()
        input("press any key to continue...")
        print("1D array after swap:\n")
        print(self.getArray1D())

#=========================================================================
# MAIN

# Object instantiation
memory = Memory()
    
option = None
while option != 0:
    # Display menu of options
    memory.displayMenu()
    option = int(input("Please select an option\n> "))

    if option == 1:
        if len(memory.getArray1D()) != 0:
            print("Matrix is already initialized.")
        else:
            memory.initializeArray2D()
            print("Matrix has been initialized.")
            memory.initializeArray1D()

    elif option == 2:
        print("Array 2d:")
        memory.getArray2D()

    elif option == 3:
        print("Enter the following values for the element you want to access and print...")
        row = int(input("Row: "))
        col = int(input("Column: "))
        memory._accessAndPrintElement(row, col)

    elif option == 4:
        print("Enter the following values for the element you want to access and replace.")
        row = int(input("Row: "))
        column = int(input("Column: "))
        memory._accessAndReplaceElement(row, column)
        print("Element is replaced succesfully!")

    elif option == 5:
        memory.swapElements()
        print("Arrays have swapped succesfully!")
        input("Press any key to continue...")

    elif option == 0: # Exit the program
        print("Thank you for using the program! Exiting...")

    else:
        print(f"**Option {option} does not exist.**")
    
    input("Press any key to continue...")

    if platform.system() == "Windows":
        os.system("cls") # Clear screen on windows
    else:
        os.system("clear") # Clear screen on mac
