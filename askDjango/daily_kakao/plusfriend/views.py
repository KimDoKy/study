from os.path import basename
import requests
from django.core.files import File
from .decorators import bot
from .models import Post

@bot
def on_init(request):
    return {'type': 'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']  # text, photo, audio(m4a), video(mp4)
    content = request.JSON['content'] # photo 타입일 경우에는 이미지 URL

    if type == 'photo':
        img_url = content
        img_name = basename(img_url)
        res = requests.get(img_url, stream=True)
        post = Post(user=request.user)
        post.photo.save(img_name, File(res.raw))
        post.save()
        response = '사진을 저장했습니다.'
    else:
        post = Post.objects.create(user=request.user, message = content)
        response = '포스팅을 저장했습니다.'


    return {
        'message': {
            'text': response,
        }
    }

@bot
def on_added(request):
    user_key = request.JSON['user_key']

@bot
def on_block(request, user_key):
    pass

@bot
def on_leave(request, user_key):
    pass
