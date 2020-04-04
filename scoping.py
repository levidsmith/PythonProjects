global x
x = 42

def foo():
    x = 3
    print("foo x: " + str(x)) #x is local, 3

    y = "42"
    y = int(y) + 1
    print("foo y: " + str(y))

def bar():
    print("bar x: " + str(x)) #x is global, 42

def baz():
    global x
    x += 1
    print("baz x: " + str(x))
    
foo()
bar()
baz()

print("x: " + str(x))
