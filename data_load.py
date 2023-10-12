from typing import Dict, Any, List, Literal, Optional, Union
from enum import Enum
from abc import ABC
from typing_extensions import Annotated
from pydantic import BaseModel, Field
import yaml


class DataCatalogEntryType(Enum):
    """Enum for the different types of data sources"""
    CSV_IN_ZIP = "csv_in_zip"
    CSV = "csv"
    JSON = "json"
    DATABASE = "database"
    API = "api"
    SCENARIOS = "scenarios"


class DataCatalogBase(BaseModel, ABC):
    name: str
    description: str
    website_url: Optional[str] = None
    readme: Optional[str] = None


class ScenariosCatalogEntry(DataCatalogBase):
    source_type: Literal["scenarios"] = "scenarios"
    scenarios: List["DataCatalogEntry"]


class CSVCatalogEntry(DataCatalogBase):
    source_type: Literal["csv"] = "csv"
    csv_file: str


class CSVinZIPCatalogEntry(CSVCatalogEntry):
    source_type: Literal["csv_in_zip"] = "csv_in_zip"
    zip_url: str


class SQLQueryCatalogEntry(DataCatalogBase):
    source_type: Literal["sql_query"] = "sql_query"
    sqlalchemy_url: str
    query: str

# 'Register' these types with pydantic
DataCatalogEntry = Annotated[Union[ScenariosCatalogEntry, CSVCatalogEntry,CSVinZIPCatalogEntry], Field(discriminator='source_type')]


class DataCatalog(BaseModel):
    domain: str
    data_sources: List[DataCatalogEntry]
    exceptions: list = Field(default_factory=list)
    notes: Optional[str] = None

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
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"Could not find data catalog at {catalog_path}, check filepath.") from error
        except yaml.YAMLError as error:
            raise yaml.YAMLError(
                f"Could not load data catalog at {catalog_path}, check formatting.") from error
        except Exception as error:
            raise Exception(
                f"Could not load data catalog at {catalog_path}, please check file is valid") from error

        

        cat_instance = cls.model_validate(yaml_dict)
        return cat_instance
