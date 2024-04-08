from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post , Like , Comment
from .serializer import PostSerializer, LikeSerializer, CommentSerializer




@api_view(['GET'])
def get_likes_for_post(request, post_id):
    likes = Like.objects.filter(post_id=post_id)
    likes_data = []
    for like in likes:
        like_data = {
            'id': like.id,
            'post_id': like.post_id,
            'post_title': like.post.title,  
        }
        likes_data.append(like_data)
    return Response({'likes': likes_data})


@api_view(['GET'])
def get_post_details(request):
    posts = Post.objects.all()
    response_data = []
    for post in posts:
        comments = Comment.objects.filter(post=post)
        comment_data = []
        for comment in comments:
            comment_data.append({
                "text": comment.text,
           
            })
        post_data = {
            "post_name": post.title,
            "comments": comment_data,
        }
        response_data.append(post_data)
    return Response(response_data)


