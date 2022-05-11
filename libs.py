def dict_to_query(d: dict[str, str]):
    items = d.items()
    return "&".join(list(map(lambda x: "=".join(x), items)))




