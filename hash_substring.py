# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    command = input()

    # input from keyboard
    if command.startswith('I'):

        searchFor = input()
        pattern = input()

    # input from file
    elif command.startswith('F'):
        
        file = open('./tests/' + '06', 'r')

        searchFor = file.readline()
        pattern = file.readline()
    
    # return both lines in one return
    if 1 <= len(searchFor) <= len(pattern) <= (5 * 10**5):
        return(pattern, searchFor)
    else:
        exit()

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    copy = pattern
    position = 0
    cutoff = 0
    occurances = []

    while cutoff < len(pattern):
        position = copy.find(text)
        if (position < 0):
            break
        occurances.append(position+cutoff)

        copy = copy[position+1:len(copy)]
        cutoff = cutoff + position+1
    # and return an iterable variable
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

