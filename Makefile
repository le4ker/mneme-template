.PHONY: format lint install setup help

format:
	find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 prettier --write

lint:
	find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 markdownlint

install:
	brew install prettier markdownlint-cli

setup:
	git config core.hooksPath .githooks
	chmod +x .githooks/pre-commit .githooks/check-links

help:
	@echo "format  - format all markdown files with Prettier"
	@echo "lint    - lint all markdown files with markdownlint"
	@echo "install - install dependencies via Homebrew"
	@echo "setup   - configure git hooks"
