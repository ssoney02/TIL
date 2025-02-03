# 아래 함수를 수정하시오.
def get_value_from_dict(my_dict, key):
    value = my_dict.get(key, 'unknown') # 일치하는 key가 없을경우, 기본값 생성해서 출력!!!!!!!!!!
    return value


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown