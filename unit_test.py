from Add import add

def testAddMethod():
    #valid test cases
    assert add(['1,2,3','4,5','6','7,8']) == 36
    assert add(['//%','1%2%3','9%0']) == 15
    assert add(['//[***]','1***2***3000***3']) == 6
    assert add(['//[%%][**]','1**3%%2**2','7**4%%3%%9'])==31
    print("all the valid test cases are passed successfully")


    #uncomment the below lines to see the exception raised when invalid delimiters are given
    '''
    #invalid test cases
    assert add(['1,2,3,','4,5','6','7,8']) == "invalid delimiter(s) found", "No need of extra delimiter at the last of one line"
    assert add(['//%','1%2%3','9%%0']) == "invalid delimiter(s) found", "Invalid delimiter is given, Length is larger than the original delimiter"
    assert add(['//[***]','1***2**3']) == "invalid delimiter(s) found", "Invalid delimiter is given, Length is smaller than the original delimiter"
    '''


    #uncomment the below lines to see the exception raised when negative values are given
    '''
    #valid test cases with negative values
    assert add(['1,2,-3','4,-5','6','7,8']) != 36
    assert add(['//%','1%2%3','-9%0']) != 15
    assert add(['//[***]','-1***-2***-3']) != 6
    assert add(['//[%%%][**]','-1**3%%2**2','7**-4%%3%-9'])!=31
    '''
