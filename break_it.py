"""
Break this repository's CI on purpose, one failure type at a time.

    python break_it.py test         a test fails            (test_failure)
    python break_it.py lint         the linter fails        (lint_build)
    python break_it.py dependency   package install fails   (dependency)

It only edits a file. Commit and push the change yourself, on a branch, so
that main stays green:

    git switch -c break-test
    python break_it.py test
    git commit -am "Break: test"
    git push -u origin break-test

To undo an edit that has not been committed:  git checkout .
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        sys.exit(f"{path.name}: expected to find {old!r} exactly once. "
                 "Is the file already broken? Undo with: git checkout .")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def break_test():
    # The discount is added instead of subtracted: two tests fail.
    replace_once(HERE / "shop.py", "(100 - percent)", "(100 + percent)")
    return "shop.py: the discount is now added instead of subtracted"


def break_lint():
    # An import nobody uses: ruff reports F401.
    replace_once(HERE / "shop.py", "\n\n\ndef subtotal(prices):",
                 "\n\nimport os\n\n\ndef subtotal(prices):")
    return "shop.py: an unused import was added"


def break_dependency():
    # A package that does not exist: pip install fails in both jobs.
    path = HERE / "requirements.txt"
    text = path.read_text(encoding="utf-8")
    if "self-heal-no-such-package" in text:
        sys.exit("requirements.txt is already broken. Undo with: git checkout .")
    path.write_text(text.rstrip("\n") + "\nself-heal-no-such-package==9.9.9\n",
                    encoding="utf-8", newline="\n")
    return "requirements.txt: a package that does not exist was added"


SCENARIOS = {"test": break_test, "lint": break_lint, "dependency": break_dependency}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in SCENARIOS:
        sys.exit("usage: python break_it.py " + " | ".join(SCENARIOS))
    print("Broken -", SCENARIOS[sys.argv[1]]())
    print("Now commit and push it on a branch (see the top of this file).")


if __name__ == "__main__":
    main()
