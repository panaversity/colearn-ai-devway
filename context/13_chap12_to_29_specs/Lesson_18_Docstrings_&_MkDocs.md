# Lesson 18 Docstrings & MkDocs

<font color="#a9a56c" size=2> **@Author: Arif Kasim Rozani - (Team Operation Badar)** </font>




“It doesn’t matter how good your software is, because  **if the documentation is not good enough, people will not use it.**“

—  _[Daniele Procida](https://www.divio.com/en/blog/documentation/)_


---
Reading Resources:

1. [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)

2. [Python Docstrings](https://www.geeksforgeeks.org/python-docstrings/)
---



# **Docstrings in Python (Simple Explanation! 📖)**

**Docstrings** are **strings inside a function/class/module** that explain what it does. They act like built-in documentation.

#### **Key Features:**

-   Written as a **multi-line string (`"""..."""` or `'''...'''`)** right after the definition.
-   Accessible via `help()` or `.__doc__`.
-   Used by tools like **Sphinx** for auto-generating docs.

----------

### **1️⃣ Basic Syntax**

```python
def greet(name):
    """
      def greet(name):
        This function greets the user.

         print(f"Hello, {name}!")
    """  # <-- Docstring

    print(f"Hello, {name}!")

# Access the docstring:
print("greet.__doc__ = ", greet.__doc__)  # Output: "This function greets the user."
print("\nhelp() = ")
help(greet)           # Shows the docstring in help()
```

**Output:**
```
greet.__doc__ =  
      def greet(name):
        This function greets the user.     

         print(f"Hello, {name}!")            
    

help() = 
Help on function greet in module __main__:

greet(name)
    def greet(name):
      This function greets the user.     
    
       print(f"Hello, {name}!")

```

----------

### **3️⃣ Common Formats**

| Format        | Used By                | Example            |   |
|---------------|------------------------|--------------------|---|
| Google Style  | Popular in open-source | Google Style Guide |   |
| NumPy Style   | Scientific Python      | NumPy Docs         |   |
| reST (Sphinx) | Official Python docs   | PEP 287            |   |

1.  [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
2.  [NumPy Docs](https://numpydoc.readthedocs.io/en/latest/format.html)
3.  [PEP 287](https://peps.python.org/pep-0287/)


----------

### **4️⃣ Where to Use Docstrings?**

✔ **Functions**  
✔ **Methods**
✔ **Classes**  
✔ **Modules** (at the top of the file)  
✔ **Package** (at the top of the file)



## **Example: Class-level docstring**

```python
class Dog:
    """A class representing a dog."""

    def bark(self):
        """Makes the dog bark."""
        print("Woof!")
```


## **Package and Module Docstrings**

**`Package docstrings should be placed at the top of the package’s  __init__.py file.`** This docstring should list the modules and sub-packages that are exported by the package.

Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. **`Module docstrings are placed at the top of the file even before any imports.`**

## **Example: Module-level docstring**

```python
# Example: Module-level docstring
"""
This module provides math operations.
- add(a, b): Adds two numbers.
- divide(a, b): Divides two numbers.
"""
```


----------

### **🎯 Key Takeaway**

Docstrings = **Human-readable docs** for your code. Always write them to make your code **easier to understand and maintain!** 🚀

# **Example: Module-level docstring**
"""
<br>

This module provides math operations.
- add(a, b): Adds two numbers.
- divide(a, b): Divides two numbers.

<br>
"""

**Module docstrings must be the first statement in the file (right after imports).**


## **How to Access a Module-Level Docstring in Python**

To access the docstring of a **module** (defined at the top of a `.py` file), use either:

#### **Method 1: `__doc__` Attribute**

```python
import math  # Replace with your module name

print(math.__doc__)
```

**Output:**
```
This module provides access to the mathematical functions
defined by the C standard.
```

```python
help(math)
```

**Output:**
```
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    cbrt(x, /)
        Return the cube root of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    exp2(x, /)
        Return 2 raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(n, /)
        Find n!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    lcm(*integers)
        Least Common Multiple.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    nextafter(x, y, /)
        Return the next floating-point value after x towards y.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.
    
    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


```



---


# **Comprehensive MkDocs Tutorial: Build Beautiful Documentation**

- [MkDocs - Project documentation with Markdown](https://www.mkdocs.org/user-guide/)

- [Getting Started with MkDocs](https://www.mkdocs.org/getting-started/)

<br>
MkDocs is a **static site generator** that turns Markdown files into a professional documentation website. It's lightweight, customizable, and perfect for **developers, technical writers, and open-source projects**.

----------

## **📌 Table of Contents**

1.  Installation
2.  Project Setup
3.  Writing Content
4.  Customizing with Themes
5.  Navigation & Structure
6.  Adding Plugins
7.  Search Functionality
8.  Deployment
9.  Advanced Features

----------

## **1️⃣ Installation** <a name="installation"></a>



```bash
pip install mkdocs  # Basic installation
pip install mkdocs-material  # Install Material theme (recommended)

```

Verify installation:



```bash
mkdocs --version

```

----------

## **2️⃣ Project Setup** <a name="project-setup"></a>

### **Create a new project**



```bash
mkdocs new my-docs
cd my-docs

```

### **Folder Structure**



```
my-docs/
├── docs/          # Markdown files go here
│   └── index.md   # Homepage
└── mkdocs.yml     # Configuration file

```

### **Start the Development Server**


```bash
mkdocs serve

```

Visit: `http://localhost:8000`

----------

## **3️⃣ Writing Content** <a name="writing-content"></a>

### **Basic Markdown Syntax**



```markdown
# Header 1
## Header 2
### Header 3

- Bullet points
- Another point

1. Numbered list
2. Second item

**Bold text**, *italic text*, `code snippet`

[Link](https://example.com)

```

### **Code Blocks**



```python
def hello():
    print("Hello, MkDocs!")
```



### **Admonitions (Callouts)**





```markdown
!!! note "Note"
    This is a note.

```

Supported types:

-   `note`, `warning`, `danger`, `tip`, `info`

----------

## **4️⃣ Customizing with Themes** <a name="themes"></a>

### **Popular Themes**

| Theme       | Command                         |   |   |
|-------------|---------------------------------|---|---|
| Material    | pip install mkdocs-material     |   |   |
| ReadTheDocs | pip install mkdocs-rtd-dropdown |   |   |
| Windmill    | pip install mkdocs-windmill     |   |   |


### **Configure in `mkdocs.yml`**

```yaml
theme:
  name: material  # Material theme (recommended)
  features:
    - navigation.tabs
    - search.highlight

```

----------

## **5️⃣ Navigation & Structure** <a name="navigation"></a>

### **Basic Navigation** (`mkdocs.yml`)

```yaml
nav:
  - Home: index.md
  - User Guide:
      - Installation: guide/install.md
      - Usage: guide/usage.md
  - API Reference: api.md

```

### **Multi-Level Navigation**

```yaml
nav:
  - Getting Started:
      - Introduction: intro.md
      - Quick Start: quickstart.md
  - Advanced:
      - Configuration: advanced/config.md
      - Deployment: advanced/deploy.md

```

----------

## **6️⃣ Adding Plugins** <a name="plugins"></a>

### **Install a Plugin**

```bash
pip install mkdocs-awesome-pages

```

### **Enable in `mkdocs.yml`**

```yaml
plugins:
  - search  # Built-in search
  - awesome-pages  # Auto-generates navigation

```

### **Popular Plugins**

| Plugin                   | Purpose                     |   |   |
|--------------------------|-----------------------------|---|---|
| mkdocs-minify            | Minifies HTML/CSS/JS        |   |   |
| mkdocs-git-revision-date | Adds last update timestamps |   |   |
| mkdocs-pdf-export        | Exports docs as PDF         |   |   |


----------

## **7️⃣ Search Functionality** <a name="search"></a>

MkDocs has **built-in search** (powered by Lunr.js).

### **Enable Search** (`mkdocs.yml`)

```yaml
plugins:
  - search

```

### **Custom Search Options**

```yaml
plugins:
  - search:
      lang: en
      separator: '[\s\-]+'

```

----------

## **8️⃣ Deployment** <a name="deployment"></a>

### **Option 1: GitHub Pages (Free)**

```bash
mkdocs gh-deploy

```

→ Pushes to `gh-pages` branch.

### **Option 2: Netlify/Vercel**

-   Drag-and-drop the `site/` folder (generated by `mkdocs build`).

### **Option 3: Self-Hosted (Nginx/Apache)**

```bash
mkdocs build  # Generates static files in `site/`

```

Upload `site/` to your server.

----------

## **9️⃣ Advanced Features** <a name="advanced"></a>

### **Custom CSS/JS**

```yaml
extra_css:
  - stylesheets/custom.css
extra_javascript:
  - js/custom.js

```

### **Versioning Docs**

```yaml
extra:
  version: 1.0.0

```

### **Multi-Language Support**

```bash
pip install mkdocs-static-i18n

```

----------

## **🚀 Final `mkdocs.yml` Example**

```yaml
site_name: My Project Docs
theme:
  name: material
  features:
    - navigation.tabs
    - search.highlight
nav:
  - Home: index.md
  - Guide:
      - Installation: guide/install.md
      - Usage: guide/usage.md
  - API: api.md
plugins:
  - search
  - awesome-pages

```

----------

## **✅ Summary**

✔ **Write docs in Markdown** (`.md` files).  
✔ **Live preview** with `mkdocs serve`.  
✔ **Customizable themes & plugins**.  
✔ **Deploy for free** (GitHub Pages, Netlify).

### **Get Started Now!**

```bash
pip install mkdocs mkdocs-material
mkdocs new my-docs
mkdocs serve

```

**Perfect for:**  
📜 API Documentation  
📖 Open-Source Projects  
🔧 Internal Team Wikis

