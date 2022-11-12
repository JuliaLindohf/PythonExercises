# to implement a bubble sort algorithm in python 
class sort_bubblesort:
  def __init__(self, input_list):
    self.vector = input_list
  def bubble_sort(self): 
    # to process input list 
    L = len(self.vector) 
    swap = True 
    count = 0
    while swap == True: 
      for i in range(0, L-1): 
        temp1 = self.vector[i] 
        temp2 = self.vector[i+1] 
        if temp1 > temp2: 
           self.vector[i] = temp2
           self.vector[i+1] =temp1
           count += 1 
      if  count == 0:
        swap = False 
      count = 0 
