import streamlit as st
import random
from supabase import create_client, Client

# =========================
# Supabase 接続
# =========================
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# =========================
# 画面設定
# =========================
st.set_page_config(page_title="ルーレットアプリ", layout="centered")
st.title("🎯 シンプルルーレットアプリ")

st.write("カンマ（,）で区切って項目を入力してください")

# =========================
# 入力欄
# =========================
items_text = st.text_input(
    "例：飯, 帰る, 飲む",
    ""
)

# =========================
# ルーレット実行
# =========================
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

            # Supabase に保存
            supabase.table("todos").insert({
                "result": result
            }).execute()

# =========================
# 履歴表示
# =========================
st.subheader("🕒 過去の結果（最新10件）")

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
