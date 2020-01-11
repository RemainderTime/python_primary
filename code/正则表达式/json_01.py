import json

json_str = '{"name":"xf","age":17}'

#反序列化 josn -> dict
student = json.loads(json_str)
#类型为字典  dict
print(type(student))
print(student)

#JSON 对象 ,JOSN,JSON字符串
