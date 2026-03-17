# ===== [① ライブラリ読み込み・準備] =====
import json, os
from datetime import date


# ===== [② データ保存先の指定] =====
DB = "kakeibo.json"


# ===== [③ データ読み込み] =====
def load():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as f:
        return json.load(f)


# ===== [④ データ保存] =====
def save(rows):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


# ===== [⑤ 家計簿に1件追加] =====
def add(rows):
    amt = int(input("金額(支出は- / 収入は+)> ").strip())
    memo = input("メモ(空OK)> ").strip()
    d = input("日付 YYYY-MM-DD(空=今日)> ").strip() or str(date.today())

    rows.append({
        "date": d,
        "amount": amt,
        "memo": memo,
        "tag": None
    })

    save(rows)
    print("追加しました。")


# ===== [⑥ 一覧表示] =====
def show(rows, only_untagged=False):
    items = [r for r in rows if r["tag"] is None] if only_untagged else rows

    for i, r in enumerate(reversed(items), 1):
        tag = r["tag"] if r["tag"] else "-"
        print(f"{i:>3} | {r['date']} | {r['amount']:>7} | {tag:<8} | {r['memo']}")

    print(f"件数: {len(items)}")


# ===== [⑦ 月別合計・tag別集計] =====
def month_total(rows):
    ym = input("対象月 YYYY-MM(例 2026-01)> ").strip()

    total = sum(
        r["amount"] for r in rows
        if r["date"].startswith(ym)
    )

    by_tag = {}
    for r in rows:
        if r["date"].startswith(ym) and r["tag"]:
            by_tag[r["tag"]] = by_tag.get(r["tag"], 0) + r["amount"]

    print(f"\n{ym} 合計: {total}")

    if by_tag:
        print("tag別:")
        for k, v in sorted(by_tag.items(), key=lambda x: -abs(x[1])):
            print(f"  {k}: {v}")


# ===== [⑧ tag編集] =====
def tag_edit(rows):
    # 一覧は「新しい順」表示だが、内部は古い順なので index を変換する
    show(rows)

    n = int(input("tagを付けたい番号> ").strip())
    idx = len(rows) - n

    if idx < 0 or idx >= len(rows):
        print("番号が不正です。")
        return

    t = input("tag(空=未分類に戻す)> ").strip()
    rows[idx]["tag"] = t or None

    save(rows)
    print("更新しました。")


# ===== [⑨ メイン処理（操作メニュー）] =====
def main():
    rows = load()

    while True:
        print("\n[1]追加 [2]一覧 [3]未分類だけ [4]月合計 [5]tag付け [0]終了")
        cmd = input("> ").strip()

        if cmd == "1":
            add(rows)
        elif cmd == "2":
            show(rows)
        elif cmd == "3":
            show(rows, only_untagged=True)
        elif cmd == "4":
            month_total(rows)
        elif cmd == "5":
            tag_edit(rows)
        elif cmd == "0":
            break
        else:
            print("入力が不正です。")

# ===== [⑩ プログラム開始点] =====
if __name__ == "__main__":
    main()
