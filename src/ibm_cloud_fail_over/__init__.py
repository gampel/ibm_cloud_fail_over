"""IBM Cloud Fail Over package."""

from .ibm_cloud_fail_over import HAFailOver
from .ibm_cloud_fail_over import fail_over_cr_vip
from .ibm_cloud_fail_over import fail_over_floating_ip_start
from .ibm_cloud_fail_over import fail_over_floating_ip_stop
from .ibm_cloud_fail_over import fail_over_get_attached_fip
from .ibm_cloud_fail_over import fail_over_public_address_range
from .ibm_cloud_fail_over import fail_over_check_par_zone_compatibility
from .ibm_cloud_fail_over import check_zone_compatibility

__all__ = [
    'HAFailOver',
    'fail_over_cr_vip',
    'fail_over_floating_ip_start',
    'fail_over_floating_ip_stop',
    'fail_over_get_attached_fip',
    'fail_over_public_address_range',
    'fail_over_check_par_zone_compatibility',
]
