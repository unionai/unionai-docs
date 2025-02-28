#!/bin/sh

echo Syncing content...
if command -v rsync 1>/dev/null; then
  rsync -a content/ source/
else
  cp -R content/ source/
fi
