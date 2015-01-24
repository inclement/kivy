# Tasks:
# - generate images
# - generate rst for images

import argparse
import sys
import os
import glob
import subprocess
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description='Generate the Kivy example gallery')

parser.add_argument('task', type=str,
                    choices=['images', 'rst'])

args = parser.parse_args()


def collate_examples():
    # As a POC, just check widgets and canvas examples
    widgets = glob.glob('widgets/*.py')
    canvas = glob.glob('canvas/*.py')

    return {'Widgets': [filen_info(filen)
                        for filen in widgets],
            'Canvas': [filen_info(filen)
                       for filen in canvas]}

def filen_info(filen):
    image_filen = image_filen_from_filen(filen)
    return (filen, image_filen, os.path.exists(image_filen))

def image_filen_from_filen(filen):
    new_filen = filen[:-3].replace('/', '_') + '.png'
    return os.path.join('gallery_images', new_filen)

task = args.task
if task == 'images':
    if not os.path.exists('gallery_images'):
        os.mkdir('gallery_images')

    examples = collate_examples()

    for heading, filens in examples.items():

        for filen, image_filen, exists in filens:
            if exists:
                print '{} exists!'.format(image_filen)

elif task == 'rst':
    env = Environment(loader=FileSystemLoader('.'))

    template = env.get_template('gallery_template.rst')

    with open('gallery.rst', 'w') as fileh:
        fileh.write(template.render(headings=collate_examples()))
