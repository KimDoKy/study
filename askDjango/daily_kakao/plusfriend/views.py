from .decorators import bot

@bot
def on_init(request):
    return {'type': 'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']
    response = '아직 구현 전입니다.'
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
