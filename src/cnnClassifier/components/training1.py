from cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path
from cnnClassifier import logger
import os


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        #self.valid_generator = valid_datagenerator.flow_from_directory(
            #directory=self.config.training_data,
            #subset="validation",
            #shuffle=False,
           # **dataflow_kwargs
       # )

       # self.valid_generator = valid_datagenerator.flow_from_directory(
            #directory=self.config.training_data,
            #subset="validationg",
            #shuffle=False,
            #classes=['class1', 'class2', 'class3'],  # List of your class names
           # class_mode='categorical',  # Use 'categorical' for one-hot encoding
           # **dataflow_kwargs
        #)
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=os.path.join(self.config.training_data, "test"),  # Use "test" as the validation directory
            shuffle=False,
            classes=['class1', 'class2', 'class3'],
            class_mode='categorical',
            **dataflow_kwargs
        )
        
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        #self.train_generator = train_datagenerator.flow_from_directory(
           # directory=self.config.training_data,
           # subset="training",
           # shuffle=True,
           # **dataflow_kwargs
       # )



        #self.train_generator = train_datagenerator.flow_from_directory(
           # directory=self.config.training_data,
           # subset="train",
           # shuffle=True,
           # classes=['class1', 'class2', 'class3'],
        

        logger.info(f"Train Data Directory: {os.path.join(self.config.training_data, 'train')}")
        logger.info(f"Validation Data Directory: {os.path.join(self.config.training_data, 'test')}")

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=os.path.join(self.config.training_data, "train"),  # Use "train" as the training directory
            shuffle=True,
            classes=['class1', 'class2', 'class3'],
            class_mode='categorical',
            **dataflow_kwargs
        )

        # Log generator information
        logger.info(f"Train Generator Samples: {self.train_generator.samples}")
        logger.info(f"Validation Generator Samples: {self.valid_generator.samples}")

     # Log generator information
        logger.info(f"Train Generator Samples: {self.train_generator.samples}")
        logger.info(f"Train Generator Batch Size: {self.train_generator.batch_size}")

        logger.info(f"Validation Generator Samples: {self.valid_generator.samples}")
        logger.info(f"Validation Generator Batch Size: {self.valid_generator.batch_size}")



    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )