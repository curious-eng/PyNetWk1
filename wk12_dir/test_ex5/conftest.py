@pytest.fixture(scope='module')
def my_connect(request):
    net_connect = ConnectHandler(
        host="arista1.lasthop.io",
        username=username,
        password=password,
        device_type="arista_eos",
    )

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect
