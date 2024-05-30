# cathaybk_assignment02

## 問題描述
這是一個Python程式,用於根據學生輸入的數字去做驗證答案，看輸入的數字應該會組成像 ”偶數升冪排序”，”奇數降冪排序”。
例如 ‘417324689435’ 將會變成 ‘975331244468’。

## 解決方案
底下針對問題，思考脈絡如下:

1. 0 定義成偶數
2. 無長度限制，可能自己定義 小學生輸入的數字長度介於 0 ~ 20，方便測試邊界值
3. 輸入非數字，要做exception
4. input : str (萬一有小學生輸入一開始為 000566787)
5. output: bool (True or False)

### 相關考慮條件1: 定義邊界條件（若要不設限邊界，則可以修改限制變數）

- 0 定義成偶數
- 無長度限制，可能自己定義 小學生輸入的數字長度介於 0 ~ 20，方便測試邊界值

### 相關考慮條件2: 異常處理

- 如果輸入非數字，要做exception,程式會拋出 `InvalidInputException` 異常。

### 實作細節

1. final result = odd_str + even_str
2. odd_str = odd_list 先sort（revers=True） 再join()
3. even_str = even_list 先sort 再join()

### 執行環境

- Python 版本: 3.9.6
- 需要安裝的套件: `pytest`(用於單元測試) （教學：https://docs.pytest.org/en/latest/getting-started.html）

### 使用方式

1. clone git repo: git clone https://github.com/ch806290/cathaybk_assignment02.git
2. 到專案目錄: cd cathaybk_assignment02
3. 執行程式: python3 cathaybk_002.py

### pytest 單元測試

1. 到專案目錄: cd cathaybk_assignment02
2. 執行單元測試:python3 -m pytest test_cathaybk_002.py
