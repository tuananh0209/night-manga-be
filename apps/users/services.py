import os
import uuid


def gen_user_avatar_name(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    new_filename = str(uuid.uuid4()) + file_extension
    return os.path.join("users", instance.username, new_filename)
