import streamlit as st
import random
from supabase import create_client

# =========================
# 画面設定（最初に）
# =========================
st.set_page_config(page_title="🎯 ルーレットアプリ", layout="centered")

# =========================
# Supabase 接続
# =========================
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("🎯 シンプルルーレットアプリ")
st.write("カンマ（,）で区切って項目を入力してください")

# =========================
# 入力欄
# =========================
items_text = st.text_input("例：飯, 帰る, 飲む")

# =========================
# ルーレット実行
# =========================
if st.button("ルーレットを回す"):
    items = [i.strip() for i in items_text.split(",") if i.strip()]
    if not items:
        st.warning("項目を入力してください")
    else:
        result = random.choice(items)
        st.success(f"🎉 結果：**{result}**")

        try:
            supabase.table("todos").insert({
                "result": result
            }).execute()
        except Exception as e:
            st.error("Supabaseへの保存に失敗")
            st.write(e)

# =========================
# 履歴表示
# =========================
st.subheader("🕒 過去の結果（最新10件）")

try:
    data = supabase.table("todos") \
        .select("*") \
        .order("created_at", desc=True) \
        .limit(10) \
        .execute()

    if data.data:
        for row in data.data:
            st.write(f"{row['created_at']}：{row['result']}")
    else:
        st.write("まだ履歴がありません")
except Exception as e:
    st.error("履歴取得エラー")
    st.write(e)
