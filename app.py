import streamlit as st

st.title("⚡ 포켓몬 선택 게임 ⚡")
st.write("어떤 포켓몬을 선택할까요?")

col1, col2, col3 = st.columns(3)

with col1:
    # 온라인 이미지 사용 - 100% 작동 보장
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", 
             width=150, caption="피카츄 ⚡")
    if st.button("⚡ 피카츄"):
        st.write("피카츄를 선택했어요!")
        st.write("전기 공격! ⚡⚡⚡")
        st.balloons()

with col2:
    # 온라인 이미지 사용 - 100% 작동 보장
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", 
             width=150, caption="파이리 🔥")
    if st.button("🔥 파이리"):
        st.write("파이리를 선택했어요!")
        st.write("불꽃 공격! 🔥🔥🔥")
        st.balloons()

with col3:
    # 온라인 이미지 사용 - 100% 작동 보장
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png", 
             width=150, caption="꼬부기 💧")
    if st.button("💧 꼬부기"):
        st.write("꼬부기를 선택했어요!")
        st.write("물 공격! 💧💧💧")
        st.balloons()

# 구분선
st.write("---")

# 더 멋진 버전 - 정보까지!
st.title("🌟 포켓몬 정보 게임 🌟")

# 포켓몬 정보 데이터
pokemon_info = {
    "피카츄": {"타입": "전기", "공격": "10만볼트", "이모지": "⚡"},
    "파이리": {"타입": "불꽃", "공격": "화염방사", "이모지": "🔥"},
    "꼬부기": {"타입": "물", "공격": "하이드로펌프", "이모지": "💧"}
}

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", 
             width=120)
    if st.button("⚡ 피카츄", key="pika"):
        info = pokemon_info["피카츄"]
        st.success("피카츄 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("피카츄를 선택했어요!", icon="⚡")

with col2:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", 
             width=120)
    if st.button("🔥 파이리", key="char"):
        info = pokemon_info["파이리"]
        st.success("파이리 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("파이리를 선택했어요!", icon="🔥")

with col3:
    st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png", 
             width=120)
    if st.button("💧 꼬부기", key="squi"):
        info = pokemon_info["꼬부기"]
        st.success("꼬부기 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("꼬부기를 선택했어요!", icon="💧")
