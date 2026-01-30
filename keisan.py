from datetime import datetime     # 🟩① datetimeを使うために追加
import os
import json

history = []

# 🟩② ファイル名を自動生成（日付＋時刻入り）
now = datetime.now()                               # 現在の日時を取得
timestamp = now.strftime("%Y-%m-%d_%H%M%S")        # 日時を文字列に変換（ファイル名に使える形）
LOG_FILE = f"calc_history_{timestamp}.json"        # 日付入りのファイル名を自動生成

# 🟦③ ファイル存在チェック
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        try:
            history = json.load(f)
            print(f"以前の履歴を {LOG_FILE} から読み込みました。")
        except json.JSONDecodeError:
            print("履歴ファイルが壊れています。空の履歴から始めます。")
else:
    print(f"新しい履歴ファイル {LOG_FILE} を作成します。")

# 🟥④ 書き込み処理
def save_history():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    print(f"履歴を {LOG_FILE} に保存しました。")

# 計算処理（変更なし）
def calc(a, op, b, digits=3):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "数字を正しく入力してください（例: 12, 3.14, -0.5）"

    if op == "+": result = a + b
    elif op == "-": result = a - b
    elif op == "*": result = a * b
    elif op == "/":
        if b == 0:
            return "0で割ることはできません"
        result = a / b
    elif op == "^": result = a ** b
    elif op == "%": result = a % b
    else:
        return "演算子は +, -, *, /, ^, % のみ使用できます"

    if digits is not None:
        result = round(result, digits)

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {"time": now_str, "a": a, "op": op, "b": b, "result": result}
    history.append(record)

    save_history()
    return result

# 🟧⑤ 実行ごとにファイルを新規作成（上書き防止）
while True:
    s = input("計算式を入力してください（例: 3 + 4、終了=exit、履歴=history）: ")

    if s.lower() == "exit":
        print("終了します。")
        break
    elif s.lower() == "history":
        print("履歴:")
        for h in history:
            print(f"[{h['time']}] {h['a']} {h['op']} {h['b']} = {h['result']}")
        continue

    parts = s.split()
    if len(parts) == 3:
        a, op, b = parts
        print("結果:", calc(a, op, b))
    elif len(parts) == 4:
        a, op, b, digits = parts
        print("結果:", calc(a, op, b, int(digits)))
    else:
        print("'数字 演算子 数字 [桁数]' の形で入力してください")
