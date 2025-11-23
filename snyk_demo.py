# snyk_demo.py
# A tiny Python script with intentionally outdated dependencies
# Just run "pip install -r snyk_demo.py" won't work, but Snyk will scan this file.

print("Hello, Snyk!")

# Requirements (intentionally vulnerable versions):
# Flask==0.12.2
# requests==2.19.1
