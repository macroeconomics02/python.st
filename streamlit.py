import streamlit as st

st.markdown(
    """
    <h1 style='text-align: center;'>전력시장 분석</h1>
    <h3 style='text-align: right;'>학번: C182021 이름: 송봉근</h3>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '''
    ### 전력시장 구조
    ##### 3가지 주체
    1. 발전사업자
    2. 한국전력공사(KEPCO)
    3. 전력소비자
    '''
)
st.divider()
st.markdown(
    '''
    #### :blue[**발전 사업자**]
    전기를 생산하여 전력시장에 판매, 민간과 공기업 발전소가 존재
    - **민간 발전소** 
        - 포스코에터지, GS파워, SK E&S, 한화에너지
    - **공기업 발전소**
        - 한국수력원자력, 한국발전
    '''
)
st.markdown('''
    ###### **발전원별 발전량 비중**
    '''
)
st. image("https://www.kier.re.kr/resources/component/daumeditor-7.5.9/images/upload/1721296245871.png")
col1, col2, col3, col4 =st.columns(4)
col1.metric("**석탄**", "30%")
col2.metric("**원자력**", '28%')
col3.metric("**LNG**", '10%')
col4.metric("**그 외**", '28%')
st.divider()
st.markdown(
    '''
    #### :blue[**한국전력공사**]
    발전소에서 생산된된 전기는 전력거래소(KPX)를 통해 거래가 된 전기를 받아 소비자에게 공급 
    - **전력거래소(KPX)** 
        - 실시간 수요에 맞게 입찰 가격과 수급 계획을 기준으로 발전소 선정
        - 시장의 수요 곡선과 발전소가 전력 한단위를 생산하는데 드는 한계계통가격(SMP)가 만나는 점에서 가격이 결정된다.
        - 입찰가격 선정에 대한 자세한 내용 👉[KPX](https://www.kpx.or.kr/menu.es?mid=a10401010000)'''
)

import pandas as pd

chart_data = pd.DataFrame({
    'y': [10, 20, 30, 40, 50],
    '수요(Qd)' : [25, 20, 15, 10, 5],
    '공급(SMP)': [5, 10, 15, 20, 25]
})
st.line_chart(chart_data.rename(columns={'y': 'index'}).set_index('index'))
st.latex('Qd(p)=ax-bp')
st.latex('Qs(p)=c+dp')
st.markdown(
    '''
    - **한국전력공사** 
        - 시장에서 결정된 가격을 가지고 일정한 제도 하에서 소비자들에게 판매
        - 전국 유일의 송전·배전망 운영자
            - 송전선과 배전선을 관리하며 발전소의 전기를 소비자에게 공급하는 중간역할을 수행
        - 한전의 역할이 궁금하다면 ⚡[한전](https://home.kepco.co.kr/kepco/main.do)
        '''
)
st.divider()
st.markdown(
    '''
    #### :blue[**전력소비자**]
    주택용,	일반용,	교육용,	산업용,	농사용,	가로등,	심야로 구분되어 공급
    사용 용도에 따라 전기 가격이 다르다. 농업용 전기 가격의 경우 가장 낮고 전기가 많이 사용되지 않는 시간대에는 가격이 저렴
    일반용의 경우 전기를 많이 사용할 수록 누진세가 적용되어 가격이 올라감감
    - **전기요금 구조**
    1. 기본요금: 기본적으로 부과되는 요금
    2. 전력량요금: 사용한 전력량에 따라 부과되는 요금
    3. 기후환경요금: 깨끗하고 안전한 에너지 제공에 소요되는 비용
    4. 연료비 조정요금: 연료비의 변동분을 요금에 일부분 반영'''
)
st.image('https://github.com/macroeconomics02/python.st/blob/main/%EC%A0%84%EB%A0%A5%EC%9A%94%EA%B8%88.png')
st.divider()

st.info('이 정보는 생각해야할 중요한 문제입니다!', icon="⭐")

yt_url = yt_url = 'https://www.youtube.com/watch?v=jUIwjLCpDtI'
st.video(yt_url)
'''
### :orange[**전력시장의 문제점**]
1. 수입해오는 연료비의 변동이 시장가격에 반영이 되지않아 한전의 적자 누적
2. 민간의 전력시장 참여가 제한
3. 늘어나는 전력 수요에 대한 안정적 공급망 필요
'''
st.divider()

st.success('문제점을 어떻게 해결할지에 대한 논의입니다!',icon="🔑")
'''
### :blue[**여러 가지 해결방안**]
1. 전기 시장 자유화
    - 우리나라는 전력생산을 위한 원료를 대부분 수입해오기 때문에 원유가격의 변동에 따른 전기가격 변동성에 대해 고려할 필요 있음
    - 영국의 경우 전기시장을 정부 주도에서 시장 자유화가 실시되고 전기가격이 높아지는 부작용
2. 정부의 가격 상한제
    - 한전의 역할은 송전·배전망 관리만 하고 나머지 전기 생산 및 공급 역할은 시장 자유화
    - 전기 가격에 대해 상한제를 실시하여 일정부분 이상 상승하는 것을 방지
'''
