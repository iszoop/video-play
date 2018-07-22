from django.shortcuts import render
from django.views.generic.base import View

from .models import Video
# Create your views here.
class VideoPlayView(View):
    """
    视频播放页面
    """
    def get(self,request,video_id):
        video = Video.objects.get(id=int(video_id))
        return render(request,'video-palyer.html',{
            'video':video,
        })