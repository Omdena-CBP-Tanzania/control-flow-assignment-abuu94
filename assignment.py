#solution of task 1
def while_loop():
    number = 0
    while number <= 20:
        if number%2==0:
            if number==16:
                break;
            print(number)
        number+=1
while_loop()

#solution of task 2
def for_loop_continue():
    for i in range(1,16):
        if i % 3 == 0:
            continue
        print (i)
for_loop_continue()

#solution of task 3
def for_loop_continue():
    number= int(input("Enter a number: "))
    if number > 0:
        print(f" {number} is a positive number.")
    elif number < 0:
        print(f" {number} is a negetive number.")
    else:
        print(f" {number} is a zero.")
for_loop_continue()

def nested_loops():
    for i in range(1, 6):            # Outer loop for rows
        for j in range(1, 6):        # Inner loop for columns
            product = i * j
            print(f"{product}\t", end='')  # Print the product followed by a tab
        print()
nested_loops()