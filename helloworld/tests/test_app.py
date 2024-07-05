from helloworld.app import greeting

def test_name():

    assert greeting("Alice") == "Hello, Alice"

def test_empty():

    assert greeting("") == "Hello, Stranger"

def test_brutus():

    assert greeting("Brutus") == "BeeWare, the IDE of Python"
