from .decorators import bot
from .models import Post

@bot
def on_init(request):
    return {'type': 'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content'] # photo 타입일 경우에는 이미지 URL

    if type == 'photo':
        response = '사진 저장은 아직 지원하지 않습니다.'
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
