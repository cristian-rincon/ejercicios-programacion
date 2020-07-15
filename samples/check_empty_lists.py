

def test_method(columns=[]):

    if len(columns) == 0:
        print("Lista vacía")
    else:
        for item in columns:
            print(item)


if __name__ == "__main__":
    test_method()
