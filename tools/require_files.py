import sys, os

REQUIRED = [
    "README.md",
    "RULES.md",
    "MEASURES.dax",
    "MODEL.md",
    "CHANGELOG.md",
    "docs/visuals.md",
    "docs/plan.md",
]

missing = [p for p in REQUIRED if not os.path.exists(p)]
if missing:
    print("❌ აკლია ფაილები:", ", ".join(missing))
    sys.exit(1)
print("✅ ყველა აუცილებელი ფაილი არსებობს")
