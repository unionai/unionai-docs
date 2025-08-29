// Static site handler for Hugo site
export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  },
};
