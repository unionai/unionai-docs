all:
	rm -rf dist
	mkdir dist
	cp index.html dist/
	rsync -a --progress static/ dist/

	hugo --config hugo.toml,config.serverless.toml --destination dist/serverless
	hugo --config hugo.toml,config.byoc.toml --destination dist/byoc

dev:
	#rm -rf public
	hugo server --config hugo.toml,hugo.local.toml
