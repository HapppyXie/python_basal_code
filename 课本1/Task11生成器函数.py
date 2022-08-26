# Athour:Mr Xie
# 开发时间:2022/5/4 14:27
'''
1.包含yield语句的函数：生成器对象，生成器函数
2.yield与return作用相似，都用来从函数中返回值
3.return语句一旦执行会立刻结束函数的运行返回值；
  yield语句一旦执行返回一个值并暂停或挂起后面的代码的执行，
    通过生成器对象的__next()__,内置函数next(),
    for循环遍历生成器对象元素或其他方式显示索要数据时恢复执行

4.生成器具有惰性求值的特点，适合大数据处理。
'''

def f():
    a,b=1,1
    while True:
        yield a
        a,b=b,a+b
a=f()
for i in range(10):
    print(next(a),end=' ')