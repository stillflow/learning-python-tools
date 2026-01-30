import json

FILENAME = "todo.json"

# --- データ読み込み ---
try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        todos = json.load(f)
except FileNotFoundError:
    todos = []


# --- データ保存 ---
def save_data():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# --- タスク追加 ---
def add_task():
    title = input("タスク名: ")
    task = {"title": title, "done": False}
    todos.append(task)
    save_data()
    print("追加しました！")


# --- タスク一覧（全部表示） ---
def show_tasks():
    print("\n--- 全タスク一覧 ---")
    if not todos:
        print("（タスクはありません）")
        return

    for i, task in enumerate(todos):
        status = "✔" if task["done"] else "・"
        print(f"{i}: {status} {task['title']}")


# --- 🟦 未完了だけ表示（データはそのまま） ---
def show_unfinished_tasks():
    print("\n--- 未完了タスク ---")
    found = False

    for i, task in enumerate(todos):
        # ★ データは変えずに「見せ方」だけ絞る
        if not task["done"]:
            print(f"{i}: ・ {task['title']}")
            found = True

    if not found:
        print("（未完了タスクはありません）")


# --- 完了にする ---
def complete_task():
    show_tasks()
    if not todos:
        return

    idx_str = input("完了にする番号: ")
    if not idx_str.isdigit():
        print("数字を入力してください")
        return

    idx = int(idx_str)
    if 0 <= idx < len(todos):
        todos[idx]["done"] = True
        save_data()
        print("完了にしました！")
    else:
        print("番号が正しくありません")


# --- 削除 ---
def delete_task():
    show_tasks()
    if not todos:
        return

    idx_str = input("削除する番号: ")
    if not idx_str.isdigit():
        print("数字を入力してください")
        return

    idx = int(idx_str)
    if 0 <= idx < len(todos):
        deleted = todos.pop(idx)
        save_data()
        print(f"「{deleted['title']}」を削除しました")
    else:
        print("番号が正しくありません")


# --- 完了 ⇄ 未完了 切り替え ---
def toggle_task():
    show_tasks()
    if not todos:
        return

    idx_str = input("切り替える番号: ")
    if not idx_str.isdigit():
        print("数字を入力してください")
        return

    idx = int(idx_str)
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
        save_data()

        state = "完了" if todos[idx]["done"] else "未完了"
        print(f"「{todos[idx]['title']}」を {state} にしました")
    else:
        print("番号が正しくありません")


# --- メイン ---
def main():
    while True:
        print("\n1:追加  2:一覧  3:完了  4:削除  5:切り替え  6:未完了だけ表示  0:終了")
        cmd = input("番号: ")

        if cmd == "1":
            add_task()
        elif cmd == "2":
            show_tasks()
        elif cmd == "3":
            complete_task()
        elif cmd == "4":
            delete_task()
        elif cmd == "5":
            toggle_task()
        elif cmd == "6":
            show_unfinished_tasks()
        elif cmd == "0":
            print("終了します。")
            break
        else:
            print("正しい番号を入力してください")


if __name__ == "__main__":
    main()
