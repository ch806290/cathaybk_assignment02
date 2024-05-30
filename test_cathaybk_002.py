import pytest
from cathaybk_002 import solution,InvalidInputException

class TestPractice011:

    @pytest.mark.RAT
    def test_practice011_RAT(self):
        s = solution()
        result = s.verify_math_rule('9755524666')
        assert result is True


    @pytest.mark.FAST
    def test_practice011_Boundary(self):
        s = solution()
        result = s.verify_math_rule('11111111111111111111')
        assert result is True

    @pytest.mark.parametrize("str1, expected_exception",[
        ("-22", InvalidInputException("輸入的內容摻雜了非數字文字，請學生再檢查一次！")),
        ("12243!!", InvalidInputException("輸入的內容摻雜了非數字文字，請學生再檢查一次！")),
        ("9999999999999999999911", InvalidInputException("輸入的內容長度應該介於1~20，請學生再檢查一次！"))
    ])
    @pytest.mark.FET
    def test_practice011_Exception(self,str1,expected_exception):
        s = solution()
        with pytest.raises(InvalidInputException) as exec_output:
            s.verify_math_rule(str1)
        
        assert str(exec_output.value) == str(expected_exception)
            