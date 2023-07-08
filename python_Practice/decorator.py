
def decoratorItems(nums):
    def decorator(cb):
        def run():
            result = 0
            for i in range(nums+1):
                result+=i
            cb(result)
        return run
    return decorator


@decoratorItems(5)
def write(n):
    print("這邊用中文顯示", n)


@decoratorItems(5)
def writeEng(n):
    print("There use English write", n)


writeEng()