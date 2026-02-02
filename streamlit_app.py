import streamlit as st
import random
import time

# =====================
# ページ設定
# =====================
st.set_page_config(
    page_title="🎯 豪華ルーレットアプリ",
    page_icon="🎯",
    layout="centered"
)

# =====================
# カスタムCSS
# =====================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    margin-top: 20px;
}

.result {
    font-size: 40px;
    font-weight: bold;
    color: #764ba2;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# =====================
# タイトル
# =====================
st.markdown("<h1 style='text-align: center;'>🎯 シンプル豪華ルーレット</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>迷ったら回せ。運命はルーレットが決める。</p>", unsafe_allow_html=True)

# =====================
# カードUI
# =====================
st.markdown("<div class='card'>", unsafe_allow_html=True)

items_text = st.text_input(
    "🎲 カンマ（,）区切りで項目を入力",
    placeholder="例：飯, 帰る, 飲む"
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================
# 実行ボタン
# =====================
if st.button("🎡 ルーレットを回す", use_container_width=True):
    if items_text.strip() == "":
        st.warning("項目を入力してください")
    else:
        items = [i.strip() for i in items_text.split(",") if i.strip()]

        if len(items) == 0:
            st.warning("有効な項目がありません")
        else:
            with st.spinner("回転中..."):
                time.sleep(1.5)

            result = random.choice(items)

            st.markdown(
                f"<div class='result'>🎉 {result} 🎉</div>",
                unsafe_allow_html=True
            )

# =====================
# フッター
# =====================
st.markdown(
    "<p style='text-align:center; opacity:0.6;'>Powered by Streamlit</p>",
    unsafe_allow_html=True
)

