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
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range=40,
            horizontal_flip=True,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            **datagenerator_kwargs
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        train_data_dir = os.path.join(self.config.training_data, "train")
        test_data_dir = os.path.join( self.config.training_data, "test")
        print("Train Directory:", train_data_dir)
        print("Test Directory:", test_data_dir)
        logger.info(f"Train Directory : {train_data_dir}")
        logger.info(f"Test Directory : {test_data_dir}")


        self.train_generator = train_datagenerator.flow_from_directory(
            directory=train_data_dir,
            shuffle=True,
            class_mode='categorical',
            **dataflow_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=test_data_dir,
            shuffle=False,
            class_mode='categorical',
            **dataflow_kwargs
        )

        # Original commented-out code
        # self.train_generator = train_datagenerator.flow_from_directory(
        #     directory=os.path.join(self.config.training_data, "train"),
        #     shuffle=True,
        #     classes=['class1', 'class2', 'class3'],
        #     class_mode='categorical',
        #     **dataflow_kwargs
        # )

        # self.valid_generator = valid_datagenerator.flow_from_directory(
        #     directory=os.path.join(self.config.training_data, "test"),
        #     shuffle=False,
        #     classes=['class1', 'class2', 'class3'],
        #     class_mode='categorical',
        #     **dataflow_kwargs
        # )

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
