def process_mention(status, settings):
    if status.text.lower() == ('@%s hello' % settings.username):
        return dict(response='Hello, world!')
    else:
        return None