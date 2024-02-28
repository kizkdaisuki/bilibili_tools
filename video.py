from bilibili_api import video
from bilibili_api import Credential
from bilibili_api import sync, comment
from bilibili_api.comment import  CommentResourceType
import json_op
class Video:

    def __init__(self, credential: Credential, video_id: str):
        self.my_credential = credential
        self.my_video_id = video_id


    def method_start(self):
        lv_video = video.Video(credential=self.my_credential, bvid=self.my_video_id)
        lv_info = sync(lv_video.get_info())
        json_op.func_write_to_json(jsonfile_name='./video01.json', json_dict=lv_info)
        lv_av = lv_info['aid']
        page = 1
        cnt = 0
        comments = []
        while True:
            lv_comment = sync(comment.get_comments(oid=lv_av, type_=CommentResourceType.VIDEO, page_index=page, credential=self.my_credential))
            comments += lv_comment['replies']
            page += 1
            cnt += lv_comment['page']['size']
            if cnt >= lv_comment['page']['count']:
                break
        msg = ''
        for val in comments:
            msg += f'{val["member"]["uname"]} : {val["content"]["message"]}\n'
        json_op.func_write_to_file(file_name='./all_comments.txt', msg=msg)







