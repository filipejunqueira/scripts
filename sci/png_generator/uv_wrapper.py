from PIL import Image, ImageDraw
import cv2
import numpy as np


class Pattern:

    def __init__(self, background_color=(0, 0, 0), circle_color='#FFFFFF', width=512, height=512, radius=16, number_of_circles_line=8, circle_width=0, margin=128, fpath=None):
        self.background_color = background_color
        self.circle_color = circle_color
        self.width = width
        self.height = height
        self.radius = radius
        self.number_of_circles_line = number_of_circles_line
        self.circle_width = circle_width
        self.margin = margin
        self.fpath = fpath

    def create_control(self, image_name):
        # creating image object with size deterimned by width and height and background color
        self.img = Image.new("RGB", (self.width, self.height), self.background_color)
        canvas = ImageDraw.Draw(self.img)

        # adding the circles

        for row in range(0, self.number_of_circles_line):
            for col in range(0, self.number_of_circles_line):
                # center coordinates (x, y)
                x = self.margin + col * (self.width - 2 * self.margin) / (self.number_of_circles_line - 1) - self.radius / 2
                y = self.margin + row * (self.height - 2 * self.margin) / (self.number_of_circles_line - 1) - self.radius / 2
                shape = [(x, y), (x + self.radius, y + self.radius)]
                # draw.circle(Surface, color, pos, radius, width)
                canvas.ellipse(shape, fill=self.circle_color)

        del canvas

        # pixels = self.img.load()  # create the pixel map
        self.fpath = fr'{image_name}.png'
        self.img.save(self.fpath)
        return self.fpath

    def get_blob_center(self, path):
        _image_cv = cv2.imread(path)
        # converting to gray
        gray_image = cv2.cvtColor(_image_cv, cv2.COLOR_BGR2GRAY)
        # converting to binary
        ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
        # find contours in the binary image
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        shape = (2, 0)
        centers = []

        for c in contours:
            # Calculate the moments for each contours
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centers.append([cx, cy])

        centers = np.asarray(centers)
        centers = np.invert(centers)  # 0,0 is on the bottom left and it goes row wise from left to right.

        return centers

    def show(self):
        ## return image_cv as numpy array
        # img_cv = cv2.imread(self.fpath)
        # window_name = 'image'
        # cv2.imshow(window_name, img_cv)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # return img_cv
        pass

    def horizontal_da(self, centers):

        k = self.number_of_circles_line
        shape1 = (k * (k - 1), 1)
        shape2 = (k * (k - 2), 1)
        d_counter = 0
        a_counter = 0
        dh = np.zeros(shape=shape1)
        ah = np.zeros(shape=shape2)

        for i in range(k * k):
            # Distances in horizontal line
            if i == 0 or (i + 1) % k != 0:  # Condition first point or not the last point of every row.
                h = np.linalg.norm(centers[i + 1] - centers[i])
                dh[d_counter] = h
                d_counter += 1
            else:
                pass

            if i % k != 0 and (i + 1) % k != 0:  # Condition not the first point and not the last point of every row.
                # Angles
                v1 = centers[i] - centers[i - 1]
                v2 = centers[i + 1] - centers[i]
                v1_norm = v1 / np.linalg.norm(v1)
                v2_norm = v2 / np.linalg.norm(v2)
                dot_p = np.dot(v1_norm, v2_norm)
                if dot_p > 1:
                    dot_p = 1.0
                else:
                    pass
                print(dot_p)
                a = np.arccos(dot_p)
                ah[a_counter] = a
                a_counter += 1
                print(i)

            else:
                pass

        return dh, np.rad2deg(ah)

    def vertical_da(self, centers):

        k = self.number_of_circles_line
        shape1 = (k * (k - 1), 1)
        shape2 = (k * (k - 2), 1)
        d_counter = 0
        a_counter = 0
        dv = np.zeros(shape=shape1)
        av = np.zeros(shape=shape2)

        for c in range(k):  # collumn loop
            for n in range(k):  # element loop
                i = c + k * n
                # vertical distances
                if (n == 0 or n % (k - 1) != 0):  # first point or not the last point on every row
                    v = np.linalg.norm(centers[i + k] - centers[i])

                    dv[d_counter] = v
                    d_counter += 1

                else:
                    pass
                # vertical angles
                if n % k != 0 and (n + 1) % k != 0:  # not the first and not the last point on every row
                    v1 = centers[i] - centers[i - k]
                    v2 = centers[i + k] - centers[i]
                    v1_norm = v1 / np.linalg.norm(v1)
                    v2_norm = v2 / np.linalg.norm(v2)
                    dot_p = np.dot(v1_norm, v2_norm)
                    a = np.arccos(dot_p)
                    print(a)
                    av[a_counter] = a
                    a_counter += 1

        return dv, np.rad2deg(av)
