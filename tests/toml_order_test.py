from frontmatter.frontmatter import order


def test_order_toml():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
tags = ["livre", "other"]
categories = ["cat1", "cat2"]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[taxonomies]
tags = [ "livre", "other",]
categories = [ "cat1", "cat2",]

[extra]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    actual = order(input)
    assert expected == actual


def test_order_toml_no_taxonomies():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[extra]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    actual = order(input)
    assert expected == actual


def test_order_toml_no_extra():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
tags = ["livre", "other"]
categories = ["cat1", "cat2"]
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[taxonomies]
tags = [ "livre", "other",]
categories = [ "cat1", "cat2",]
"""
    actual = order(input)
    assert expected == actual


def test_order_toml_no_taxonomies_no_extra():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
"""
    actual = order(input)
    assert expected == actual
    assert input == actual
