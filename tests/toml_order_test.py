from frontmatter.frontmatter import order, extract, build


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


def test_order_toml_one_category_in_list():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
tags = ["livre", "other"]
categories = [ "cat1",]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[taxonomies]
tags = [ "livre", "other",]
categories = [ "cat1",]

[extra]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    actual = order(input)
    assert expected == actual


def test_order_toml_one_category_as_string():
    input = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"
tags = ["livre", "other"]
categories = "cat1"
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    expected = """date = 2020-09-08T16:18:51+02:00
title = "Lire le cycle de l'Assassin Royal, c'est compliqué"

[taxonomies]
tags = [ "livre", "other",]
categories = [ "cat1",]

[extra]
twitter = "https://twitter.com/jpcaruana/status/1303356472705921026"
"""
    actual = order(input)
    assert expected == actual


def test_order_yaml_to_toml():
    input = """layout: post
title: "Du G dans le SI, pour quoi faire ?"
date: 2019-05-13
tags: ["open-data"]
categories: découverte
author: "Vincent Ferrand"
comments: true"""
    expected = """title = "Du G dans le SI, pour quoi faire ?"
date = 2019-05-13

[taxonomies]
tags = [ "open-data",]
categories = [ "découverte",]

[extra]
layout = "post"
author = "Vincent Ferrand"
comments = true
"""
    actual = order(input)
    print(actual)
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


def test_extract_toml():
    file_content = """+++
date = 2020-09-08T16:18:51+02:00
title = "Some title"
+++
Some markdown content
"""
    toml, content = extract(file_content)

    assert toml == """
date = 2020-09-08T16:18:51+02:00
title = "Some title"
"""
    assert content == """
Some markdown content
"""


def test_extract_yaml():
    file_content = """---
date: "2020-09-08"
title: "Some title"
---
Some markdown content
"""
    toml, content = extract(file_content)

    assert toml == """
date: "2020-09-08"
title: "Some title"
"""
    assert content == """
Some markdown content
"""


def test_build_filecontent():
    toml = """date = 2020-09-08T16:18:51+02:00
title = "Some title"
"""
    content = """
Some markdown content
"""

    actual = build(toml, content)

    expected = """+++
date = 2020-09-08T16:18:51+02:00
title = "Some title"
+++
Some markdown content
"""

    print("actual", len(actual), actual)
    print("\nexpected", len(expected), expected)
    assert actual == expected
