# Frontmatter switcher

Switch unordered "[hugo](https://gohugo.io/)"-like frontmatter to a more ordered "[zola](https://www.getzola.org/)"-like one.

Before:

```toml
+++
date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
tags = ["livre", "other"]
categories = ["cat1", "cat2"]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
+++
```

After:

```toml
+++
date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[taxonomies]

tags = ["livre", "other"]
categories = ["cat1", "cat2"]

[extra]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
+++
```
