def my_function():
    print("Hello from a function")

my_function()


def my_fun(fname):
    print("my name is " +fname)

my_fun("tomal")

def my_fun(fname,lname):
    print( fname + "" +lname )
    
my_fun("tomal","khan")
my_fun("jamal","kamal")



def my_fun(*kids):
    print("the child is " + kids[1])
my_fun("komol","kolim")


def my_fun(*lov):
    print("my name is " +lov[0])
    print("my age is " +lov[1])
    print(" i loves " +lov[2])



my_fun("tomal","34","birds")




def my_fun(country="bangladesh"):
    print("iam from " +country)
my_fun("austolia")
my_fun("usa")
my_fun()