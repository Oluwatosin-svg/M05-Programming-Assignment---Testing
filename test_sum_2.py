def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")

#The output displayed an error. This is because there is another
#assertion to test with tuple but the numbers in it doesn't 
#correlate with the numbers without the test that isn't tupel#