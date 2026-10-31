.PHONY: format check-format lint test check install setup help

format:
	find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 prettier --write

check-format:
	find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 prettier --check

lint:
	find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 markdownlint

test:
	python3 -m unittest discover -s tests -v

check: check-format lint test

install:
	brew install prettier markdownlint-cli

setup:
	git config core.hooksPath .githooks
	chmod +x .githooks/pre-commit .githooks/check-links

help:
	@echo "format  - format all markdown files with Prettier"
	@echo "check-format - verify Markdown formatting with Prettier"
	@echo "lint    - lint all markdown files with markdownlint"
	@echo "test    - run Python unit tests"
	@echo "check   - run formatting, lint, and tests"
	@echo "install - install dependencies via Homebrew"
	@echo "setup   - configure git hooks"
