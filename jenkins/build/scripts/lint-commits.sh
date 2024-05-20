set -e

echo "BRANCH_NAME: \"${BRANCH_NAME}\""
echo "CHANGE_TARGET: \"${CHANGE_TARGET}\""
echo "NODE_VERSION: \"${NODE_VERSION}\""

git --version
echo ----------------
firstCommit=$(git rev-list HEAD --not '--remotes=*/release*' '--remotes=*/main' '--remotes=*/develop' | tail -n1)
echo "first commit: ${firstCommit}"
git log -1 ${firstCommit}
echo ----------------
baseCommit=$(git rev-parse ${firstCommit}~)
echo "base commit: ${baseCommit}"
git log -1 ${baseCommit}
echo ----------------
npm install -g @commitlint/cli @commitlint/config-conventional
npx commitlint -V --from=${baseCommit}