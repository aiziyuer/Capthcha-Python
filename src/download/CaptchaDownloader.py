#!/usr/bin/env python
# coding=utf-8
import bs4
import requests
import os


class CaptchaDownloader:
    """
    验证码相关的下载类
    """

    # 通过登录页获取到验证码的hash值
    def get_captcha_hash(self):
        # 模拟的http请求头
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.double.com',
            'Accept-Language': 'zh-CN',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)like Gecko',
            'Host': 'www.douban.com'
        }
        # 尝试获取登录页
        response = requests.get('https://www.douban.com/accounts/login', headers=headers)
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        return [a.attrs.get('src') for a in soup.select('#captcha_image')]
        pass

    # 保存验证码
    def save_captcha(self, hash_url, dir, file_name):
        if hash_url:
            r = requests.get(hash_url, stream=True)
            if r.status_code == 200:
                with open(os.path.join(dir, file_name), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

            pass  # end if hash_url
        pass  # end def save_captcha

    def batch_save_captcha(self, dir, count):
        for i in range(1, count):
            hash_arrays = download.get_captcha_hash()
            hash_url = None if len(hash_arrays) == 0 else hash_arrays[0]
            self.save_captcha(hash_url, dir, ("captcha-%d.png" % i))
        pass


if __name__ == '__main__':
    download = CaptchaDownloader()
    download.batch_save_captcha('../../data/00_original', 50)

    pass
