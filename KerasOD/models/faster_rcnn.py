import tensorflow as tf

class FasterRCNN(tf.keras.Model):
    def __init__(self) -> None:
        super(FasterRCNN, self).__init__()
        self.feature_extractor = None
        self.rpn = None
        
    def call(self, inputs):
        pass
    
    def build(self):
        pass