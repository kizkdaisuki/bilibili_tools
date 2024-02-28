
from bilibili_api import Credential
from video import Video
def func_main():
    sessdata = 'ff28cae6%2C1724342981%2C43cec%2A22CjAkgVOOGLy6HTOgfPQvATuH7YJyiAouyP18ZD9-aVjA4dLd4thM08Wu7HVzcmURe7ASVl9jby1HUHZFdkE2X3dOVXZLc0NFWm50ZWk2d2RZMHlFVU1HSC16ZEh0bXdYV2lQTHpzY1hUYnJJWVpnRk9yN0NJVEQ1dm5uLW9pU0Fua0ZUclNqb3V3IIEC'
    bili_jct = '395931c8785024f8f87f4e061065160'
    buvid3 = '3F39D15E-7969-B76F-67A7-3D114C9FEA2409006infoc'
    credential = Credential(sessdata=sessdata, bili_jct=bili_jct, buvid3=buvid3)
    video = Video(credential=credential, video_id='BV1Yj421X7XW')
    video.method_start()


if __name__ == '__main__':
    func_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
