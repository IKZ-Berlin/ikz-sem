from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import numpy as np
from nomad.config import config
from nomad.datamodel.data import ArchiveSection, EntryData, EntryDataCategory, Schema
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    ELNComponentEnum,
    SectionProperties,
)
from nomad.datamodel.metainfo.basesections import (
    CompositeSystem,
    CompositeSystemReference,
    Process,
    System,
    Measurement,
)
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, Section, SubSection
from nomad.metainfo.metainfo import Category
from structlog.stdlib import BoundLogger

configuration = config.get_plugin_entry_point('nomad_ikz_fz.schema_packages:mypackage')

m_package = SchemaPackage()

class IKZFZCategory(EntryDataCategory):
    m_def = Category(label='IKZ Electronmicroscopy', categories=[EntryDataCategory])


class MySchema(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('MySchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'

class EquipmentElectronMicroscop(Enum):
    NOVA_600 = 'Nova 600'
    APREO = 'Apreo'


class ElectronMicroscopEntry:
    def __init__(self, equipment, manufacturer, max_acceleration_voltage, detectors):
        self.manufacturer = manufacturer
        self.max_acceleration_voltage = max_acceleration_voltage
        self.detectors = detectors

class ElectronMicroscop:
    def __init__(self):
        self.name = "Electron Microscop"
        self.sections = {
            "ElectronMicroscop": {
                "base_sections": [
                    # Uncomment and add as needed
                    # "nomad.datamodel.metainfo.basesections.Measurement",
                    # "nomad.datamodel.metainfo.basesections.Instrument",
                    # "nomad.datamodel.metainfo.basesections.Experiment",
                    "nomad.datamodel.data.EntryData",
                    # "nomad.datamodel.data.EntryDataCategory"
                ],
                "quantities": {
                    "equipment": {
                        "type": {
                            "type_kind": Enum,
                            "type_data": [Equipment.NOVA_600, Equipment.APREO]
                        },
                        "m_annotations": {
                            "eln": {
                                "component": RadioEnumEditQuantity
                            }
                        }
                    },
                    "Manufacturer": {
                        "type": str,
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    },
                    "Maximal_Acceleration_Voltage": {
                        "type": np.float64,
                        "unit": "kV",
                        "m_annotations": {
                            "el": {
                                "defaultDisplayUnit": "kV",
                                "component": NumberEditQuantity
                            }
                        }
                    },
                    "Detectors": {
                        "type": str,
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    }
                }
            }
        }





class ElectronMicroscopJournalEntry:
    def __init__(self, equipment, date, feg, e_column, i_column, chamber, comment):
        self.equipment = equipment
        self.date = date
        self.feg = feg
        self.e_column = e_column
        self.i_column = i_column
        self.chamber = chamber
        self.comment = comment
 class ElectronMicroscopJournal:
    def __init__(self):
        self.name = "NOVA Journal"
        self.sections = {
            "ElectronMicroscop": {
                "base_sections": [
                    # Uncomment and add as needed
                    # "nomad.datamodel.metainfo.basesections.Measurement",
                    "nomad.datamodel.data.EntryData"
                ],
                "quantities": {
                    "equipment": {
                        "type": {
                            "type_kind": Enum,
                            "type_data": [Equipment.NOVA_600, Equipment.APREO]
                        },
                        "m_annotations": {
                            "eln": {
                                "component": RadioEnumEditQuantity
                            }
                        }
                    },
                    "Date": {
                        "type": datetime,
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": DateTimeEditQuantity
                            }
                        }
                    },
                    
                    "FEG": {
                        "type": np.float64,
                        "shape": ['*'],
                        "unit": "pascal",
                        "m_annotations": {
                            "eln": {
                                "component": NumberEditQuantity,
                                "defaultDisplayUnit": "pascal"
                            }
                        }
                    },
                    "E-Column": {
                        "type": np.float64,
                        "shape": ['*'],
                        "unit": "pascal",
                        "m_annotations": {
                            "eln": {
                                "component": NumberEditQuantity,
                                "defaultDisplayUnit": "pascal"
                            }
                        }
                    },
                    "I-Column": {
                        "type": np.float64,
                        "shape": ['*'],
                        "unit": "pascal",
                        "m_annotations": {
                            "eln": {
                                "component": NumberEditQuantity,
                                "defaultDisplayUnit": "pascal"
                            }
                        }
                    },
                    "Chamber": {
                        "type": np.float64,
                        "shape": ['*'],
                        "unit": "pascal",
                        "m_annotations": {
                            "eln": {
                                "component": NumberEditQuantity,
                                "defaultDisplayUnit": "pascal"
                            }
                        }
                    },
                    
                    "Comment": {
                        "type": str,
                        "m_annotations": {
                            "eln": {
                                "component": RichTextEditQuantity
                            }
                        }
                    }
                }
            }
        }
       



class MeasurementMethod(Enum):
    IMAGES = 'Images'
    EDX = 'EDX'
    EBSD = 'EBSD'
    CL = 'CL'
class ElectronMicroscopyEntry:
    def __init__(self, date, hallo, sample_from, equipment, measurement_method, material, sample_id, reference, preperation, goal_or_question, summary, data_file, data_link):
        self.date = date
        self.hallo = hallo
        self.sample_from = sample_from
        self.equipment = equipment
        self.measurement_method = measurement_method
        self.material = material
        self.sample_id = sample_id
        self.reference = reference
        self.preperation = preperation
        self.goal_or_question = goal_or_question
        self.summary = summary
        self.data_file = data_file
        self.data_link = data_link

class ElectronMicroscopy:
    def __init__(self):
        self.name = "Electron Microscopy"
        self.sections = {
            "ElectronMicroscopy": {
                "base_sections": [
                    # Uncomment and add as needed
                    # "nomad.datamodel.metainfo.basesections.Measurement",
                    # "nomad.datamodel.metainfo.basesections.Instrument",
                    # "nomad.datamodel.metainfo.basesections.Experiment",
                    "nomad.datamodel.data.EntryData",
                    # "nomad.datamodel.data.EntryDataCategory"
                ],
                "quantities": {
                    "Date": {
                        "type": datetime,
                        "m_annotations": {
                            "eln": {
                                "component": DateTimeEditQuantity
                            }
                        }
                    },
                    "Hallo": {
                        "type": 'Author',
                        "m_annotations": {
                            "eln": {
                                "component": AuthorEditQuantity
                            }
                        }
                    },
                    "Sample from": {
                        "type": 'Author',
                        "m_annotations": {
                            "eln": {
                                "component": AuthorEditQuantity
                            }
                        }
                    },
                    "Equipment": {
                        "type": {
                            "type_kind": Enum,
                            "type_data": [Equipment.NOVA_600, Equipment.APREO_S]
                        },
                        "shape": ['2'],
                        "m_annotations": {
                            "eln": {
                                "component": EnumEditQuantity
                            }
                        }
                    },
                    "Measurement method": {
                        "type": {
                            "type_kind": Enum,
                            "type_data": [MeasurementMethod.IMAGES, MeasurementMethod.EDX, MeasurementMethod.EBSD, MeasurementMethod.CL]
                        },
                        "shape": ['4'],
                        "m_annotations": {
                            "eln": {
                                "component": EnumEditQuantity
                            }
                        }
                    },
                    "Material": {
                        "type": str,
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    },
                    "SampleID": {
                        "base_sections": [
                            # Uncomment and add as needed
                            # "nomad.datamodel.metainfo.eln.CompositeSystem",
                            "nomad.datamodel.data.EntryData"
                        ],
                        "type": str,
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    },
                    "Reference": {
                        "type": 'nomad.datamodel.data.EntryData',
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": ReferenceEditQuantity
                            }
                        }
                    },
                    "Preperation": {
                        "type": str,
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    },
                    "Goal or Question": {
                        "type": str,
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": StringEditQuantity
                            }
                        }
                    },
                    "Summary": {
                        "type": str,
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": RichTextEditQuantity
                            }
                        }
                    },
                    "Data_file": {
                        "type": str,
                        "shape": ['*'],
                        "description": "The png file name.",
                        "m_annotations": {
                            "eln": {
                                "component": FileEditQuantity
                            },
                            "browser": {
                                "adaptor": RawFileAdaptor
                            }
                        }
                    },
                    "Data_link": {
                        "type": str,
                        "shape": ['*'],
                        "m_annotations": {
                            "eln": {
                                "component": URLEditQuantity
                            }
                        }
                    }
                }
            }
        }