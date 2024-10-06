import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time take by function{end_time- start_time }")
    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, rime taken by this function")
    time.sleep(2)

@time_decorator
def test_ui_2():
    print("Add a function")
    time.sleep(5)

# test_ui_1()
