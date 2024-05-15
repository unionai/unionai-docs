build:
	mkdir ./build/html
	sphinx-build ./temp/serverless ./build/html/serverless
	sphinx-build ./temp/byoc ./build/html/byoc
	cp ./source/_static/index.html ./build/html/index.html
clean:
	rm -rf ./build

