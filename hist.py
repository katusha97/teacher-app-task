import argparse
import cv2
import os.path

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_image", type=str, required=True,
                help="path to image")
ap.add_argument("-l", "--limit", type=int, required=False,
                help="number of lines to print", default=1e18)
args = vars(ap.parse_args())


def main():
    input_path = args['input_image']
    if not os.path.exists(input_path):
        print('specified image does not exist')
        return

    image = cv2.imread(input_path)
    counter_for_pixel = {}  # словарь, в котором по пикселю хранится число его встречания
    for row in image:
        for val in row:
            new_tuple = tuple(val)
            if new_tuple not in counter_for_pixel:
                counter_for_pixel[new_tuple] = 0
            counter_for_pixel[new_tuple] += 1

    sorted_d = sorted(counter_for_pixel.items(), key=lambda x: x[1], reverse=True)
    limit = int(args['limit'])
    for key, val in sorted_d[:limit]:
        print(f'{key}: {val}')
    print(f'length of dictionary is: {len(sorted_d)}')


if __name__ == '__main__':
    main()
