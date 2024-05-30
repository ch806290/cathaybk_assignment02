'''
Q: 
國泰國中的老師出了一道題目給同學們練習，
同學們自己設定一串奇偶混和地亂數，並將數字依照” 奇數都在偶數前面”，
且”偶數升冪排序”，”奇數降冪排序”。
例如 ‘417324689435’ 將會變成 ‘975331244468’。

然而，班上有50位學生，每一個同學給出的數字長度不一，
老師希望能用一段小程式來幫助他驗證答案，請你寫一個函數幫幫老師吧!

1. 0 定義成偶數
2. 無長度限制，可能自己定義 小學生輸入的數字長度介於 0 ~ 20，方便測試邊界值
3. 輸入非數字，要做exception
4. input : str (萬一有小學生輸入一開始為 000566787)
5. output: bool (True or False)

design
a. final result = odd_str + even_str
b. odd_str = odd_list 先sort（revers=True） 再join()
c. even_str = even_list 先sort 再join()


'''
import re


class InvalidInputException(Exception):
    pass

class solution:
    def verify_math_rule(self, str1:str) -> bool:
        tempList = list(str1)
        oddlist = []
        evenlist = []


        pattern = r'^[\d]+$'
        if not re.match(pattern, str1):
            raise InvalidInputException('輸入的內容摻雜了非數字文字，請學生再檢查一次！')


        for i in tempList:
            
            if int(i) % 2 == 0:
                evenlist.append(i)
            else:
                oddlist.append(i)

        oddlist.sort(reverse=True)
        evenlist.sort()


        result = "".join(oddlist) + "".join(evenlist)

        print("-------------------------------")
        print(f"str1 is {str1}")
        print(f"result is {result}")

        return (str1 == result)

def main():
    s = solution()
    print(s.verify_math_rule('9876543'))
    print(s.verify_math_rule('9731111'))
    print(s.verify_math_rule('0248888'))
    print(s.verify_math_rule('9731111068888'))
    print(s.verify_math_rule('975331244468'))

    print(s.verify_math_rule('111'))
    print(s.verify_math_rule('20004'))
    print(s.verify_math_rule('222'))

    print(s.verify_math_rule('-22'))


if __name__ =='__main__':
    main()
