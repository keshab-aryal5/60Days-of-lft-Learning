class MyException(Exception):
    '''Message to be delivered for my own created exception
    Attributes:
        message -- explanation fo the error
    '''
    
    def __init__(self,message="Amount cann't be a negative number."):
        self.message = message
        super().__init__(message)

if __name__ == '__main__':
    try:
        amount = int(input("Enter the amount contributed: "))
        if amount < 0:
            raise MyException("Money cann't be a negative number bro.")
    except MyException as e:
        print(e)
        exit(1)
      