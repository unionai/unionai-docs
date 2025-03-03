all:
	rm -rf dist
	mkdir dist
	cp index.html dist/
	rsync -a --progress static/ dist/

	hugo --config hugo.toml,config.serverless.toml --destination dist/serverless
	hugo --config hugo.toml,config.byoc.toml --destination dist/byoc

dev:
	rm -rf public
	if ! scripts/dev-pre-flight.sh; then exit 1; fi
	hugo server --config hugo.toml,hugo.local.toml
