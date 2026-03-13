#dictionary store data in key value pair, it is similar to object in javascript

dictionary_english_vietname = {
    "hello": "xin chao",
    "goodbye": "tam biet",
    "thank you": "cam on"
}

print(dictionary_english_vietname["hello"])
#get value from dictionary by key
print(dictionary_english_vietname.get("a", "key not found"))

print(dictionary_english_vietname.pop("goodbye"))

print(dictionary_english_vietname.popitem())

#dictionary use to store data in key value pair, it is similar to object in javascript