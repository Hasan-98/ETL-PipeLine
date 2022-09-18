"""Running the ETL application"""

import logging
import logging.config
import yaml

def main():
    """
    entry point to run the etl job
    """
    #Parsing YAML File
    config_path = 'D:/ETL_Project/ETL-PipeLine/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    #print(config)
    #comfigure loggin
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    #logger.info("This is a test.")


if __name__ == '__main__':
    main()