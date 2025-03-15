import pickle
class DataHandler:
    def __init__(self, base_dir):
        """
        Class to handle the input and output of data
        """
        self.base_dir = base_dir

    def unpickle(self, file):
        """
        Unpickle packed data
        :param file: file name to unpickle data
        :return:each of the batch files contains a dictionary with the following elements:
                data --
                    a 10000x3072 numpy array of uint8s.
                    Each row of the array stores a 32x32 colour image.
                    The first 1024 entries contain the red channel values,
                    the next 1024 the green, and the final 1024 the blue.
                    The image is stored in row-major order,
                    so that the first 32 entries of the array are
                    the red channel values of the first row of the image.
                labels --
                    a list of 10000 numbers in the range 0-9.
                    The number at index i indicates the label of the ith image in the array data.
        """
        with open(self.base_dir + file, 'rb') as fo:
            dict = pickle.load(fo, encoding='bytes')
        return dict

