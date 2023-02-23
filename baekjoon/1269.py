a, b= map(int,input().split())
a_set = set(list(map(int,input().split())))
b_set = set(list(map(int,input().split())))
print(len(b_set|a_set) - len(b_set&a_set))