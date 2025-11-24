"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABC, abstractmethod
from enum import Enum


class Calculator:

    @abstractmethod
    def get_salary(self):
        pass


class ProjectManagerCalculator(Calculator):
    def get_salary(self):
        return 15000


class DeveloperCalculator(Calculator):
    def get_salary(self, work_hour):
        return work_hour * 150


class SalesCalculator(Calculator):
    def get_salary(self, sales_amount):
        return 1200 + sales_amount * 0.05


if __name__ == "__main__":
    calculator_dict = {
        "pm": ProjectManagerCalculator(),
        "coder": DeveloperCalculator(),
        "sales": SalesCalculator()
    }

    c = calculator_dict['pm']
    print(f"项目经理的工资是{c.get_salary()}")

    c = calculator_dict['coder']
    print(f"程序员的工资是{c.get_salary(240)}")

    c = calculator_dict['sales']
    print(f"销售的工资是{c.get_salary(200000):.0f}")

