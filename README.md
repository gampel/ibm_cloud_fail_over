
```markdown
# IBM Cloud Fail Over Functions


## Overview

IBM Cloud Fail Over is a Python module designed to automate failover processes for applications hosted on IBM Cloud. This module provides essential functions to manage failover scenarios effectively, ensuring high availability and reliability.

## Features

- **Automated Failover**: Seamlessly switch to backup resources when primary resources are unavailable.
- **Resource Management**: Manage critical resources like Virtual IPs and Floating IPs with ease.

## Installation

You can install the IBM Cloud Fail Over module using pip. Run the following command:

```bash
pip install ibm_cloud_fail_over
```

## Usage

### Main Functions

#### `fail_over_cr_vip`

This function manages the failover of a Cloud Resource Virtual IP (CR VIP).

**Usage:**

```python
from ibm_cloud_fail_over import fail_over_cr_vip

# Example usage
active_ip = fail_over_cr_vip(vpc_url='IBM Cloud VPC regional URL",
                           primary_vip='your_primary_vip',
                           secondary_vip='your_secondary_vip',
                           api_key="Optional: API key" )
print(active_ip)
```

**Parameters:**

| Parameter          | Type   | Description                                      |
|--------------------|--------|--------------------------------------------------|
| `vpc_url    `      | str    | IBM Cloud VPC regional URL.                      |
| `primary_vip`      | str    | The primary Virtual IP to monitor.               |
| `secondary_vip`    | str    | The secondary Virtual IP to switch to.           |
| `api_key`          | str    | Optional needed only if you are not using trusted profile, IBM cloud api acsess key               |

**Returns:**

-  The Active ip post failover operation.

#### `fail_over_floating_ip_start`

This function manages the failover of a Floating IP Attach to the caller Endpoint (VSI/BM)

**Usage:**

```python
from ibm_cloud_fail_over import fail_over_floating_ip_start

# Example usage
result = fail_over_floating_ip_start(vpc_url='IBM Cloud VPC regional URL",
                                master_vni_id="Virtual network inetface uuid for new active",
                                passive_vni_id="Virtual network inetface uuid for new passive" ,
                                fip_id="the floating ip uuid",
                                api_key="Optional: API key" ))
print(result)
```

**Parameters:**

| Parameter          | Type     | Description                                      |
|--------------------|----------|--------------------------------------------------|
| `vpc_url    `      | str(url) | IBM Cloud VPC regional URL.                      |
| `master_vni_id`    | str(uuid)| Virtual network inetface uuid for new active.    |
| `passive_vni_id`   | str(uuid)| Virtual network inetface uuid for new active.    |
| `fip_id        `   | str(uuid)| Floating IP uuid to move.                        |
| `api_key`          | str      | Optional needed only if you are not using trusted profile, IBM cloud api acsess key|
**Returns:**

- A confirmation message indicating the success or failure of the failover operation.

#### `fail_over_floating_ip_stop`

This function manages the failover of a Floating IP Detach to the  caller Endpoint (VSI/BM)

**Usage:**

```python
from ibm_cloud_fail_over import fail_over_floating_ip_stop

# Example usage
result = fail_over_floating_ip_stop(vpc_url='IBM Cloud VPC regional URL",
                                master_vni_id="Virtual network inetface uuid for new active",
                                passive_vni_id="Virtual network inetface uuid for new passive" ,
                                fip_id="the floating ip uuid",
                                api_key="Optional: API key" ))
print(result)
```

**Parameters:**

| Parameter          | Type     | Description                                      |
|--------------------|----------|--------------------------------------------------|
| `vpc_url    `      | str(url) | IBM Cloud VPC regional URL.                      |
| `master_vni_id`    | str(uuid)| Virtual network inetface uuid for new active.    |
| `passive_vni_id`   | str(uuid)| Virtual network inetface uuid for new active.    |
| `fip_id        `   | str(uuid)| Floating IP uuid to move.                        |
| `api_key`          | str      | Optional needed only if you are not using trusted profile, IBM cloud api acsess key |
**Returns:**

- A confirmation message indicating the success or failure of the failover operation.
#### `fail_over_get_attached_fip`

This function manages the failover of a Floating IP Detach to the  caller Endpoint (VSI/BM)

**Usage:**

```python
from ibm_cloud_fail_over import fail_over_get_attached_fip

# Example usage
api_key = ""
attached_fip_id, attached_fip_ip = fail_over_get_attached_fip(api_key)

print(attached_fip_ip)
print(attached_fip_id)
```

**Parameters:**
None

**Returns:**
attached_fip_id, attached_fip_ip 

## Troubleshooting

If you encounter issues while using the module, consider the following:

- **Invalid IP Addresses**: Ensure that the IP addresses provided for primary and secondary resources are valid and reachable.
- **Network Issues**: Check your network connectivity to the IBM Cloud resources.
- **Permissions**: Ensure that your IBM Cloud account has the necessary permissions to manage the specified resources.
- **Required dependencies**: Enable [Instance Metada Service](https://cloud.ibm.com/docs/vpc?topic=vpc-imd-configure-service&interface=ui) on Both Enpoints
- **Optional dependencies**: Enable [Trusted profile](https://cloud.ibm.com/docs/vpc?topic=vpc-imd-trusted-profile-metadata&interface=ui) to avoid using and api access key
   


For further assistance, please check the [GitHub Issues](https://github.com/gampel/ibm_cloud_fail_over/issues) page or contact the project maintainer.

## Contributing

We welcome contributions! To contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue on GitHub or contact the project maintainer at [dev@gampel.net](mailto:dev@gampel.net).

```

### TOOD:
 
