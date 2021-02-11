import argparse
import cv2
import os.path

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_image", type=str, required=True,
                help="path to image to be transposed")
ap.add_argument("-o", "--output_image", type=str, required=True,
                help="path to save transposed image")
args = vars(ap.parse_args())


def main():
    input_path = args['input_image']
    if not os.path.exists(input_path):
        print('specified image does not exist')
        return

    source = cv2.imread(input_path)
    image = cv2.transpose(source)
    cv2.imwrite(args['output_image'], image)


if __name__ == '__main__':
    main()
