class Madre:
 def __init__(self):
    print(f"Soy Madre")
class Padre:
 def __init__(self):
    print(f"Soy Padre")
class Hijo(Madre, Padre):
 def __init__(self):
    super().__init__()
    print(f"Soy Hijo")
hijo = Hijo()