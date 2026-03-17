def clean_text(text):
    lines = text.split("\n")

    cleaned_lines = []
    blank_streak = 0

    removed_blank_lines = 0
    trimmed_lines = 0

    for line in lines:

        # trim leading / trailing spaces
        stripped = line.strip()
        if line != stripped:
            trimmed_lines += 1

        line = stripped

        # blank line detection
        if line == "":
            blank_streak += 1
        else:
            blank_streak = 0

        if blank_streak <= 1:
            cleaned_lines.append(line)
        else:
            removed_blank_lines += 1

    # remove leading blank lines
    while cleaned_lines and cleaned_lines[0] == "":
        cleaned_lines.pop(0)
        removed_blank_lines += 1

    # remove trailing blank lines
    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()
        removed_blank_lines += 1

    result = "\n".join(cleaned_lines)

    return result, removed_blank_lines, trimmed_lines


print("Paste your text below.")
print("Type END on a new line to finish.")

input_lines = []

while True:
    line = input()
    if line == "END":
        break
    input_lines.append(line)

text = "\n".join(input_lines)

before_len = len(text)

result, removed_blank, trimmed = clean_text(text)

after_len = len(result)

print("\n--- Cleaned Text ---\n")
print(result)

print("\n--- Statistics ---")
print("Removed blank lines:", removed_blank)
print("Trimmed lines:", trimmed)
print("Characters before:", before_len)
print("Characters after:", after_len)
