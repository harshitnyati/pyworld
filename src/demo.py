from src.utils import gnum

def lotteryresult(num):
    result = gnum()
    print("generated number is : " , num)
    if result == num:
        return "You Won!"
    else:
        return "You Lost!"
