---
title: CI smoke test
variants: +flyte +union
---

# CI smoke test

This mentions PKCE and CUDA, which are in the project dictionary and should NOT be flagged.

This line has a deliberate mispeling that cspell SHOULD flag.



A compact table (the two blank lines above SHOULD trip markdownlint MD012;
the compact table below should NOT trip MD060 now that it is disabled):

|A|B|
|-|-|
|1|2|
