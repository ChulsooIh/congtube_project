Django 기반 콩튜브 프로젝트
1. 콩튜브를 기반으로 기능 추가 및 구현
2. 기능 정의
    - 조회수가 있었으면 좋겠다
        * 조회수 기반으로 Best 목록을 만들 수 있다
    - 로그인, 검색기능 추가
        - 검색기능은 이름 기반으로
    - 메인화면(리스트)랑 상세 페이지
    - 리뷰를 추가
    - 메인화면에 조회수, 인기순, 알파벳순 순서를 바꿔서 보여주기
    - 구독 기능
3. 디비 모델링
    유투버 모델         YouTuberModel
        유투버 ID         id                = int
        이름            name            = String    
        프로필 사진     profile_img        = URL
        영상 URL         vodio_url        = URL
        자기소개        description        = String
        조회수         views            = int
        생성날짜         create_date     = DateTime
    
    유투버 카테고리 모델 YouTuberCategoryModel
        유투버 ID     youtuber_id        = int
        카테고리 ID    category_id        = int
        등록날짜        register_date    = DateTime
    구독자 모델         SubscriberModel
        사용자 ID        user_id            = int
        유투버 ID        youtuber_id        = int
        등록날짜        register_date   = DateTime
    리뷰 모델             ReviewModel
        리뷰 ID        id                = int
        사용자 ID        user_id            = int
        리뷰 텍스트    review_text        = String
        등록날짜        register_date    = DateTime
        삭제 유무        delete_yn        = String
    카테고리 모델         CategoryModel
        카테고리 ID    id                = int
        카테고리 이름    category_name    = String
        등록날짜        register_date   = DateTime
4. 화면 생성
    - 메인 화면
        /home?q=검색어
            회원가입, 로그인 기능이 있어야 한다
            검색창이 나온다
            카테고리가 나온다
            유투버에 프로필 사진과 이름 리스트가 나온다
    - 상세 화면
        /detail/<int:pk>
            검색창
            영상화면
            이름
            카테고리
            자기 소개글
            조회수, 구독자 수, 구독자 버튼
            리뷰
            추천 유투버 4명 가져오기
5. 기술 조사
    - 로그인, 회원가입 기능
    - URL 다음 q파라미터를 어떻게 받아서 뷰에 넘길 것인지?
