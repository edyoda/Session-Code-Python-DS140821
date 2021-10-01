# pdb is a inbuilt python debugger.

# What is Debugging ?
# Finding and Fixing the Error.

a = input()
b = input()
#breakpoint()
def sum_the_values(a,b):
    print('We are inside the function')
    print(int(a)+int(b))
    
sum_the_values(a,b)

# pdb console appears whenever it sees a breakpoint().
# c(continue) => continue all the leftover code after wherever we are.
# n(next) => runs the very next piece of code.
# s(step inside) => to step inside a function such that enter will work like showing us the next line executing.
# WE CAN USE print() method in pdb console.
# WE CAL KNOW DATA TYPE of variables in pdb console by using 'whatis'