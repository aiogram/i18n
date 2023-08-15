
package_dir := aiogram_i18n
tests_dir := tests
examples_dir := examples
code_dir := $(package_dir) $(tests_dir) $(examples_dir)

.PHONY: lint
lint:
	black --check --diff $(code_dir)
	ruff $(package_dir)
	mypy --strict $(package_dir)

.PHONY: reformat
reformat:
	black $(code_dir)
	ruff --fix $(package_dir)
