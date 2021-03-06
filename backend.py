'''Python script to convert the given image
    into a black and white and  dotted text using opencv
'''

# python --version = Python 3.8.5
# cv2.__version__ = '4.5.1'

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

        return image

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

        width, height = edge_img.shape

        # adding border
        edge_img = np.full((width + 100, height + 100), 0, dtype="uint8")

        # draw edges
        for x, y in edges:
            edge_img[x + 40, y + 40] = 255

        # copy for show image
        #self.show_img = edge_img.copy()

        # edge coordinates
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
            cv2.circle(edge_img, (y, x), 8, (0, 0, 0), 10)
        for x, y in right_border:
            cv2.circle(edge_img, (y, x), 8, (0, 0, 0), 10)

        # Drawing dots on image
        for x, y in left_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)
            #cv2.circle(self.show_img, (y, x), 3, (255, 255, 255), 4)
        for x, y in right_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)
           # cv2.circle(self.show_img, (y, x), 3, (255, 255, 255), 4)

        # changing color black to white and vise-versa
        edge_img = cv2.bitwise_not(edge_img)
       # self.show_img = cv2.bitwise_not(self.show_img)

        border = left_border + right_border[::-1]

        # numbering of dots
        edge_img = cv2.putText(edge_img, 'Start', (border[0][1]+10, border[0][0] - 10), cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0, 0, 0), thickness=2)

        num = 1
        for x, y in border[::33]:
            edge_img = cv2.putText(edge_img, str(num), (y + 1, x - 3), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0), thickness=1)
            #self.show_img = cv2.putText(self.show_img, str(num), (y + 1, x - 3), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5,
                                   #color=(0, 0, 0), thickness=1)
            num += 1

        return edge_img

    def show(self,path):
        '''
        show full dotted image
        :return: dotted image
        '''
        # load image
        image = cv2.imread(path)

        edge_img = cv2.Canny(image, 200, 400)

        edges = np.argwhere(edge_img != [0])

        width, height = edge_img.shape

        # adding border
        edge_img = np.full((width + 100, height + 100), 0, dtype="uint8")

        # draw edges
        for x, y in edges:
            edge_img[x + 40, y + 40] = 255

        # edge coordinates
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
        # Drawing dots on image
        for x, y in left_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)
            #cv2.circle(self.show_img, (y, x), 3, (255, 255, 255), 4)
        for x, y in right_border[::33]:
            cv2.circle(edge_img, (y, x), 3, (255, 255, 255), 4)
            #cv2.circle(self.show_img, (y, x), 3, (255, 255, 255), 4)
        # changing color black to white and vise-versa
        edge_img = cv2.bitwise_not(edge_img)

        border = left_border + right_border[::-1]

        # numbering of dots
        edge_img = cv2.putText(edge_img, 'Start', (border[0][1] + 10, border[0][0] - 10), cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(0, 0, 0), thickness=2)
        num = 1

        for x, y in border[::33]:
            edge_img = cv2.putText(edge_img, str(num), (y + 1, x - 3), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5,
                                   color=(0, 0, 0), thickness=1)
            #self.show_img = cv2.putText(self.show_img, str(num), (y + 1, x - 3), cv2.FONT_HERSHEY_SIMPLEX,
                                        #fontScale=0.5,
                                       # color=(0, 0, 0), thickness=1)
            num += 1

        return edge_img

    def save(self, image, path):
        '''
        save image
        :param image: image
        :param path: destination path
        :return: None
        '''
        cv2.imwrite(path, image)


# Driver code
if __name__ == "__main__":
    img_con = Image_converter()
    img = img_con.load_img('images//sir.jpg')
    img_con.save(img, 'images//back_white.png')

    img1= img_con.generate('images//sir.jpg')
    img_con.save(img1, 'images//Edge.png')
    img2 = img_con.show('images//sir.jpg')
    img_con.save(img2, 'images//show.png')

