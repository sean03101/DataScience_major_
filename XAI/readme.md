# Border emphasis LIME

### 연구 배경
![image](https://github.com/sean03101/DataScience_major_/assets/59594037/84626bd0-7326-49ba-9704-ff65b636d595)


LIME(Local Interpretable Model-agnostic Explanations) 
  - 블랙박스 모델의 예측에 대해 해석 가능한 모델로 지역적으로 근사 시킴으로써 블랙박스 모델을 설명
  - 개별 데이터 객체에 대한 블랙박스 모델의 예측을 설명하기 위하여 local surrogate model을 학습
  - 다음과 같은 절차를 통해 관심개체에 대한 블랙박스 모델의 예측을 설명
      1) 블랙박스 모델의 예측에 대해 설명하고자 하는 데이터 객체를 선택한다.
      2) 관심개체 주위로 데이터셋을 교란(perturb)시켜 새로운 데이터 샘플들을 생성하고 블랙박스 모델의 예측 값을 얻는다.
      3) 관심개체와 생성된 샘플 간의 거리와 Exponential smoothing kernel을 통해 생성된 각 샘플에 대한 가중치를 설정한다
      4) Weighted, interpretable model을 학습한다.
      5) Local model을 해석함으로써 관심개체에 대한 예측을 설명한다.

<br>
  - 장점
    1) 블랙박스 모델에 관계 없이 모델을 설명할 수 있다. (Local model agnostic)
    2) 테이블, 텍스트, 이미지 데이터 모두에서 사용 가능하다.
  - 단점
    1) Hyperparameter 대한 민감성 : LIME에서 설정하는 hyperparameter에 따라 설명의 결과가 완전히 다를 수 있다.
    2) 데이터 생성의 랜덤성 : 무작위로 교란(perturb)을 통해 생성된 샘플로 학습된 local surrogate model은 블랙 박스 모델을 충분히 근사하지 않을 수 있다.
    3) 불안정성 : 동일한 데이터 객체에 대해서도 매번 서로 다른 설명을 도출할 수 있다. 



### 연구 방법론 : Border emphasis LIME

![image](https://github.com/sean03101/DataScience_major_/assets/59594037/ed662a34-fbbf-4014-8c9b-b616f5f46260)

- Classification black box model에 적용가능한 Local surrogate method




