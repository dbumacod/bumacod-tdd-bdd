def increment_by_one(i):
    return i + 1
 
def decrement_by_one(i):
    return i - 1
    
def test_increment_answer():
    assert increment_by_one(2) == 3
    
def test_decrement_answer():
    assert decrement_by_one(4) == 3