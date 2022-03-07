# 1. Name:
#      Penelope Sanchez
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      Design the Sub-List sort algorithm. 
# 4. What was the hardest part? Be as specific as possible.
#      Combinate the sublists in order to verify the values
# 5. How long did it take for you to complete the assignment?
#      4 hrs

def main():
   test()
   display(sort(read()))

def read():
   array = input("Input a list of numbers seperated by spaces: ")  
   array_list = array.split() #arrays
   for i in range(len(array_list)): #strings -> integers
      array_list[i] = int(array_list[i])   
   return array_list

def sort(array):
   size = len(array)
   value = array

   index = []
   for i in range(len(value)):
      index.append(" ")
   num = 2

   while num > 1:
      num = 0
      first_value_1 = 0
      index = [] #reset the index list
      for i in range(len(value)):
         index.append(" ")

      #If the beginning of the first sublist is the last element in the other sublist
      while first_value_1 < size:

         #Creating Sub-lists.
         last_value_1 = first_value_1 + 1
         while last_value_1 < size and value[last_value_1 - 1] <= value[last_value_1]:
            last_value_1 += 1
         first_value_2 = last_value_1
         if first_value_2 < size:
            last_value_2 = first_value_2 + 1
         else:
            last_value_2 = first_value_2
         while last_value_2 < size and value[last_value_2 - 1] <= value[last_value_2]:
            last_value_2 += 1        
         num += 1

         #Combines the two sub-lists 
         combine(value, index, first_value_1, first_value_2, last_value_2)

         #Creates the new starting point.
         first_value_1 = last_value_2

      # Swaps the index and values.
      value = index
   return value

def test():
   assert([] == sort([])) #Empty 
   assert([10] == sort([10])) #Singular 
   assert([10,20] == sort([10,20])) #Small Sorted 
   assert([10,20] == sort([20,10])) #Small Unsorted 
   assert([1,3,5,7,9,11,13,15,17] == sort([1,3,5,7,9,11,13,15,17])) #Sorted Odd 
   assert([1,3,5,7,9,11,13,15,17] == sort([17,15,13,11,9,7,5,3,1])) #Reversed Odd 
   assert([0,2,4,6,8,10,12,14,16] == sort([0,2,4,6,8,10,12,14,16])) #Sorted Even 
   assert([0,2,4,6,8,10,12,14,16] == sort([16,14,12,10,8,6,4,2,0])) #Reversed Even 
   assert([5,5,10,10,15,40,40] == sort([40,5,10,10,15,5,40])) #Duplicates 
   print("Passes all test cases!")

def combine(source, destination, first_value_1, first_value_2, last_value_2): #Combines the two sub-lists and returns the destination array
   last_value_1 = first_value_2
   for i in range(first_value_1, last_value_2):
      if (first_value_1 < last_value_1) and (first_value_2 == last_value_2 or source[first_value_1] < source[first_value_2]):
         destination[i] = source[first_value_1]
         first_value_1 += 1
      else:
         destination[i] = source[first_value_2]
         first_value_2 += 1
   return destination

def display(array): #Print sorted values
   print(f"This is the sorted list: {array}")

#Main call
if __name__ == "__main__":
   main()
