# この Makefile では、コードのリントとフォーマットチェックを行います

# リンターの設定
LINTER = flake8

# リントのターゲット
lint:
    $(LINTER) .

# コードのフォーマットをチェックするターゲット
format-check:
    black --check .

# リントとフォーマットチェックをまとめて実行するターゲット
check: lint format-check