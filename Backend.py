'''Python script to convert the given image
    into a black and white and  dotted text using opencv
'''

#python --version = Python 3.8.5
#cv2.__version__ = '4.5.1'

# import the required modules
import cv2

class Image_converter():

    def load_img(self,path):
        """
        Load image
        :param path: path of image
        :return: black and white image
        """
        # Read the image
        image = cv2.imread(path, 0)

        # Apply median blur
        image = cv2.medianBlur(image, 5)

        return  image

    def generate(self,path):
        '''
        generate egde image
        :param path: path of image
        :return: egde image
        '''
        #load image
        image = self.load_img(path)

        # Apply MEAN thresholding to get refined edges
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        return  image

    def save(self,image,path):
        '''
        save image
        :param image: image
        :param path: destination path
        :return: None
        '''
        cv2.imwrite(path,image)


#Driver code
if __name__ == "__main__":
    img_con = Image_converter()
    img = img_con.load_img('1.jpg')
    img_con.save(img,'back_white.png')

    img = img_con.generate('1.jpg')
    img_con.save(img,'Edge.png')
