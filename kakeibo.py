import json
from datetime import date

FILENAME = "kakeibo.json"
FAV_FILE = "favorites.json"

# 家計簿データ読み込み
try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        kakeibo = json.load(f)
except FileNotFoundError:
    kakeibo = []

# お気に入りデータ読み込み（店名のみのリスト）
try:
    with open(FAV_FILE, "r", encoding="utf-8") as f:
        favorites = json.load(f)
except FileNotFoundError:
    favorites = []

# お気に入りに店名を追加
def add_favorite():
    place = input("店名（お気に入り追加）：")
    favorites.append(place)
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(favorites, f, ensure_ascii=False, indent=2)
    print(f"{place} をお気に入りに保存しました。")

# ① お気に入りから番号で選ぶ機能を追加
def select_favorite_place():
    if not favorites:
        print("お気に入り店舗がありません。手入力してください。")
        return None

    print("\n=== よく行くお店 ===")
    # ② 番号付きで表示（enumerate追加）
    for i, shop in enumerate(favorites, 1):
        print(f"{i}: {shop}")
    print("0: その他 (自分で入力)")

    # ③ 番号入力受付を追加
    choice = input("番号を入力：")

    # ④ 0なら「自分で入力」
    if choice == "0":
        return None

    try:
        idx = int(choice) - 1     # ⑤ 数 → インデックスへ変換
        return favorites[idx]     # ⑥ 選んだ店名を返す
    except:
        print("番号が正しくありません。")
        return None

# ----------------------------------------------------
# 🟦 月別合計を計算する関数（追加）
def calc_monthly_totals(kakeibo):
    monthly_totals = {}
    for entry in kakeibo:
        month = entry["date"][:7]  # "2025-11-03" → "2025-11"
        monthly_totals[month] = monthly_totals.get(month, 0) + entry["price"]
    return monthly_totals
# ----------------------------------------------------

# モード選択
mode = input("1: 普通に入力 / 2: お気に入り登録 → ")

if mode == "2":
    add_favorite()
    exit()

# ⑦ まず番号で店を選ぶ
place = select_favorite_place()

# ⑧ 選ばれなかった場合だけ手入力
if place is None:
    place = input("店名は？：")

price = int(input("金額は？："))

today = date.today().isoformat()
record = {"date": today, "place": place, "price": price}
kakeibo.append(record)

with open(FILENAME, "w", encoding="utf-8") as f:
    json.dump(kakeibo, f, ensure_ascii=False, indent=2)

total = sum(entry["price"] for entry in kakeibo)
print(f"\n{today} の外食を記録しました！ 現在の外食合計：{total}円")

# ----------------------------------------------------
# 🟦 ここで月別集計を表示（追加）
totals = calc_monthly_totals(kakeibo)

print("\n=== 月別の外食合計 ===")
for month, total_price in totals.items():
    print(f"{month}：{total_price}円")
# ----------------------------------------------------
