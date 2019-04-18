def do_a_bunch_of_work():
    print("Doing a bunch of work!")


def add_it_up(a, b):
    return a + b


def split_it_up(words):
    for word in words.split(' '):
        print(word)


do_a_bunch_of_work()
do_a_bunch_of_work()
do_a_bunch_of_work()
do_a_bunch_of_work()

result = add_it_up(25, 17)
print(result)

split_it_up("This is a multi-line statement.")
