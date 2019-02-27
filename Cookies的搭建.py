# 存储模块
import random
import redis


class RedisClient(object):
    def __init__(self, type, website, host='localhost', port=6379, password=''):
        self.db = redis.StrictRedis(host='localhost', port=6379, password='', decode_responses=True)
        self.type = type
        self.website = website

    def name(self):
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        return self.db.hget(self.name(), username)

    def delete(self, username):
        return self.db.hdel(self.name(), username)

    def count(self):
        return self.db.hlen(self.name())

    def random(self):
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        return self.db.hkeys(self.name())

    def all(self):
        return self.db.hgetall(self.name())

    # 存储模块
    for username in accounts_usernames:
        if not username in cookies_usernames:
            password = self.acconts_db.get(username)
            print('正在生成cookies', '账号', username, '密码', password)
            result = self.new_cookies(username, password)

    def get_cookies(self):
        return self.browser.get_cookies()

    def main(self):
        self.open()
        if self.password_error():
            return {
                       'status': 1,
                       'content', '用户名或密码错误'
            }
        #获取验证码图片
        image=self.get_image('captcha.png')
        numbers=self.detect_image(image)
        self.move(numbers)
        # 如果不需要验证码直接登录
        if self.login_successfully():
            cookies = self.get_cookies()
            return {
                'status': 1,
                'content': cookies
            }
        else:
            return {
                'status':3,
                'content':'登录失败'
            }


