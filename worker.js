export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // Handle root redirect to default variant
    if (url.pathname === '/' || url.pathname === '/docs') {
      return Response.redirect(url.origin + '/docs/byoc/', 301);
    }
    
    // Handle legacy paths and version routing
    if (url.pathname.startsWith('/docs/')) {
      // Extract path components
      const pathParts = url.pathname.split('/').filter(Boolean);
      
      if (pathParts.length >= 2) {
        // Check if this looks like a version path (v1, v2, etc.)
        const possibleVersion = pathParts[1];
        const isVersionPath = /^v\d+$/.test(possibleVersion);
        
        if (!isVersionPath) {
          // No version specified, default to v2 (latest)
          const newPath = '/docs/v2/' + pathParts.slice(1).join('/');
          return Response.redirect(url.origin + newPath, 301);
        }
      }
    }
    
    // Handle legacy domain redirects if needed
    if (url.hostname === 'docs.flyte.org') {
      const newUrl = new URL(url.pathname, 'https://www.union.ai');
      if (!url.pathname.startsWith('/docs/')) {
        newUrl.pathname = '/docs/flyte' + url.pathname;
      }
      return Response.redirect(newUrl.toString(), 301);
    }
    
    // Pass through to static assets
    return env.ASSETS.fetch(request);
  }
};