# range to generate : range(2.3, 3.78, 0.01)

def range_generator(start, end, step):
    
    while(start <= end):
        yield start
        start += step

# range to generate : range('c','x',2)

def alphabetical_range_generator(start , end , step):
    start = ord(start)
    end = ord(end)
    while(start <= end):
        yield chr(start)
        start = start + step


if __name__ == "__main__" :

    for number in range_generator(2.3, 3.78, 0.01) :
        print(f"{number:.2f}")
        

    for char in alphabetical_range_generator('c','x',2):
        print(char)
    
    

