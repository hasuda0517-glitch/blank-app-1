import streamlit as st
import random
from supabase import create_client, Client

# Supabase 接続
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.set_page_config(page_title="ルーレットアプリ", layout="centered")
st.title("🎯 シンプルルーレットアプリ")

st.write("カンマ（,）で区切って項目を入力してください")

items_text = st.text_input(
    "例：飯, 帰る, 飲む",
    ""
)

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
            supabase.table("roulette_history").insert({
                "result": result
            }).execute()

# 過去の結果表示
st.subheader("🕒 過去の結果")

data = supabase.table("roulette_history") \
    .select("*") \
    .order("created_at", desc=True) \
    .limit(10) \
    .execute()

for row in data.data:
    st.write(f"{row['created_at']}：{row['result']}")
