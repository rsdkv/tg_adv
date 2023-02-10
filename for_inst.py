import instaloader

L = instaloader.Instaloader()
user_name = 'login'
password = 'your_password'
'''
здесь вводятся данные для входа
с того аккаунта, с которого будут производиться
запросы(лучше иметь отдельный аккаунт, так как 
все равно имеется вероятность блокировки аккаунта,
с которого выполняются запросы, так как они 
автоматические)
'''
L.login(user_name, password)
target_user = 'user_name'     #вводится ник нужного аккаунта
profile = instaloader.Profile.from_username(L.context, target_user)
POSTS = profile.get_posts()
for post in POSTS:
    if post.is_video:
        L.download_post(post, target_user)

