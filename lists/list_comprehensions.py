# instead of using 
squares_of_evens  = []
for i in range(10):
    if i % 2 == 0:
        squares_of_evens.append(i * i)
        
        
# consider using
squares_of_evens = [i*i for i in range(10) if i % 2 == 0]

