def add_before_ui_after_ui(func):
    def Prasha():
        print("Bfore")
        func()
        print("After")
    return Prasha()
@add_before_ui_after_ui
def test_ui():
    print("I will")