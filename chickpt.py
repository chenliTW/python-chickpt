import requests
import urllib.parse

class chickpt:

    login_key=""
    m_id=""
    device_id="FA73X1702285"

    def __init__(self,login_key="",m_id=""):
        self.login_key=login_key
        self.m_id=m_id

    def sms_login(self,phone_num: str):
        requests.post("https://www.chickpt.com.tw/api/v2/mobile_login_verify?mobile={}&user_mode=1".format(phone_num))
        code=input("please input verification code:")
        res=requests.post("https://www.chickpt.com.tw/api/v2/mobile_login?mobile={}&user_mode=1&verify_code={}&device_id={}".format(phone_num,code,self.device_id)).json()
        self.login_key=res["data"][0]["login_key"]
        self.m_id=res["data"][0]["m_id"]
        print("your login key is:{}".format(self.login_key))
        print("your m_id is:{}".format(self.m_id))

    def search_case(self,keyword: str):
        data=[]
        res=requests.get("https://www.chickpt.com.tw/api/v2/cases?keyword={}".format(keyword)).json()
        data+=res["data"]
        total_page=res["meta"]["pagination"]["total_pages"]
        for page in range(1,total_page+1):
            res=requests.get("https://www.chickpt.com.tw/api/v2/cases?keyword={}&page={}".format(keyword,str(page))).json()
            data+=res["data"]
        return data

    def get_resume(self,job_id: str):
        resume=requests.get("https://www.chickpt.com.tw/api/v2/resume?device_id={}&from=1&&job_id={}&login_key={}&m_id={}&user_mode=1".format(self.device_id,job_id,self.login_key,self.m_id)).json()
        return resume

    def apply_case(self,job_id: str,bio: str,questions=["","",""]):
        bio=urllib.parse.quote_plus(bio)
        for i in range(len(questions)):
            questions[i]=urllib.parse.quote_plus(questions[i])
        res=requests.post("https://www.chickpt.com.tw/api/v2/apply?device_id={}&job_id={}&content={}&question_1={}&question_2={}&question_3={}&login_key={}&m_id={}&user_mode=1&from=1".format(self.device_id,job_id,bio,questions[0],questions[1],questions[2],self.login_key,self.m_id)).json()
        return res


