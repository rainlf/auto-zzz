import os
import pyautorain.tool.ctl as ctl

DIR = os.path.dirname(__file__)
IMG_CONFIRM = os.path.join(DIR, 'img', 'confirm.png')
IMG_PASS = os.path.join(DIR, 'img', 'pass.png')
IMG_PASSED = os.path.join(DIR, 'img', 'passed.png')
IMG_PENDING = os.path.join(DIR, 'img', 'pending.png')
IMG_PUBLISH = os.path.join(DIR, 'img', 'publish.png')
IMG_REVIEW = os.path.join(DIR, 'img', 'review.png')
IMG_REVIEW2 = os.path.join(DIR, 'img', 'review2.png')


def main():
    ctl.find_click(IMG_REVIEW, IMG_REVIEW)
    ctl.find_click(IMG_PASS, 0.9)
    ctl.find_click(IMG_PUBLISH)
    ctl.find_click(IMG_CONFIRM)


if __name__ == '__main__':
    main()
    pass
