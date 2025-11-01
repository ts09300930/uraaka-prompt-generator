import streamlit as st
import random

st.set_page_config(page_title="裏垢プロンプト生成機", layout="centered")
st.title("裏垢女子AIプロンプト生成機")
st.caption("リアル固定！単語が少なくてもAIが自動で裏垢風に補完")

real_styles = [
    "高画質", "リアル", "自然光", "フィルム写真風", "iPhone撮影風",
    "スナップショット", "夕暮れの街", "暗い部屋", "鏡越し", "夜のネオン"
]

uraaka_addons = [
    "スマホ自撮り", "鏡越し", "舌出し", "胸元チラ", "腰見せ", "暗い部屋",
    "ネオン街", "下着チラ見え", "ノーブラ", "濡れ髪", "ベッドの上", "誘惑ポーズ"
]

theme = st.text_input("テーマ（例: 金髪ギャル, JK, OL）", "金髪ギャル")
words_input = st.text_area("単語（カンマ区切り、なくてもOK）", "ミニスカ, タピオカ")
ero_level = st.slider("エロ度合い", 0, 100, 80)
count = st.selectbox("生成数", [5, 10, 15], index=1)

if st.button("生成！", type="primary"):
    user_words = [w.strip() for w in words_input.split(",") if w.strip()]
    if len(user_words) < 3:
        add_count = 3 - len(user_words)
        added = random.sample(uraaka_addons, k=add_count)
        user_words += added
        st.info(f"AIが自動追加: {', '.join(added)}")
    
    final_words = user_words
    
    with st.spinner("生成中..."):
        prompts = []
        for _ in range(count):
            if ero_level >= 70 and len(final_words) > 1:
                word = random.choice(final_words[:len(final_words)//2 + 1])
            else:
                word = random.choice(final_words)
            style = random.choice(real_styles)
            prompt = f"{theme}, {word}, {style}, 詳細な顔, リアルな肌, 自然なポーズ"
            prompts.append(prompt)
    
    st.success(f"{count}個生成！")
    for i, p in enumerate(prompts, 1):
        st.code(f"{i}. {p}")
    
    txt = "\n".join([f"{i}. {p}" for i, p in enumerate(prompts, 1)])
    st.download_button("保存", txt, "prompts.txt")
