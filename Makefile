all:
	rm -rf dist
	mkdir dist
	cp index.html dist/
	rsync -a --progress static/ dist/

	hugo --config hugo.toml,config.serverless.toml --destination dist/serverless
	hugo --config hugo.toml,config.byoc.toml --destination dist/byoc

dev:
	rm -rf public
	if [[ ! -e hugo.local.toml ]]; then
	  echo "FATAL: You need to have a 'hugo.local.toml' for development mode."
		echo "       (please copy it from 'hugo.local.toml~sample' to get started)"
		exit 1
	fi
	hugo server --config hugo.toml,hugo.local.toml
