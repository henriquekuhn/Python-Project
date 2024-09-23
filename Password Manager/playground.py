def uppercase_decorator(function):
    print("uppercase_decorator")
    print(function)
    def wrapper():
        print("wrapper")
        print(f"FUNCTION {function}")
        func = function()
        print(f"aqui {func}")
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    print("say hi")
    return 'hello there'

print("Inicio")
decorate = uppercase_decorator(say_hi)
print("decorate")
print(decorate)
fim = decorate()
print(fim)


play_dict = [
    {"likes: 10, comments: 1"},
    {"likes: 100, comments: 5"},
    {"likes: 100, comments: 8"},
    {"likes: 100, comments: 9"},
    {"likes: 99, comments: 4"}
    ]


print(play_dict["likes"])