# 1 объединение словарей
dict1
dict2
# old:
dict3 = {**dict1, **dict2}
# new:
dict3 = dict1 | dict2


# 2 new http status
import http 
print(http.HTTPStatus.OK)
print(http.HTTPStatus.FORBIDDEN)


# удаление префиксов и суффиксов
s = '"wdfsdf"'
s.removeprefix('"').removesuffix('"')




