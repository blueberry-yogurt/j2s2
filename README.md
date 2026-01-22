# j2s2
웹 스크래핑
## ERD

![ERD](erd.png)

users : token_blacklist = 1 : N
- 한 명의 유저는 여러 개의 블랙리스트 토큰을 가질 수 있음

users : diaries = 1 : N
- 한 명의 유저는 여러 개의 다이어리를 가질 수 있음

users : bookmarks = 1 : N
- 한 명의 유저는 여러 개의 북마크를 가질 수 있음

quotes : bookmarks = 1 : N
- 하나의 명언은 여러 유저에게 북마크될 수 있음

users : user_questions = 1 : N
- 한 명의 유저는 여러 질문에 답변(선택)할 수 있음

questions : user_questions = 1 : N
- 하나의 질문은 여러 유저에게 갈 수 있음

users : questions = N : M
- user_questions 테이블을 통한 다대다 관계

(중간 테이블: user_questions)
