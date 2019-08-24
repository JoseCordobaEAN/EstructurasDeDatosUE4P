def sumatoria(num):
    """
    (int) -> int

    Calcula la sumatoria de todos los numeros hasta el valor dado

    >>> sumatoria(10)
    55
    >>> sumatoria(19)
    190
    >>> sumatoria(1000000000)
    500000000500000000

    :param num: int el numero hasta donde queremos calcular la sumatoria
    :return: int la suma de todos los digitos hasta el valor
    """
    acum = 0
    for i in range(num + 1):
        acum += i
    return acum