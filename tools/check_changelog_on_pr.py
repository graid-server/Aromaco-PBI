import os, sys, subprocess

# მუშაობს მხოლოდ pull_request-ზე
if os.environ.get("GITHUB_EVENT_NAME", "") != "pull_request":
    print("ℹ️ CHANGELOG check მხოლოდ PR-ზე მოქმედებს")
    sys.exit(0)

# შევადაროთ main-ს (თუ სხვა default branch გაქვს, შეცვალე აქ)
base = "origin/main...HEAD"
changed = subprocess.check_output(["git", "diff", "--name-only", base], text=True)
files = set(f.strip() for f in changed.splitlines() if f.strip())

if "CHANGELOG.md" not in files:
    print("❌ PR-ში უნდა იყოს განახლებული CHANGELOG.md")
    sys.exit(1)

print("✅ CHANGELOG განახლებულია PR-ში")
