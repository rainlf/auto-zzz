"""
@author rain
@date 8/10/2024 7:34 AM
"""

import yaml


def test1():
    with open('test.yaml', 'r') as f:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
        for key in data:
            print(key, ':', data[key])


def test2():
    with open('test2.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
        for stage in data:
            print(stage, ':', data[stage])


if __name__ == '__main__':
    test1()
    test2()
