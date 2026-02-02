class String:
    def __init__(self, text):
        self.text = text
    def to_lower(self):
        result = ""
        for char in self.text:
            char_code = ord(char)
            if ord('A') <= char_code <= ord('Z'):
                result += chr(char_code + 32)
            else:
                result += char
        return String(result) 

    def to_upper(self):
        result = ""
        for char in self.text:
            char_code = ord(char)
            if ord('a') <= char_code <= ord('z'):
                result += chr(char_code - 32)
            else:
                result += char
        return String(result) 

    def is_lower(self):
        for char in self.text:
            char_code = ord(char)

            if ord('A') <= char_code <= ord('Z'):
                return False
        return True

    def is_upper(self):
        for char in self.text:
            char_code = ord(char)
            if ord('a') <= char_code <= ord('z'):
                return False
           
        return True
    
    def __repr__(self):
        return self.text

s1 = String("Hello World 123!")
s2 = String("PYTHON")

print(f"Asl matn: {s1}")
print(f"to_upper: {s1.to_upper()}")
print(f"to_lower: {s1.to_lower()}")
print(f"is_upper('Hello World'): {s1.is_upper()}")
print(f"is_upper('PYTHON'): {s2.is_upper()}")
print(f"is_lower('Hello World'): {s1.is_lower()}")
print(f"is_lower('hello world'): {s1.to_lower().is_lower()}")