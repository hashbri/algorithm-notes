#异常处理
try:
    #可能会出现异常的代码
except #错误类型  SyntaxError语法错误 TypeError类型错误 ValueError值错误 IndexError索引错误
    #处理逻辑
except Exception as e:#捕获所有继承自exception的异常，并获取异常对象e
    print("发生异常",e)