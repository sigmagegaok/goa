def introduce_yourself(name, surname, age, country, city, hobby):
    introduction = (
        f"გამარჯობა! მე ვარ {name} {surname}, {age} წლის. ვცხოვრობ {country}-ში, ქალაქ {city}-ში. "
        f"ჩემი საყვარელი ჰობია {hobby}. მიხარია, რომ გიამბობთ ჩემს თავზე!"
    )
    return introduction

info = introduce_yourself("ნინო", "ჯაფარიძე", 25, "საქართველო", "თბილისი", "ცეკვა")
print(info)
