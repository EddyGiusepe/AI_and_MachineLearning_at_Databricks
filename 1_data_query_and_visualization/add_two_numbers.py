#! /usr/bin/env python
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Script soma_dois_numbers.py
===========================
Este script é usado para somar dois números reais
e retornar o resultado.
"""


def soma_dois_numbers(a: float, b: float) -> float:
    """Realiza a soma de dois números reais.
    
    Esta função recebe dois números de ponto flutuante e retorna
    a soma aritmética entre eles.
    
    Args:
        a (float): Primeiro número real a ser somado.
        b (float): Segundo número real a ser somado.
    
    Returns:
        float: O resultado da soma de a + b.
    
    Examples:
        >>> soma_dois_numbers(1.5, 2.5)
        4.0
        
        >>> soma_dois_numbers(10.0, -5.5)
        4.5
        
        >>> soma_dois_numbers(0.0, 0.0)
        0.0
    """
    return a + b


if __name__ == "__main__":
    print(soma_dois_numbers(1.5, 2.5))
