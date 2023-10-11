from enum import Enum
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Literal, Optional, Type, Union
import yaml


class DataCatalogEntryType(Enum):
    """Enum for the different types of data sources"""
    CSV_IN_ZIP = "csv_in_zip"
    CSV = "csv"
    JSON = "json"
    DATABASE = "database"
    API = "api"
    SCENARIOS = "scenarios"


class DataCatalogEntry(BaseModel):
    name: str
    source_type: DataCatalogEntryType
    description: str
    website_url: Optional[str]
    readme: Optional[str]


class ScenariosCatalogEntry(DataCatalogEntry):
    source_type = Literal[DataCatalogEntryType.SCENARIOS]
    scenarios: List[DataCatalogEntry]


class DataCatalogueCSV(DataCatalogEntry):
    source_type = Union[Literal[DataCatalogEntryType.CSV],
                         Literal[DataCatalogEntryType.CSV_IN_ZIP]]
    csv_file: str


class DataCatalogueCSVinZIP(DataCatalogueCSV):
    source_type = Literal[DataCatalogEntryType.CSV_IN_ZIP]
    zip_url: str


class SQLQuery(DataCatalogEntry):
    source_type: Literal[DataCatalogEntryType.DATABASE]
    sqlalchemy_url: str
    query: str

class DataCatalog(BaseModel):
    domain: str
    data_sources: List[Type[DataCatalogEntry]]
    exceptions: list
    notes: str

    @classmethod
    def load_from_yaml(cls, catalog_path: str = "data_catalog.yaml") -> "DataCatalog":
        """Loads a data catalog from a yaml file

        Args:
            catalog_path (str, optional): path to data catalog file. Defaults to "data_catalog.yaml".

        Raises:
            FileNotFoundError: When file is not found
            yaml.YAMLError: When yaml file is not valid, or parsing error
            Exception: Any other error

        Returns:
            DataCatalog: an instance of the object
        """

        try:
            yaml_dict: Dict[str, Any] = yaml.safe_load(
                open(catalog_path, 'r', encoding='utf-8'))
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Could not find data catalog at {catalog_path}, check filepath.") from e
        except yaml.YAMLError as e:
            raise yaml.YAMLError(
                f"Could not load data catalog at {catalog_path}, check formatting.") from e
        except Exception as e:
            raise Exception(
                f"Could not load data catalog at {catalog_path}, please check file is valid") from e

        cat_instance = cls.model_validate(yaml_dict)
        return cat_instance
