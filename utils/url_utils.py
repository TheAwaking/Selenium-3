def add_basic_auth_to_url(base_url, username, password):
    protocol, rest = base_url.split("://")
    return f"{protocol}://{username}:{password}@{rest}"
