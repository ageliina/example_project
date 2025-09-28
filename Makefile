.PHONY: tests

dirnames=src tests

tests:
	ruff format $(dirnames)
	pydocstyle $(dirnames)
	pytest --doctest-modules --cov=src $(dirnames)
	coverage html
