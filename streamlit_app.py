import streamlit as st
import random
import time

# =====================
# ページ設定
# =====================
st.set_page_config(
    page_title="🎡 Ultimate Roulette",
    page_icon="🎡",
    layout="centered"
)

# =====================
# セッション初期化
# =====================
if "history" not in st.session_state:
    st.session_state.history = []

# =====================
# CSS（かなり盛ってる）
# =====================
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #1a2a6c, #b21f1f, #fdbb2d);
}

.card {
    background: rgba(255,255,255,0.95);
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    margin-top: 30px;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    color: white;
    text-shadow: 0 0 20px rgba(255,255,255,0.6);
}

.subtitle {
    text-align: center;
    color: white;
    opacity: 0.85;
}

.spin {
    font-size: 28px;
    text-align: center;
    animation: blink 0.3s infinite;
}

@keyframes blink {
    0% {opacity: 0.3;}
    50% {opacity: 1;}
    100% {opacity: 0.3;}
}

.result {
    font-size: 52px;
    font-weight: bold;
    text-align: center;
    color: #ff4b4b;
    text-shadow: 0 0 25px rgba(255,75,75,0.8);
    margin-top: 20px;
}

.history {
    background: rgba(255,255,255,0.85);
    border-radius: 15px;
    padding: 15px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# =====================
# タイトル
# =====================
st.markdown("<div class='title'>🎡 ULTIMATE ROULETTE</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>今日の運命を、回せ。</div>", unsafe_allow_html=True)

# =====================
# メインカード
# =====================
st.markdown("<div class='card'>", unsafe_allow_html=True)

items_text = st.text_input(
    "🎯 カンマ区切りで候補を入力",
    placeholder="例：飯, 帰る, 飲む, 寝る"
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================
# 回す
# =====================
if st.button("🎡 回す", use_container_width=True):
    if items_text.strip() == "":
        st.warning("項目を入力してください")
    else:
        items = [i.strip() for i in items_text.split(",") if i.strip()]
        if len(items) == 0:
            st.warning("有効な項目がありません")
        else:
            slot = st.empty()

            # 疑似回転
            for _ in range(15):
                slot.markdown(
                    f"<div class='spin'>🎯 {random.choice(items)}</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.1)

            # 結果
            result = random.choice(items)
            slot.markdown(
                f"<div class='result'>🎉 {result} 🎉</div>",
                unsafe_allow_html=True
            )

            # 履歴保存
            st.session_state.history.insert(0, result)
            st.session_state.history = st.session_state.history[:5]

# =====================
# 履歴表示
# =====================
if st.session_state.history:
    st.markdown("<div class='history'>", unsafe_allow_html=True)
    st.subheader("📜 最近の結果")
    for i, h in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {h}")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================
# フッター
# =====================
st.markdown(
    "<p style='text-align:center; color:white; opacity:0.6;'>Powered by Streamlit</p>",
    unsafe_allow_html=True
)
