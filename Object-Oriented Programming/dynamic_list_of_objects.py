# Author:   Travis-Owens
# Date:     2019-1-30
# Purpose:  Demonstrating how to create a dynamic number of objects and store them in a list.
#           Then how to access each object in the list.

class main:
    def __init__(self):
        self.objects_list = []   # Create empty list to store objects.
        self.create_objects()    # Call the function create_objects. This will populate the objets_list
        self.print_objects()     # Call the function print_objects. This will loop through each object and print the self value of x

    def create_objects(self):
        # Use a for loop to create 5 objects,
        # Create the object and pass the integer value of i
        # Append the object to the objects_list
        for i in range(5):
            self.objects_list.append(test_object(i))

    def print_objects(self):
        # Use a for loop to access each object in the list
        # For each object,represnted by obj, call the print_x() function of the test_object class
        # Each object will print out the integer value assigned in create_objects()
        for obj in self.objects_list:
            obj.print_x()

class test_object(object):
    def __init__(self, y):
        # Assign the passed integer to a self variable.
        # Self variables are unique to each object that is created.
        self.x = y

    def print_x(self):
        # When called print the vairable self.x for the given object
        print(self.x)

if __name__ == "__main__":
    main()                  # Execute the main class
