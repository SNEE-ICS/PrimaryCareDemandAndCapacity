from typing import Dict, Any, List, Literal, Optional, Union
from enum import Enum
from abc import ABC
from typing_extensions import Annotated

from pydantic import BaseModel, Field
import yaml
import pandas as pd


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




class CSVCatalogEntry(DataCatalogBase):
    source_type: Literal["csv"] = "csv"
    csv_file: str

    def to_pandas_dataframe(self, pandas_read_csv_kwargs:Optional[dict]) -> pd.DataFrame:
        """Loads the csv file into a pandas dataframe

        Returns:
            pd.DataFrame: the dataframe
        """
        if read_csv_kwargs is None:
            read_csv_kwargs = {}
        return pd.read_csv(self.csv_file, **read_csv_kwargs)


class CSVinZIPCatalogEntry(CSVCatalogEntry):
    source_type: Literal["csv_in_zip"] = "csv_in_zip"
    csv_file: str


class SQLQueryCatalogEntry(DataCatalogBase):
    source_type: Literal["sql_query"] = "sql_query"
    query: str
    database_metadata: Optional[Dict[str, Any]] = None

    def to_pandas_dataframe(self, pandas_read_sql_kwargs:Optional[dict]) -> pd.DataFrame:
        """Loads the sql query into a pandas dataframe

        Returns:
            pd.DataFrame: the dataframe
        """
        if read_sql_kwargs is None:
            read_sql_kwargs = {}
        return pd.read_sql(self.query, **read_sql_kwargs)
    

# 'Register' these types with pydantic
DataCatalogEntry = Annotated[Union[CSVCatalogEntry, CSVinZIPCatalogEntry,
                         SQLQueryCatalogEntry], Field(discriminator='source_type')]

class ScenariosCatalogEntry(DataCatalogBase):
    scenarios: List[DataCatalogEntry]

class DataCatalog(BaseModel):
    domain: str
    single_data_sources: List[DataCatalogEntry]
    scenario_data_sources: List[ScenariosCatalogEntry]
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
