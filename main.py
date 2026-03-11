import os
from convertor import convertor
from InquirerPy import inquirer
from InquirerPy.base.control import Choice, Separator

current_dir = os.path.dirname(os.path.realpath(__file__))

images = []

for file in os.listdir(current_dir):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        full_path = os.path.join(current_dir, file)
        images.append(full_path)
print("********************WEBP CONVERTOR**********************\n")
for img in images:
    print(os.path.basename(img))
if len(images) == 0:
    print("No images in directory")
    exit()
print(f"\n{len(images)} images found\n")
input("Press any key to continue...")

selected_size = inquirer.select(
    message="Choose the size:",
    choices=[
        "360x640",
        "375x667",
        "390x844",
        "393x873",
        "412x915",
        "414x896",
        "640x360",
        "640x480",
        "768x1024",
        "800x600",
        "800x1200",
        "1024x768",
        "1024x1366",
        "1080x1080",
        "1080x1350",
        "1080x1920",
        "1200x630",
        "1200x800",
        "1200x1200",
        "1280x720",
        "1280x800",
        "1366x768",
        "1440x900",
        "1536x864",
        "1600x900",
        "1920x1080",
        "2560x1440",
        "3840x2160",
        Separator(),
        Choice(value="original", name="Original size"),
        Choice(value="custom", name="Custom size"),
        Choice(value="exit", name="Exit"),
    ],
    default="640x480",
    pointer="==> ",
    qmark="*",                        # можно поменять иконку вопроса
).execute()

if selected_size == "custom":
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    print(f"Selected size: {width}×{height}")
    input("Press any key to start converting...")
    convertor(images, current_dir, size=(width, height))
elif selected_size == "exit":
    exit()
elif selected_size == "original":
    print("Selected size: original")
    input("Press any key to start converting...")
    convertor(images, current_dir, size=None)
else:
    width, height = map(int, selected_size.split("x"))
    print(f"Selected size: {width}×{height}")
    input("Press any key to start converting...")
    convertor(images, current_dir, size=(width, height))