build:
	sphinx-build ./source ./build/serverless --tag serverless
	sphinx-build ./source ./build/byoc --tag byoc
	mkdir ./build/html
	mv ./build/serverless ./build/html
	mv ./build/byoc ./build/html
	cp ./source/_static/index.html ./build/html/index.html
clean:
	rm -rf ./build

