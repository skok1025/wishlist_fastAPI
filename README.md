## chatGPT 를 활용하여 만든 wish list API 

### 구성
```
- DB : Redis
- language : Python
- Framework : FastAPI
- chatGPT Link : https://chat.openai.com/share/e5a0be87-3104-4ea9-aaab-0e70270397d2

- GPT 요청 프롬포트 :
파이썬 fastAPI 를 이용하여 아래 조건에 맞는 개발을 해줘. 
- 버킷리스트를 체크하는 용도의 api 를 개발하고자 함. 
- redis 를 데이터 보관용으로 사용하고 저장될 데이터는 아래와 같음. 
- zset 타입이며 key값은 "wishlist" member 값은 "{해야할일}||{체크여부}" score 는 현재 시간 (yyyyMMddHis)
ex) 여행가기||F , 20230610003310
- 해당 데이터를 가공하는 api 를 제작해줘.
```

### 실행 방법
```
# uvicorn main:app --reload
```

Spring 프레임워크로 api 를 만들다가 fastAPI 와 chatGPT 를 이용해서 API 를 만들어봤는데 
생각보다 잘 돌아가서 놀랐습니다.
참고로 해당 API 는 전적으로 GPT 가 만든것이고 저는 GPT 요청프롬포트에 요구사항만 넣었습니다. 

