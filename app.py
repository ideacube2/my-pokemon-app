import streamlit as st

# 확장된 포켓몬 데이터 (실제 작동하는 이미지 URL 사용)
pokemon_data = {
    "피카츄": {
        "타입": "전기", "HP": 35, "공격": 55, "방어": 40, "스피드": 90,
        "특징": "전기를 몸에 저장하는 전기쥐 포켓몬", 
        "이모지": "⚡",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/025.png"
    },
    "파이리": {
        "타입": "불꽃", "HP": 39, "공격": 52, "방어": 43, "스피드": 65,
        "특징": "꼬리 끝의 불꽃으로 기분을 표현", 
        "이모지": "🔥",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/004.png"
    },
    "꼬부기": {
        "타입": "물", "HP": 44, "공격": 48, "방어": 65, "스피드": 43,
        "특징": "단단한 등껍질로 몸을 보호", 
        "이모지": "💧",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/007.png"
    },
    "이상해씨": {
        "타입": "풀", "HP": 45, "공격": 49, "방어": 49, "스피드": 45,
        "특징": "등의 씨앗에서 에너지를 얻음", 
        "이모지": "🌱",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/001.png"
    },
    "라이츄": {
        "타입": "전기", "HP": 60, "공격": 90, "방어": 55, "스피드": 110,
        "특징": "피카츄의 진화형, 더 강한 전기 공격", 
        "이모지": "⚡",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/026.png"
    },
    "리자드": {
        "타입": "불꽃", "HP": 58, "공격": 64, "방어": 58, "스피드": 80,
        "특징": "파이리의 진화형, 더 매서운 불꽃", 
        "이모지": "🔥",
        "이미지": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/005.png"
    }
}

# 페이지 설정
st.set_page_config(
    page_title="나만의 포켓몬 도감",
    page_icon="⚡",
    layout="wide"
)

st.title("📚 나만의 포켓몬 도감")
st.markdown("---")

# 메뉴 선택
menu = st.selectbox("메뉴를 선택하세요", ["포켓몬 정보 보기", "능력치 비교", "전체 도감", "랜덤 뽑기"])

if menu == "포켓몬 정보 보기":
    st.write("## 🔍 포켓몬 정보")
    
    selected = st.selectbox("포켓몬 선택", list(pokemon_data.keys()))
    pokemon = pokemon_data[selected]
    
    # 2열로 배치 (이미지 + 정보)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 이미지 표시
        try:
            st.image(pokemon['이미지'], width=250, caption=f"{selected} {pokemon['이모지']}")
        except:
            # 이미지 로딩 실패시 이모지로 대체
            st.markdown(f"<div style='text-align: center; font-size: 100px;'>{pokemon['이모지']}</div>", unsafe_allow_html=True)
            st.caption("이미지 로딩 중...")
    
    with col2:
        st.write(f"### {selected} {pokemon['이모지']}")
        st.write(f"**타입:** {pokemon['타입']}")
        st.write(f"**특징:** {pokemon['특징']}")
        
        st.write("#### ⚡ 능력치")
        
        # 능력치를 2열로 배치
        stat_col1, stat_col2 = st.columns(2)
        
        with stat_col1:
            # HP
            st.write("💚 **HP**")
            st.progress(min(pokemon['HP'] / 150, 1.0))  # 최대값 150으로 설정
            st.write(f"`{pokemon['HP']}`")
            
            # 공격
            st.write("⚔️ **공격**")
            st.progress(min(pokemon['공격'] / 150, 1.0))
            st.write(f"`{pokemon['공격']}`")
        
        with stat_col2:
            # 방어
            st.write("🛡️ **방어**")
            st.progress(min(pokemon['방어'] / 150, 1.0))
            st.write(f"`{pokemon['방어']}`")
            
            # 스피드
            st.write("💨 **스피드**")
            st.progress(min(pokemon['스피드'] / 150, 1.0))
            st.write(f"`{pokemon['스피드']}`")
        
        # 총 능력치
        total = pokemon['HP'] + pokemon['공격'] + pokemon['방어'] + pokemon['스피드']
        st.metric("🏆 총 능력치", total)

elif menu == "능력치 비교":
    st.write("## ⚔️ 포켓몬 대결 시뮬레이터")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 👈 첫 번째 포켓몬")
        p1 = st.selectbox("선택하세요", list(pokemon_data.keys()), key="compare1")
        try:
            st.image(pokemon_data[p1]['이미지'], width=150)
        except:
            st.write(f"## {pokemon_data[p1]['이모지'] * 3}")
    
    with col2:
        st.write("### 👉 두 번째 포켓몬")
        p2 = st.selectbox("선택하세요", list(pokemon_data.keys()), key="compare2")
        try:
            st.image(pokemon_data[p2]['이미지'], width=150)
        except:
            st.write(f"## {pokemon_data[p2]['이모지'] * 3}")
    
    if st.button("⚔️ 대결 시작!", type="primary"):
        st.write("---")
        st.write("### 📊 능력치 비교 결과")
        
        p1_data = pokemon_data[p1]
        p2_data = pokemon_data[p2]
        
        p1_wins = 0
        p2_wins = 0
        
        # 각 능력치별 비교
        stats = ['HP', '공격', '방어', '스피드']
        
        for stat in stats:
            val1 = p1_data[stat]
            val2 = p2_data[stat]
            
            col_a, col_b, col_c = st.columns([2, 1, 2])
            
            with col_a:
                st.metric(f"{p1} {stat}", val1)
            
            with col_b:
                if val1 > val2:
                    st.write("👈 **승리**")
                    p1_wins += 1
                elif val2 > val1:
                    st.write("**승리** 👉")
                    p2_wins += 1
                else:
                    st.write("🤝 **무승부**")
            
            with col_c:
                st.metric(f"{p2} {stat}", val2)
        
        # 최종 승자 결정
        st.write("---")
        st.write("### 🏁 최종 결과")
        
        if p1_wins > p2_wins:
            st.success(f"🎉 **{p1} 승리!** ({p1_wins}승 {p2_wins}패)")
            st.balloons()
        elif p2_wins > p1_wins:
            st.success(f"🎉 **{p2} 승리!** ({p2_wins}승 {p1_wins}패)")
            st.balloons()
        else:
            st.info(f"🤝 **무승부!** ({p1_wins} : {p2_wins})")

elif menu == "전체 도감":
    st.write("### 🌟 등록된 모든 포켓몬")
    
    # 3개씩 나란히 배치
    pokemon_list = list(pokemon_data.items())
    
    for i in range(0, len(pokemon_list), 3):
        cols = st.columns(3)
        
        for j, col in enumerate(cols):
            if i + j < len(pokemon_list):
                name, data = pokemon_list[i + j]
                
                with col:
                    # 이미지 표시
                    try:
                        st.image(data['이미지'], width=150)
                    except:
                        st.markdown(f"<div style='text-align: center; font-size: 50px;'>{data['이모지']}</div>", unsafe_allow_html=True)
                    
                    st.write(f"**{name}**")
                    st.write(f"타입: {data['타입']}")
                    total = data['HP'] + data['공격'] + data['방어'] + data['스피드']
                    st.write(f"총 능력치: {total}")
                    
                    # 간단한 능력치 바
                    st.progress(min(total / 600, 1.0))  # 최대값 600으로 설정

elif menu == "랜덤 뽑기":
    st.write("## 🎲 포켓몬 랜덤 뽑기")
    st.write("어떤 포켓몬이 나올까요? 운을 시험해보세요!")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🎁 포켓몬 뽑기!", type="primary", use_container_width=True):
            import random
            
            # 랜덤 포켓몬 선택
            selected = random.choice(list(pokemon_data.keys()))
            pokemon = pokemon_data[selected]
            
            st.success(f"축하해요! **{selected}**가 나왔어요!")
            
            # 뽑힌 포켓몬 표시
            try:
                st.image(pokemon['이미지'], width=200)
            except:
                st.markdown(f"<div style='text-align: center; font-size: 100px;'>{pokemon['이모지']}</div>", unsafe_allow_html=True)
            
            st.write(f"**타입:** {pokemon['타입']}")
            st.write(f"**특징:** {pokemon['특징']}")
            
            # 총 능력치로 레어도 결정
            total = pokemon['HP'] + pokemon['공격'] + pokemon['방어'] + pokemon['스피드']
            
            if total >= 300:
                st.write("### 🌟🌟🌟 **전설급!**")
                st.balloons()
            elif total >= 250:
                st.write("### 🌟🌟 **레어!**")
            else:
                st.write("### 🌟 **일반**")
            
            st.write(f"총 능력치: **{total}**")

# 사이드바 정보
st.sidebar.title("📖 도감 정보")
st.sidebar.write(f"**등록된 포켓몬:** {len(pokemon_data)}마리")

# 타입별 개수 표시
type_count = {}
for pokemon in pokemon_data.values():
    ptype = pokemon['타입']
    type_count[ptype] = type_count.get(ptype, 0) + 1

st.sidebar.write("**타입별 개수:**")
for ptype, count in type_count.items():
    st.sidebar.write(f"- {ptype}: {count}마리")

# 푸터
st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.write("💻 **개발자:** [여기에 본인 이름]")
    st.write("🛠️ **제작 도구:** Streamlit")

with col2:
    st.write("📝 **버전:** 2.0")
    st.write("📅 **업데이트:** 2025년")
