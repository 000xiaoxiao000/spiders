from urllib.robotparser import RobotFileParser

rp=RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.baidu.com/?tn=78000241_5_hao_pg'))
print(rp.can_fetch('*','https://www.jianshu.com/u/47c841215f33'))