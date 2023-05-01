
default: build

build: ts

readme:
	@echo "Recompiling README ..."
	@readmix --compile --markdown README.rx
	@echo "    Done."

license:
	@echo "Recompiling LICENSE ..."
	@readmix --compile --markdown LICENSE.rx
	@echo "    Done."

publish: build readme license
	@echo "Publishing to NPM ..."
	@npm publish
	@echo "    Done."

ts: clean
	@echo "Compiling TS to JS ..."
	@tsc
	@echo "    Done."

clean:
	@echo "Cleaning JS ..."
	@rm -rf dist
	@echo "    Done."
