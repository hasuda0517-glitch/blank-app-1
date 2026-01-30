import streamlit as st
import random

st.set_page_config(page_title="ルーレットアプリ", layout="centered")
st.title("🎯 シンプルルーレットアプリ")

st.write("カンマ（,）で区切って項目を入力してください")

# 入力欄
items_text = st.text_input(
    "例：飯, 帰る, 飲む",
    ""
)

# ルーレット実行
if st.button("ルーレットを回す"):
    if items_text.strip() == "":
        st.warning("項目を入力してください")
    else:
        items = [item.strip() for item in items_text.split(",") if item.strip()]
        
        if len(items) == 0:
            st.warning("有効な項目がありません")
        else:
            result = random.choice(items)
            st.success(f"🎉 結果：**{result}**")
