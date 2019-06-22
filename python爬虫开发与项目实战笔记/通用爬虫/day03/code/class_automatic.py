import requests,sys,json

class Automatic():
    def __init__(self,translade_word):
        self.translade_word = translade_word
        self.langdetect_headers ={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"}
        self.langdetect_parpams = {"query": translade_word}
        self.langdetect_url ="http://fanyi.baidu.com/langdetect"
        self.translated_url = "http://fanyi.baidu.com/basetrans"

    def langdetect(self):
        response = requests.post(self.langdetect_url,headers = self.langdetect_headers,data=self.langdetect_parpams)
        return json.loads(response.content.decode())['lan']

    def get_data_language(self,language_word):
        #
        # if "zh" ==language_word:
        #     translade_data ={"query":self.translade_word,
        #                         "from":"zh",
        #                         "to":"en"}
        # else:
        #     translade_data = {"query": self.translade_word,
        #                       "from": language_word,
        #                       "to": "zh"}
        return {"query":self.translade_word,"from":"zh","to":"en"} if "zh" ==language_word \
                else {"query": self.translade_word,"from": language_word,"to": "zh"}

    def translade(self,translade_data):
        response = requests.post(self.translated_url,data=translade_data,headers = self.langdetect_headers)
        response_data = json.loads(response.text)
        # print("1111111111",response_data)
        return response_data

    def get_ret(self,response_data):
        data = response_data["trans"][0]["dst"]
        print("{}  翻译后的结果：{}".format(self.translade_word, data))



    def run(self):
        language_word = self.langdetect()
        translade_data= self.get_data_language(language_word)
        response_data = self.translade(translade_data)
        self.get_ret(response_data)

if __name__ == '__main__':
    translade_word = sys.argv[1]
    automatic = Automatic(translade_word)
    automatic.run()