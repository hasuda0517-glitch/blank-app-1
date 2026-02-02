# 🎯 Supabase × Streamlit ルーレットアプリ

## 概要
Supabase の PostgreSQL データベースと Streamlit を利用して作成した  
**シンプルなルーレットアプリ**です。  
ルーレットの結果を Supabase に保存し、アプリを再起動しても履歴が保持されます。

sqlite3 などのローカルデータベースは使用していません。

---

## 主な機能
- カンマ区切りで入力した項目からランダムに1つ選択
- ルーレット結果を Supabase に保存
- 過去の結果を一覧表示（最新10件）

---

## 使用技術
- Python
- Streamlit
- Supabase（PostgreSQL）

---

## Supabase の設定

### テーブル構成（`todos`）

| column名 | type |
|--------|------|
| id | int8 (Primary Key, Auto Increment) |
| result | text |
| created_at | timestamp (default: now()) |

- **RLS（Row Level Security）は OFF**
- 課題・学習目的のため、認証なしで insert を許可

---

## URL

このURLで試すことができます.
https://blank-app-r066lmkf7vm.streamlit.app/


