from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.constants import (CONFIG_FILE_PATH,
                                     PARAMS_FILE_PATH)
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig)
class ConfigurationManager:

    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self):

        create_directories([self.config.data_ingestion.root_dir])

        data_ingestion = DataIngestionConfig(root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir)

        return data_ingestion


    def get_prepare_base_model_config(self):
        create_directories([self.config.prepare_base_model.root_dir])
        return PrepareBaseModelConfig(
            root_dir= self.config.prepare_base_model.root_dir,
            base_model_path = self.config.prepare_base_model.base_model_path,
            updated_base_model_path = self.config.prepare_base_model.updated_base_model_path,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_outptut_activation_function=self.params.OUTPTUT_ACTIVATION_FUNCTION,
            params_metrics=self.params.METRICS
        )


