#!/usr/bin/env bash
set -e
USUARIO="${1:-}"
REPO="curso-estatistica-python"
[ -z "$USUARIO" ] && { echo "Uso: ./setup_github.sh USUARIO"; exit 1; }
sed -i "s/SEU_USUARIO/$USUARIO/g" README.md notebooks/*.ipynb
gh auth status &>/dev/null || gh auth login --web --git-protocol https
[ ! -d .git ] && git init -b main
[ -z "$(git config user.email)" ] && git config user.email "${USUARIO}@users.noreply.github.com"
[ -z "$(git config user.name)" ] && git config user.name "$USUARIO"
git add .
git commit -m "Curso de Estatistica com Python e IBGE/SIDRA - 10 aulas" || true
if gh repo view "$USUARIO/$REPO" &>/dev/null; then
  git remote | grep -q origin || git remote add origin "https://github.com/$USUARIO/$REPO.git"
  git push -u origin main
else
  gh repo create "$REPO" --public --source=. --remote=origin --push --description "Curso de 10 aulas de Estatistica com Python usando IBGE/SIDRA"
fi
echo "Pronto: https://github.com/$USUARIO/$REPO"
