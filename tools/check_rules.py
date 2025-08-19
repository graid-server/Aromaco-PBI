import sys, pathlib

p = pathlib.Path("RULES.md")
if not p.exists():
    print("❌ RULES.md არ არსებობს")
    sys.exit(1)

txt = p.read_text(encoding="utf-8", errors="ignore")
ok = True

if 'STAGE_SEMANTIC_ID' not in txt or '"S"' not in txt:
    print('❌ RULES.md-ში უნდა ეწეროს Won: crm_deal[STAGE_SEMANTIC_ID] = "S"')
    ok = False

if 'DATE_CREATE' not in txt:
    print("❌ RULES.md-ში უნდა ეწეროს, რომ მთავარი თარიღია crm_deal[DATE_CREATE]")
    ok = False

if 'CATEGORY_NAME' not in txt or 'აუთი' not in txt:
    print('❌ RULES.md-ში უნდა ეწეროს Out ლოგიკა (CATEGORY_NAME = "აუთი")')
    ok = False

if not ok:
    sys.exit(1)

print("✅ RULES.md შემოწმება OK")
