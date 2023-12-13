# Placeholder for non-executable code
# import os
# import time
# import tensorflow as tf
# from cnnClassifier.entity.config_entity import PrepareCallbacksConfig
# import urllib.request as request
# from zipfile import ZipFile

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        # Placeholder for non-executable code
        # timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        # tb_running_log_dir = os.path.join(
        #     self.config.tensorboard_root_log_dir,
        #     f"tb_logs_at_{timestamp}",
        # )
        # return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

        pass  # Placeholder for non-executable code

    @property
    def _create_ckpt_callbacks(self):
        # Placeholder for non-executable code
        # return tf.keras.callbacks.ModelCheckpoint(
        #     filepath=str(self.config.checkpoint_model_filepath),
        #     save_best_only=True
        # )

        pass  # Placeholder for non-executable code

    def get_tb_ckpt_callbacks(self):
        # Placeholder for non-executable code
        # return [
        #     self._create_tb_callbacks,
        #     self._create_ckpt_callbacks
        # ]

        pass  # Placeholder for non-executable code
