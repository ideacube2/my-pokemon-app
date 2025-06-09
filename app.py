import streamlit as st

# 확장된 포켓몬 데이터
pokemon_data = {
    "피카츄": {
        "타입": "전기", "HP": 35, "공격": 55, "방어": 40, "스피드": 90,
        "특징": "전기를 몸에 저장하는 전기쥐 포켓몬", "이모지": "⚡"
    },
    "파이리": {
        "타입": "불꽃", "HP": 39, "공격": 52, "방어": 43, "스피드": 65,
        "특징": "꼬리 끝의 불꽃으로 기분을 표현", "이모지": "🔥"
    },
    "꼬부기": {
        "타입": "물", "HP": 44, "공격": 48, "방어": 65, "스피드": 43,
        "특징": "단단한 등껍질로 몸을 보호", "이모지": "💧"
    },
    "이상해씨": {
        "타입": "풀", "HP": 45, "공격": 49, "방어": 49, "스피드": 45,
        "특징": "등의 씨앗에서 에너지를 얻음", "이모지": "🌱"
    }
}

st.title("📚 나만의 포켓몬 도감")

# 메뉴 선택
menu = st.selectbox("메뉴를 선택하세요", ["포켓몬 정보 보기", "능력치 비교", "전체 도감"])

if menu == "포켓몬 정보 보기":
    selected = st.selectbox("포켓몬 선택", list(pokemon_data.keys()))
    pokemon = pokemon_data[selected]
    
    st.write(f"## {selected} {pokemon['이모지'] * 3}")
    st.write(f"**타입:** {pokemon['타입']}")
    st.write(f"**특징:** {pokemon['특징']}")
    
    # 능력치 표시
    st.write("### 능력치")
    for stat in ['HP', '공격', '방어', '스피드']:
        st.write(f"**{stat}:** {pokemon[stat]}")
        st.progress(pokemon[stat] / 100)

elif menu == "능력치 비교":
    col1, col2 = st.columns(2)
    
    with col1:
        p1 = st.selectbox("첫 번째 포켓몬", list(pokemon_data.keys()), key="compare1")
    with col2:
        p2 = st.selectbox("두 번째 포켓몬", list(pokemon_data.keys()), key="compare2")
    
    if st.button("비교하기"):
        st.write("### 비교 결과")
        for stat in ['HP', '공격', '방어', '스피드']:
            val1 = pokemon_data[p1][stat]
            val2 = pokemon_data[p2][stat]
            
            if val1 > val2:
                winner = p1
            elif val2 > val1:
                winner = p2
            else:
                winner = "무승부"
            
            st.write(f"**{stat}:** {p1}({val1}) vs {p2}({val2}) → {winner}")

elif menu == "전체 도감":
    st.write("### 🌟 등록된 모든 포켓몬")
    
    for name, data in pokemon_data.items():
        with st.expander(f"{data['이모지']} {name}"):
            st.write(f"타입: {data['타입']}")
            st.write(f"특징: {data['특징']}")
            total = data['HP'] + data['공격'] + data['방어'] + data['스피드']
            st.write(f"총 능력치: {total}")