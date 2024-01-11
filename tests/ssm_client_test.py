import boto3

from moto import mock_ssm

@mock_ssm
def test_ssm_get_parameter():
    client = boto3.client("ssm", region_name="us-east-1")
    client.put_parameter(Name="foo",
                         Value="bar",
                         Type='String')

    response = client.get_parameter(Name="foo")
    assert "bar" == response["Parameter"]["Value"]
