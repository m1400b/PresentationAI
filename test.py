from src.models.elements import TextElement, ImageElement

t = TextElement(
    text="Hello PresentationAI"
)

i = ImageElement(
    path="test.png"
)

print(t)
print(i)