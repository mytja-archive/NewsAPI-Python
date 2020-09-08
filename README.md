# NewsAPI-Python
Super simple Python NewsAPI wrapper

This library is based in pure Python, and it doesn't need any external libraries

# Inner workings
1. It gets JSON data from NewsAPI
2. It parses it, to Python text data
3. Rearanges it
4. Converts it back to JSON

# Issues
1. This library gives another [] since its variables were saved in a list. Although, gTTS doesn't bother those extra stuff, so it's okay.

# Get it working!
First, you'll have to initialize getAPI function like this:
```
getAPI("my-api-token")
```

Then, you have 2 functions. One is getNews(), and other is headlines()

If you see any strange stuff, then report it.

# Supports Python 2 and Python 3
