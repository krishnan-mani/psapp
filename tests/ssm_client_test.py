from psapp import ps

import boto3
from moto import mock_ssm


@mock_ssm
def test_ssm_get_parameter():
    client = boto3.client("ssm", region_name="us-east-1")
    client.put_parameter(Name="foo",
                         Value="bar",
                         Type='String')

    ps_client = ps.PS(client)
    response = ps_client.get_parameter("foo")
    assert "bar" == response["Parameter"]["Value"]
