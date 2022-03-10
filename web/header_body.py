# -- coding: utf-8 --

class header_body:

    def header(self):
        self.header = {
            'Host': '172.29.19.92:8989',
            'Connection': 'keep-alive',
            'Content-Length': 39,
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 98.0.4758.102 Safari / 537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://172.29.19.92:8989',
            'Referer': 'http://172.29.19.92:8989/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cookie': 'spauthn=3485b0bacc9223344d98d13912d99ab6126be823'
        }
        return self.header


    def bodylogindata(self):
        self.bodydata = {
            'password': 'admin',
            'username': 'admin'
        }
        return self.bodydata

