from typing import List
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
import cv2
import os
import ffmpeg

from django.conf import settings
eas_key = b'1234567890123456'
iv = b'1234567890123456'

print(eas_key, iv)


def encrypt_image(path: str):
    try:

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

        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        cipher = AES.new(key=eas_key, mode=AES.MODE_CFB, iv=iv)
        cipher_image = cipher.decrypt(image)

        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing encrypted data in image
        fin.write(cipher_image)
        fin.close()

    except Exception as ex:
        print('Error caught : ', ex)


def image_to_video(paths: List[str], **kwargs):
    # (
    #     ffmpeg.input(paths[0], framerate=1/1, ).output(
    #         os.path.join('', 'movie1.mp4')).run()
    # )
    video_folder = 'video_gens'
    media_root = ''
    video_name ='1' + '.mp4'

    frame = cv2.imread(os.path.join('/', paths[0]))
    height, width, layers = frame.shape
    codec = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    video = cv2.VideoWriter(video_name, codec, 1, (width, height))

    for image in paths:
        video.write(cv2.imread(os.path.join(media_root, video_folder, image)))

    video.release()

# decrypt_image('E:\\project\\night-manga-be\\apps\\users\\management\\commands\\image00007.jpg')
# encrypt_image('E:\\project\\night-manga-be\\apps\\users\\management\\commands\\image00007.jpg')


image_to_video(
    ['E:\\project\\night-manga-be\\apps\\users\\management\\commands\\thumb-1920-716130.png'])
