# coding=utf-8
import requests
import execjs

js = '''function a(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
    }
    function n(r) {
        var o = r.length;
        o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substr(-10, 10));
        var t = void 0
          , n = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        t = null !== C ? C : (C = window[n] || "") || "";
        for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {
            var m = r.charCodeAt(g);
            128 > m ? d[f++] = m : (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)),
            d[f++] = m >> 18 | 240,
            d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224,
            d[f++] = m >> 6 & 63 | 128),
            d[f++] = 63 & m | 128)
        }
        for (var S = h, u = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), l = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), s = 0; s < d.length; s++)
            S += d[s],
            S = a(S, u);
        return S = a(S, l),
        S ^= i,
        0 > S && (S = (2147483647 & S) + 2147483648),
        S %= 1e6,
        S.toString() + "." + (S ^ h)
    }
    var C = null;
    t.exports = n
}'''

# ctx = execjs.compile(js)
# ctx.call("n","你好啊")


headers = {
    # "Accept":"*/*",
    # "Accept-Encoding":"gzip, deflate",
    # "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6",
    # "Connection":"keep-alive",
    # "Content-Type":"application/x-www-form-urlencoded",
    # "Host":"fanyi.baidu.com",
    # "Origin":"http://fanyi.baidu.com",
    # "Referer":"http://fanyi.baidu.com/",
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
    # "X-Requested-With":"XMLHttpRequest",
    # "Cookie":"BAIDUID=B27C9ABD8A5079E6D8F42D0451E1CFA2:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1515338548; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BIDUPSID=B27C9ABD8A5079E6D8F42D0451E1CFA2; PSTM=1515339233; H_PS_PSSID=1437_24565_21117_17001; PSINO=6; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1515340680; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1515340680; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1515340680"
}

data = {"query":"你好啊",
        "from":"zh",
        "to":"en"}
r = requests.post("http://fanyi.baidu.com/basetrans",headers=headers,data=data)
print(r.content.decode())
