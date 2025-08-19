import sys, re, pathlib

path = pathlib.Path("MEASURES.dax")
if not path.exists():
    print("❌ ვერ ვპოულობ MEASURES.dax-ს")
    sys.exit(1)

text = path.read_text(encoding="utf-8", errors="ignore")
errors = []

# 1) არ უნდა იყოს ';' არგუმენტების გამყოფად
if ";" in text:
    errors.append("MEASURES.dax-ში აღმოჩენილია ';' — გამოიყენე ',' არგუმენტების გამყოფად.")

# 2) არ უნდა იყოს ქართული ასოები DAX-ში
if re.search(r"[ა-ჰ]", text):
    errors.append("MEASURES.dax-ში აღმოჩენილია ქართული სიმბოლოები — მეჟარების კოდი იყოს მხოლოდ ინგლისურად.")

if errors:
    print("❌ DAX ლინტმა იპოვა პრობლემები:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("✅ DAX ლინტ OK")
