import os

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base = _up(_up(__file__)) # pandas is 582291 lines long!
files = []
for r, d, f in os.walk(base):
    for file in f:
        if file.endswith(".py") or file.endswith(".md") or file.endswith(".rst") or file.endswith(".glsl") or file.endswith(".txt") or file.endswith(".pyx") or file.endswith(".c") or file.endswith(".toml") or file.endswith(".yml") or file.endswith(".json"):
            files.append(os.path.join(r, file))

line_count = 0
variable_count = 0
comparison_count = 0
class_count = 0
function_count = 0
nothing_count = 0
chars = 0
spaces = 0
words = 0
for file in files:
    try:
        if not ("pmma"+os.sep+"temporary"+os.sep in file or "pmma"+os.sep+"logs"+os.sep in file):
            with open(file, 'r') as f:
                content = f.readlines()
    except:
        continue

    for line in content:
        line_count += 1
        chars += len(line)
        if "if" in line or "else" in line or "elif" in line:
            comparison_count += 1
        if "class" in line:
            class_count += 1
        if "def" in line:
            function_count += 1
        if "=" in line:
            variable_count += 1
        if line.strip() == "":
            nothing_count += 1
        spaces += line.count(" ")
        words += len(line.split())

    #with open(r"H:\Downloads\PMMA aggregate.txt", "a") as file:
        #file.writelines(content)

print(f"PMMA is: {line_count:_} lines long")
print(f"PMMA has: {chars:_} characters!")
print(f"PMMA has: {variable_count:_} variables! {round((variable_count/line_count)*100, 2)} %")
print(f"PMMA has: {comparison_count:_} comparisons! {round((comparison_count/line_count)*100, 2)} %")
print(f"PMMA has: {nothing_count:_} blank lines! {round((nothing_count/line_count)*100, 2)} %")
print(f"PMMA has: {function_count:_} functions! {round((function_count/line_count)*100, 2)} %")
print(f"PMMA has: {class_count:_} classes! {round((class_count/line_count)*100, 2)} %")
print(f"PMMA has: {spaces:_} spaces!")
print(f"PMMA has: {words:_} words!")
print(f"PMMA is: {round((line_count / 582291) * 100, 2)}% the length of Pandas!")
print(f"PMMA has an estimated line size of {round(((chars*8)/1000)/1000, 2)} MB!")