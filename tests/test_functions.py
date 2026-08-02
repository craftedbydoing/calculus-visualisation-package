import calc_package.core.functions as func

def test_function_return():
    f = func.sample_function(lambda x: x**2, (0,1), 10)
    assert f[0][0] == 0
    