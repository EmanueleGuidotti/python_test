
test_settings = {'theme':'light', 'language':'English', 'notifications':'on'}

def add_setting(settings, keys):
    key, value = keys
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"""Setting '{key}' already exists! Cannot add a new setting with this name."""

    if key not in settings:
        settings[key] = value
        return f"""Setting '{key}' added with value '{value}' successfully!"""

def update_setting(settings, keys):
    key, value = keys
    key = key.lower()
    value = value.lower()  

    if key in settings:
        settings[key] = value
        return f"""Setting '{key}' updated to '{value}' successfully!"""

    if key not in settings:
        return f"""Setting '{key}' does not exist! Cannot update a non-existing setting."""

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"""Setting '{key}' deleted successfully!"""

    if key not in settings:
        return f"""Setting not found!"""

def view_settings(settings):
    if len(settings) == 0:
        return f"""No settings available."""
    if len(settings) > 0:
        result = f"""Current User Settings:\n"""
        for key, value in settings.items():
            result += f"""{key.capitalize()}: {value}\n"""
        return result
