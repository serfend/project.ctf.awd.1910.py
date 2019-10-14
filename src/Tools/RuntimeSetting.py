
class RuntimeSetting:
    dic={}
    def __init__(self):
        pass
    def set(self,k,v):
        dic[k]=v
    def get(self,k):
        return dic[k]
    def exist(self,k):
        return k in dic
    def clear(self):
        dic.clear()