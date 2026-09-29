import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

class Captcha(object):

    def __init__(self):
        self.templates = {}  # Dictionary to hold templates for each character

    def __call__(self, im_path, save_path, plot = True):
        """
        Algo for inference
        args:
            im_path: .jpg image path to load and to infer
            save_path: output file path to save the one-line outcome
        """
         # Load and preprocess training data
        images, labels = self.prepare_train_data("sampleCaptchas\input", "sampleCaptchas\output")
        # Extract templates based on the training data
        self.train_templates(images, labels)
        if plot:
            self.plot_templates()

        test_image = cv2.imread(im_path)
        test_image = self.preprocess_image(test_image)
        recognized_chars = self.match_template(test_image, save_path, plot = plot)

        # Save the recognized characters to a file
        with open(save_path, 'w') as f:
            f.write(recognized_chars)

    def preprocess_image(self, image):
        """
        Preprocess the image: convert to grayscale and binarize
        args:
            image: input image to preprocess
        returns:
            binary: preprocessed binary image
        """
        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Binarize with automatic thresholding
        _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return binary
    
    def prepare_train_data(self, data_dir, labels_dir):
        """
        Prepare training data with labels from the given directory
        args:
            data_dir: directory containing input images
            labels_dir: directory containing corresponding label files
        returns:
            images: list of preprocessed images
        """
        images, labels = [], []
        for fname in os.listdir(data_dir):

            if fname.endswith('.jpg'):
                base_name = os.path.splitext(fname)[0]
                image_path = os.path.join(data_dir, fname)
                label_path = os.path.join(labels_dir, 'output' + base_name.replace('input', '') + ".txt")

                if not os.path.exists(label_path):
                    continue
            
                image = cv2.imread(image_path)
                preprocessed_image = self.preprocess_image(image)
                images.append(preprocessed_image)

                # Extract label from filename
                with open(label_path, "r") as f:
                    labels.append(f.read().strip())

        return images, labels

    def segment_image(self, binary):
        """
        Segment binary image into individual characters
        args:
            binary: preprocessed binary image
        returns:
            indices_left: list of starting indices for each character
            indices_right: list of ending indices for each character
        """
        counter = 0
        indices_left, indices_right = [], []
        letter_region = False

        for i in range(binary.shape[1]):
            column_has_black = np.any(binary[:, i] != 255)

            if column_has_black and not letter_region:
                # Start of a new letter region          
                indices_left.append(i)
                letter_region = True
            elif column_has_black and letter_region:
                # current letter region
                continue
            elif not column_has_black and letter_region:
                # End of a letter region        
                indices_right.append(i)
                letter_region = False
                counter += 1
                # finish if found the end of the fifth letter
                if counter == 5:
                    break

        return indices_left, indices_right

    def train_templates(self, images, labels):
        """
        Train templates for character recognition
        args:
            images: list of preprocessed images
            labels: list of corresponding labels for the images
        returns:
            generated templates are stored in a dict self.templates
        """
 
        templates_all = {}
        # Iterate through each image and its corresponding label
        for i, label in enumerate(labels):
            # Segment the image into characters
            indices_left, indices_right = captcha_solver.segment_image(images[i])
            # For each character in the label, store the corresponding image segment
            for j, char in enumerate(label):
                if char not in templates_all:
                    templates_all[char] = []
                segment = images[i][:, indices_left[j] - 1 : indices_right[j] + 1]
                # resize the image segment to a fixed size 
                segment = self.resize_segment(segment)
                # Append the segment to the list for the corresponding character 
                templates_all[char].append(segment)

        for letter in templates_all.keys():
            self.templates[letter] = np.mean(np.array(templates_all[letter]), axis = 0)

        # Sort the templates by character
        self.templates = dict(sorted(self.templates.items()))
    
    def match_template(self, test_image, save_path, method = 'cross_correlation', plot = True):
        """
        Match the test image with the trained templates 
        args:
            test_image: preprocessed binary image to recognize
            save_path: path to save the recognized characters
            method: method for template matching (default is 'cross_correlation')
            to_plot: whether to plot the segmented results (default is True)
        returns:
            recognized_chars: string of recognized characters from the test image
        """
        # Segment the test image into characters
        indices_left, indices_right = self.segment_image(test_image)

        # Prepare a list to hold the recognized characters
        recognized_chars = []

        # Iterate through each segmented character
        for i in range(len(indices_left)):
            segment = test_image[:, indices_left[i] - 1 : indices_right[i] + 1]
            segment = self.resize_segment(segment)

            # Compare with each template
            best_match = None
            best_score = float('inf')
            for letter, template in self.templates.items():
                # Calculate score (e.g. cross-correlation)

                score = self.calculate_score(segment, template, method)
                if score < best_score:
                    best_score = score
                    best_match = letter

            recognized_chars.append(best_match)
        recognized_chars = ''.join(recognized_chars)
        # Optionally plot the results
        if plot:
            self.plot_segment_results(test_image, recognized_chars, indices_left, indices_right)

        return recognized_chars
    
    def calculate_score(self, segment, template, method = 'cross_correlation'):
        """
        Calculate the score between a segment and a template
        args:
            segment: image segment to compare
            template: template image to compare against
            method: method for calculating the score (default is 'cross_correlation')
        returns:
            score: calculated score between the segment and the template
        """
        if method == 'cross_correlation':
            # Use cross-correlation to compare the segment with the template
            corr = np.corrcoef(segment.reshape(-1), template.reshape(-1))[0, 1]
            return 1 - corr
        
    def resize_segment(self, segment):
        """
        Resize the segment to a fixed size
        args:
            segment: image segment to resize
        returns:
            resized_segment: resized image segment
        """
        resized_segment = cv2.resize(segment, (10, 30), interpolation=cv2.INTER_NEAREST)
        return resized_segment
        
    def plot_segment_results(self, image, label, indices_left, indices_right):
        """
        Plot segmented results
        args:
            image: original image to visualize
            label: recognized characters for the segmented image
            indices_left: list of starting indices for each character
            indices_right: list of ending indices for each character
        """
        # This function can be used to visualize the segmented characters
        fig, ax = plt.subplots(2, 3, figsize=(15, 10))
        ax[0, 0].imshow(image, cmap='gray')
        ax[0, 0].set_title(label)
        ax = ax.flatten()
        for i in range(len(indices_left)):
            ax[i + 1].imshow(image[:, indices_left[i] - 1 : indices_right[i] + 1], cmap='gray')
            if label:
                ax[i + 1].set_title(label[i])

    def plot_templates(self):

        # Plot extracted templates during training
        fig, ax = plt.subplots(6, 6, figsize=(15, 15))
        ax = ax.flatten()
        for i, (letter, image) in enumerate(captcha_solver.templates.items()):
            ax[i].imshow(image, cmap='gray')
            ax[i].set_title(letter)

if __name__ == "__main__":

    # Example usage
    captcha_solver = Captcha()
    to_plot = True  # Set to True to visualize templates and captcha solver result
    captcha_solver("sampleCaptchas\input\input100.jpg", "sampleCaptchas\output\output100.txt", plot = to_plot)