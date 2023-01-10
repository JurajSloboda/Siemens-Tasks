#!/usr/bin/env python3

def fool(items):
    result = []
    for i in range(len(items)):

        flag = False
        for j in range(len(result)):

            if items[i] == result[j]:
                flag = True
                break

        if not flag:
            result.append(items[i])

    return result

items = [1,1,2,4,5,3,1,2,1]
print(items)
print(fool(items))