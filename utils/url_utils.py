def add_basic_auth_to_url(base_url, username, password):
    protocol, rest = base_url.split("://", 1)
    auth_url = f"{protocol}://{username}:{password}@{rest}"
    return auth_url
