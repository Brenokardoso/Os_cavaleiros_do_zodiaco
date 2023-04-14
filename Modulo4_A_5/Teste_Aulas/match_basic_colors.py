from enum import Enum
class Color(Enum):
	RED = "red"
	BLUE = "blue"
	GREEN = "green"
	
color = Color(input("Choice your color"))

print("""match color:
	case Color.RED:
		print(f"I see red")
	case Color.GREEN:
		print(f"I see green")
	case Color.RED:
		print(f"I see the blues""")