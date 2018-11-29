#!/usr/bin/env python3

"""planets.py: Description of what planets does.

__author__ = "Lian Feiyue"
__pkuid__  = "1800011733"
__email__  = "1800011733@pku.edu.cn"
"""

from urllib.request import urlopen


def get_the_exchange(jstr):
    """将从网站上得到的字符串在双引号处切开，返回所兑换货币及数量的字符串
    """
    jstrsp = jstr.split('"')
    return jstrsp[7]


def get_the_number(s):
    """将所兑换货币及数量的字符串在空格处切开，第一部分为数量，返回之
    如果该字符串为空，返回货币输入有误
    """
    exc = get_the_exchange(s)
    num = exc.split(" ")
    if exc is "":
        return "currency invalid"
    else:
        return num[0]


def exchange(currency_from, currency_to, amount_from):
    """先判断amount_from是否为数值，如不是返回数量输入有误
    将货币输入大写，避免因小写而错误
    再从网站上得到字符串并解码
    最后将函数"get_the_number(jstr)的值返回即得兑换数量
    """
    try:
        amountfl = float(amount_from)
    except ValueError:
        return "amount_from invalid"
    else:
        a = str(currency_from).upper()
        b = str(currency_to).upper()
        s = 'from={}&to={}&amt={}'.format(a, b, amountfl)
        doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?'+s)
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('ascii')
        return get_the_number(jstr)


def test_get_the_exchange():
    """测试get_the_exchange(jstr)函数
    """
    assert("4.7496295 Euros" == get_the_exchange('''{ "from" : "5.5 United States Dollars",
"to" : "4.7496295 Euros", "success" : true, "error" : "" }'''))
    assert("17.13025 Chinese Yuan" == get_the_exchange('''{ "from" : "2.5 United States Dollars",
"to" : "17.13025 Chinese Yuan", "success" : true, "error" : "" }'''))


def test_get_the_number():
    """测试get_the_number(s)函数
    """
    assert("17.13025" == (get_the_exchange('''{ "from" : "2.5 United States Dollars","to" : 
"17.13025 Chinese Yuan","success" : true, "error" : "" }''').split(" "))[0])
    assert("" == (get_the_exchange('''{ "from" : "", "to" : "", "success" : 
false, "error" : "Exchange currency code is invalid." }''').split(" "))[0])


def test_all():
    """测试所有函数
    """
    test_get_the_exchange()
    test_get_the_number()
    print("All tests passed")


def main():
    """先测试函数和进行输出测试
    然后可以输入兑换多少数值的某种货币
    输出能兑换另一种货币多少数值
    """
    test_all()
    print(exchange("USD", "EUR", 5.5))
    print(exchange("CNY", "usd", 8))
    print(exchange("USD", "xxx", 1))
    print(exchange("xxx", "USD", 1))
    print(exchange("CNY", "usd", "A"))
    get_from = input("please enter the currency to be changed：")
    get_to = input("please enter the currency to get：")
    amount = input("please enter the amount of the currency：")
    print("you can get:" + exchange(get_from, get_to, amount))

    
if __name__ == "__main__":
    main()
