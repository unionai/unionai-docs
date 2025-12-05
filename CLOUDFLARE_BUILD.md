# Cloudflare Pages Configuration

## Build Settings

Configure your Cloudflare Pages project with these settings:

### Framework preset
**None** (Custom/Static site)

### Build command
```bash
chmod +x build.sh && ./build.sh
```

### Build output directory
```bash
dist
```

### Root directory
```bash
/
```

### Environment variables
Set these in your Cloudflare Pages dashboard:

- `PYTHON_VERSION`: `3.9` (or higher)
- `NODE_VERSION`: `18` (or higher)

## How it works

1. The `build.sh` script installs Python dependencies using pip3
2. Runs `make dist` which builds all documentation variants
3. The Python processor (`process_shortcodes.py`) converts Hugo shortcodes to markdown
4. Output is generated in the `dist/` directory for Cloudflare Pages

## Local Testing

To test the build process locally (without UV):

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run build
chmod +x build.sh
./build.sh
```

## Troubleshooting

If the build fails:

1. Check that Python 3.8+ is available
2. Verify that `toml` package can be installed
3. Check Hugo version compatibility (supports 0.145.0+)
4. Review build logs for specific Python errors

The build script automatically falls back from `uv run` to `python3` if UV is not available.