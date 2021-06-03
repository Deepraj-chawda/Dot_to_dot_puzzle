'''Python script to convert the given image
    into a black and white and  dotted text using opencv
'''

# python --version = Python 3.8.5
# cv2.__version__ = '4.5.1'
# np.__version__ = '1.19.2'

# import the required modules
import cv2
import numpy as np


class Image_converter:

    def load_img(self, path):
        """
        Load image
        :param path: path of image
        :return: black and white image
        """
        # Read the image
        image = cv2.imread(path, 0)

        # Apply median blur
        image = cv2.medianBlur(image, 5)

        self.save(path="ResultImages/black_white.png", image=image)

    def generate(self, path):
        '''
        generate egde image
        :param path: path of image
        :return: egde image
        '''
        # load image
        image = cv2.imread(path)

        edge_img = cv2.Canny(image, 200, 400)

        edges = np.argwhere(edge_img != [0])

        # finding left border
        prev = 0
        left_border = []
        for x, y in edges:
            if x != prev:
                left_border.append([x, y])
                prev = x

        # finding right border
        right_border = list([x, y] for x, y in dict(edges.tolist()).items())

        # removing right and left border
        for x, y in left_border:
            cv2.circle(edge_img, (y, x), 10, (0, 0, 0), 10)
        for x, y in right_border:
            cv2.circle(edge_img, (y, x), 10, (0, 0, 0), 10)

        # Drawing dots on image
        for x, y in left_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)
        for x, y in right_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)

        # changing color black to white and vise-versa
        edge_img = cv2.bitwise_not(edge_img)

        border = left_border + right_border[::-1]

        # numbering of dots
        num = 1
        for x, y in border[::33]:
            edge_img = cv2.putText(edge_img, str(
                num), (y + 1, x - 3), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0), thickness=1)
            num += 1

        self.save(path="ResultImages/edge.png", image=edge_img)

    def save(self, image, path):
        '''
        save image
        :param image: image
        :param path: Destination path
        :return: None
        '''
        cv2.imwrite(path, image)


# Driver code
if __name__ == "__main__":
    img_con = Image_converter()
    # img = img_con.load_img(
    # 'D:/Learning/Python/Mini Project with OpenCV/Project/Image_converter/images.png')
    # img_con.save(img, 'back_white.png')

    # img = img_con.generate(
    # 'D:/Learning/Python/Mini Project with OpenCV/Project/Image_converter/images.png')
    # img_con.save(img, 'Edge.png')
