import attr

from ..factory import target_factory
from .power import NetworkPowerPort 


@target_factory.reg_resource
@attr.s(eq=False)
class LiebertPowerPort(NetworkPowerPort):

    host = attr.ib(validator=attr.validators.instance_of(str))
    pdu = attr.ib(validator=attr.validators.instance_of(int),
                  converter=int)
    branch = attr.ib(validator=attr.validators.instance_of(int),
                     converter=int)
    rcp = attr.ib(validator=attr.validators.instance_of(int),
                  converter=int)
    model = 'liebert'
    index = '{}.{}.{}'.format(pdu, branch, rcp)
