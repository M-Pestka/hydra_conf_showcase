import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf

from dataclasses import dataclass, field

@dataclass
class OPTConf:
    pass

@dataclass
class SGDConf(OPTConf):
    momentum: float 

@dataclass
class ADAMConf(OPTConf):
    beta1: float
    beta2: float

@dataclass
class MainConf:
    optimizer: OPTConf


cs = ConfigStore.instance()
cs.store(name="base_conf", node=MainConf)
cs.store(group="optimizer",
        name="base_sgd",
        node=SGDConf,
        )
cs.store(group="optimizer",
        name="base_adam",
        node=ADAMConf,
        )


@hydra.main(config_name="conf", config_path=".")
def main(cfg: MainConf):
    configuration_object = OmegaConf.to_object(cfg)
    print(configuration_object)

main()
