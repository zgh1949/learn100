import module1 as m1 # 导入时会执行那个模块的代码
import module2 as m2 # 模块的代码放入__name__ == "__main__"，当前模块名称和导入的模块名称不符合，就不执行了

m1.foo()
m2.foo()

print("当前模块名称是",__name__)
print("模块1的模块名称",m1.__name__)
print("模块2的模块名称",m2.__name__)
print("于是就不会执行模块2的执行代码：print(\"Other code in module2\")")