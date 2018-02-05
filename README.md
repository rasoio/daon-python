# Daon

## Installation

```python
pip install daon
```

## Usage

```python
from daon import Tagger
tagger = Tagger()

tagger.pos(u'네, 안녕하세요. 반갑습니다.')

# 추출 품사 지정
tagBit = tagger.makeTagBit(['N','SL','SH'])

tagger.pos(u'네, 안녕하세요. 반갑습니다.', includeBit=tagBit)

# 새로운 모델 적용 (모델 파일)
tagger = Tagger(model_path='/Users/mac/work/daon/daon-core/src/main/resources/daon/core/reader/model.dat')

# 새로운 모델 적용 (모델 url)
tagger = Tagger(url='http://localhost:5001/v1/model/download?seq=1514366867073')
```

[품사(tag) 정보](https://github.com/rasoio/daon/blob/master/daon-elasticsearch/README.md#%ED%92%88%EC%82%ACtag-%EC%A0%95%EB%B3%B4)

### 참고

[konlpy](https://github.com/konlpy/konlpy)

[konlpy py4j](https://github.com/nazgul33/konlpy)