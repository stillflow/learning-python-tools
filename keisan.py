# 履歴を保存するリスト
history = []

def calc(a, op, b, digits=3):
    """2つの数と演算子を受け取り計算する（履歴＋小数点桁数指定対応）"""
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "❌ 数字を正しく入力してください（例: 12, 3.14, -0.5）"

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            return "❌ 0で割ることはできません"
        result = a / b
    elif op == "^":
        result = a ** b
    elif op == "%":
        result = a % b
    else:
        return "❌ 演算子は +, -, *, /, ^, % のみ使用できます"

    # 小数点桁数を指定
    if digits is not None:
        result = round(result, digits)

    history.append(f"{a} {op} {b} = {result}")
    return result


# --- CLI風の入力ループ ---
while True:
    s = input("計算式を入力してください（例: 3 + 4、終了=exit、履歴=history、小数点指定=3 / 2 5）: ")

    # 特殊コマンド処理
    if s.lower() == "exit":
        print("終了します。")
        break
    elif s.lower() == "history":
        print("履歴:", history)
        continue

    # 入力を分割して処理を振り分け
    parts = s.split()
    if len(parts) == 3:
        a, op, b = parts
        print("結果:", calc(a, op, b))
    elif len(parts) == 4:  # 桁数指定あり
        a, op, b, digits = parts
        print("結果:", calc(a, op, b, int(digits)))
    else:
        print("❌ '数字 演算子 数字 [桁数]' の形で入力してください")
