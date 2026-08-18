import numpy as np
import math as m

SEQUENCES = {
    "1/n": {"f": lambda n: 1/n, 
            "L": 0,
            "latex": r"\frac{1}{n}"},

    "3-1/n": {"f": lambda n: 3-1/n, 
              "L": 3,
              "latex": r"3-\frac{1}{n}"},

    "2^n": {"f": lambda n: 2**n, 
            "L": "inf",
            "latex": r"2^n"},

    "sin(n)": {"f": lambda n: np.sin(n), 
               "L": "DNE",
               "latex": r"\sin(n)"},
}

FUNCTIONS = {
    "sin(x)/x": {"f": lambda x: np.sin(x)/x,
                 "a": 0,
                 "L": 1,
                 "hole_x": 0,
                 "latex": r"\frac{\sin(x)}{x}"},
}

DERIVATIVES = {
    "x^2": {"f": lambda x: x**2,
            "a": -3,
            "latex": r"x^2"},

    "e^x": {"f": lambda x: np.exp(x),
            "a": 0,
            "latex": r"e^x"},
            
    "sin(x)": {"f": lambda x: np.sin(x),
               "a": 0,
               "latex": r"\sin(x)"},

    "|x|": {"f": lambda x: np.abs(x),
            "a": 0,
            "latex": r"|x|"},

    "3": {"f": lambda x: 3 + 0*x,
          "a": 2,
          "latex": r"3"},
}

INTEGRATION = {
    "e^x": {"f": lambda x: np.exp(x),
                "domain": (0, 3),
                "latex": r"e^x"},
    
    "sin(x)": {"f": lambda x: np.sin(x),
                "domain": (0, np.pi),
                "latex": r"\sin(x)"},

    "1/x^2": {"f": lambda x: 1/(x**2),
                "domain": (0.5, 5),
                "latex": r"\frac{1}{x^2}"},
}

TAYLOR = { 
    "e^x": {"f": lambda x: np.exp(x), 
            "deriv": lambda k, a: np.exp(a), 
            "a": 0,
            "latex": r"e^x"},

    "sin(x)": {"f": lambda x: np.sin(x), 
               "deriv": lambda k, a: np.sin(a + k*np.pi/2), 
               "a": 0,
               "latex": r"\sin(x)"},

    "1/(1-x)": {"f": lambda x: 1/(1-x), 
                "deriv": lambda k, a: m.factorial(k) / (1-a)**(k+1), 
                "a": 0,
                "latex": r"\frac{1}{1-x}"},

    "x^2": {"f": lambda x: x**2, 
            "deriv": lambda k, a: (a**2 if k == 0 else (2*a if k == 1 else (2 if k == 2 else 0))), 
            "a": 0,
            "latex": r"x^2"}
}