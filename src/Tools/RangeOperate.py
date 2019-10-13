def eachIp(functions):
    result=''
    for index in range(len(ips)):
        result+=functions(index)
        result+='\n'
    return result
def eachIpArgs(functions,args):
    result=''
    for index in range(len(ips)):
        result+=functions(index,args)
        result+='\n'
    return result