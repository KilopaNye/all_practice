import json
import urllib.request as request
import bs4

src = "https://m.youtube.com/"

# # 建立一個request物件
# filesrc=request.Request(src, headers={
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
# })
# with request.urlopen(filesrc) as response:
#     data=response.read().decode("utf-8")

# # # 解析原始碼，取得文章標題。丟進BS4
# roots=bs4.BeautifulSoup(data, "html.parser")
# titles=roots.find_all("span", class_="yt-core-attributed-string")
# print(titles)
# for title in titles:
#     print(title.string)


def loops(url):
    # 建立一個request物件
    requests = request.Request(url,headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})
    with request.urlopen(requests) as response:
        data = response.read().decode("utf-8")
    # 解析原始碼，取得文章標題。
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("h3", class_="xw0")
    num=1
    with open("app.txt", mode="a", encoding="utf-8") as file:
        for title in titles:
            print(num, ".", title.a.string, "\n", file=file)
            num += 1
    nextLink = root.find("a", string="下一頁")
    return(nextLink["href"])
abs=0
url = "https://5278.cc/forum-23-1.html"
while abs<3:
    url="https://5278.cc/"+loops(url)
    abs+=1



# class File():
#     def __init__(self, name):
#         self.name=name
#         self.file=None  #尚未打開檔案 初期為None
#     def open(self):
#         self.file=open(self.name, mode="r", encoding="utf-8")
#     def read(self):
#         return self.file.read()

# data1=File("app.txt")
# data1.open()
# data=data1.read()
# print(data)


# class Point():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# p1=Point(5,6)
# print(p1.x,p1.y)


# class IO:
#     arc=["internet","IOPAP"]
#     def read(src):
#         if src not in IO.arc:
#             print("不支援")
#         else:
#             print("Read From" ,src)

# IO.read("IOPAP")


# import urllib.request as request
# src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
# with request.urlopen(src) as response:
#     data = json.load(response)
#     slist = data["result"]["results"]
# with open("app.txt", mode="w", encoding="utf8") as file:
#     for company in slist:
#         file.write(company["公司名稱"]+"\n")


# 檔案讀取與寫入練習
# sum=0
# with open("app.txt",mode="r",encoding="utf8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

# with open("app.json",mode="r") as file:
#     data=json.load(file)
# print("name :",data["name"])

# data["name"]="New name"
# with open("app.json",mode="w") as file:
#     json.dump(data, file)


# 亂數模組練習
# aka=random.sample([0,1,5,8],2)
# print(aka)

# random.shuffle(aka)
# print(aka)