class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름: {self.name}")
        print(f"아이디: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 회원 인스턴스 생성 및 members 리스트에 저장
members = []
members.append(Member("김철수", "kcs", "1234"))
members.append(Member("박지영", "pjy", "5678"))
members.append(Member("이영희", "lyh", "9012"))

# members 리스트의 회원 이름 출력
for member in members:
    member.display()

# 각 회원의 게시글 작성 및 posts 리스트에 저장
posts = []
for member in members:
    for i in range(3):
        posts.append(Post(f"{member.name}의 게시글 {i+1}", f"{member.name}의 게시글 내용 {i+1}", member.username))

# 특정 유저의 게시글 제목 출력
username = "pjy"
for post in posts:
    if post.author == username:
        print(f"제목: {post.title}")

# 특정 단어 포함 게시글 제목 출력
keyword = "안녕"
for post in posts:
    if keyword in post.content:
        print(f"제목: {post.title}")