from src.demo import lotteryresult
from unittest import mock

def test_rs():
    with mock.patch('src.demo.gnum', return_value=3):
        rs = lotteryresult(3)
    print( "result of lotteryresult function is " , rs)
    assert rs == "You Won!"


@mock.patch('src.demo.gnum', return_value=3)
def test_rs(mock_check_output):
    rs = lotteryresult(3)
    print( "result of lotteryresult function is " , rs)
    assert rs == "You Won!"