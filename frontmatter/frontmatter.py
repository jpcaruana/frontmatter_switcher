import toml


def build(frontmatter, content):
    return "+++\n" + frontmatter + "+++" + content


def extract(content):
    parts = content.split("+++")
    return parts[1], parts[2]


def order(toml_string):
    parsed_toml = toml.loads(toml_string)
    target_toml = {"taxonomies": {}, "extra": {}}
    for key in parsed_toml.keys():
        value = parsed_toml.get(key)
        if key in ["taxonomies", "extra"]:
            continue
        if key in ["tags", "categories"]:
            target_toml["taxonomies"][key] = value
            continue
        if key not in ["date", "title"]:
            target_toml["extra"][key] = value
        else:
            target_toml[key] = value
    if target_toml.get("taxonomies") == {}:
        target_toml.pop("taxonomies")
    if target_toml.get("extra") == {}:
        target_toml.pop("extra")
    return toml.dumps(target_toml)
