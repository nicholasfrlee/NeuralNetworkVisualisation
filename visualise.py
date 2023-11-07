from manim import *
import numpy as np
from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, /
NeuralNetwork, ImageLayer
from PIL import Image

im = Image.open("images/tum.png") 
sqrWidth = np.ceil(np.sqrt(im.size[0]*im.size[1])).astype(int)
im_resize = im.resize((sqrWidth, sqrWidth))
numpy_image = np.asarray(im_resize)

config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0


class BasicScene(ThreeDScene):

    def construct(self):
        nn = NeuralNetwork([
                ImageLayer(numpy_image, height=1.5),
                Convolutional2DLayer(1, 7, 3, filter_spacing=0.18),
                Convolutional2DLayer(7, 5, 3, filter_spacing=0.18, 
                                     activation_function="ReLU"),
                Convolutional2DLayer(5, 3, 3, filter_spacing=0.18),
                FeedForwardLayer(3, activation_function="Sigmoid"),
            ],
            layer_spacing=0.10,
        )
        # Center 
        nn.move_to(ORIGIN)
        self.add(nn)

        forward_pass = nn.make_forward_pass_animation()
        # Play animation
        self.play(forward_pass)