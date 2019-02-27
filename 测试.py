from PIL import Image
import os
## 调整照片大小
### path， 照片的路径
### factor，缩放的比例～
def resize(path, factor=0.9):
    img  = Image.open(path)
    out = img.resize(tuple(map(lambda x: int(x * factor), img.size)))
    # 保存文件，直接将原来的文件替换掉（有风险，建议备份源文件）
    with open(path, 'w') as f:
        out.save(f)
    return path

# 对的，我处理的就是获奖证书，放心吧都是很low be的奖 \\-_-
base_path = '../获奖证书/after/'
# 遍历这个文件夹，找到所有jpg文件，然后拿到文件路径（绝对路径）
files = [os.path.abspath(base_path + item) for item in os.listdir(base_path)
  if len(item.split('.')) == 2 and item.split('.')[1] == 'jpg']

# 执行～
list(map(resize, files))