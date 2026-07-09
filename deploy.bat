@echo off
echo === 1. Building static site ===
python build.py
if %errorlevel% neq 0 exit /b %errorlevel%

echo === 2. Pushing gh-pages ===
cd /d _deploy
git add -A
git commit -m "update" 2>nul
git push origin gh-pages --force

echo === 3. Pushing source code ===
cd /d ..
git add -A
git commit -m "update" 2>nul
git push origin master

echo === Done! ===
