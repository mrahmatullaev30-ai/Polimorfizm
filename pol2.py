class Convertor:
    def __init__(self):
    
        self.rules = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ю': 'Yu', 'Я': 'Ya'
        }

        self.rev_rules = {v: k for k, v in self.rules.items() if v != ''}

    def ru_to_en(self, text):
        res = ""
        for char in text:
        
            res += self.rules.get(char, char)
        return res

    def en_to_ru(self, text):

        sorted_keys = sorted(self.rev_rules.keys(), key=len, reverse=True)
        
        res = text
        for key in sorted_keys:
            res = res.replace(key, self.rev_rules[key])
        return res


conv = Convertor()

text_ru = "Салом дунё"
converted_en = conv.ru_to_en(text_ru)
print(f"RU -> EN: {converted_en}") 

text_en = "Salom dunyo"
converted_ru = conv.en_to_ru(text_en)
print(f"EN -> RU: {converted_ru}")


print(conv.ru_to_en("Юлдуз Яйра Ёдгор")) 
print(conv.en_to_ru("Yulduz Yayra Yodgor")) 
