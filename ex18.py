def print_two(*args):
    arg1, arg2, = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")
    
#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
#This one takes no arguements
def print_none():
    print("I aint got nuthin.")
    

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()