"""
PicCollage_Problem1.tests.test_problem1 contains the unit test cases for
the module PicCollage_Problem1.problem1.problem1.
"""


from PicCollage_Problem1.problem1.problem1 import contain_sevens


def test_contain_sevens():
    """
    test_contain_sevens exxecute tests for the function contain_sevens.
    """

    input_data = [7, 20, 70, 100]
    output = [1, 2, 8, 19]
    for i in range(len(input_data)):
        assert contain_sevens(input_data[i]) == output[i]
