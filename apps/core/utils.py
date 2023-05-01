import uuid
import cv2
import os
from typing import List
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from django.conf import settings


def encrypt_image(path: str):
    try:
        eas_key = settings.AES_KEY
        iv = settings.IV_KEY
        # open file for reading purpose
        print(eas_key)

        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        cipher = AES.new(key=eas_key, mode=AES.MODE_CFB, iv=iv)
        cipher_image = cipher.encrypt(image)

        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing encrypted data in image
        fin.write(cipher_image)
        fin.close()

    except Exception as ex:
        print('Error caught : ', ex)


def decrypt_image(path: str):
    try:
        eas_key = settings.AES_KEY
        iv = settings.IV_KEY
        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        cipher = AES.new(key=eas_key, mode=AES.MODE_CFB, iv=iv)
        cipher_image = cipher.decrypt(image)

        # opening file for writing purpose
        # fin = open(path, 'wb')

        # writing encrypted data in image
        # fin.write(cipher_image)
        # fin.close()
        return cipher_image
    except Exception as ex:
        print('Error caught : ', ex)


def image_to_video(paths: List[str], **kwargs):

    video_folder = 'video_gens'
    media_root = settings.MEDIA_ROOT
    video_name = uuid.uuid4() + '.mp4'

    frame = cv2.imread(os.path.join('/', paths[0]))
    height, width, layers = frame.shape
    codec = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    video = cv2.VideoWriter(video_name, codec, 1, (width, height))

    for image in paths:
        video.write(cv2.imread(os.path.join(media_root, video_folder, image)))

    video.release()
