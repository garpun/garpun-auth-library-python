VERSION=$(shell python garpunauth/info.py)

init:
	pip3 install pipenv --upgrade
	pipenv install --dev

blacken:
	 nox -s blacken

publish:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

	$(shell git tag $(VERSION))
	$(shell git push origin $(VERSION))

	rm -fr build dist .egg garpunauth.egg-info