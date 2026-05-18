import copy
from typing import List, Dict

fixtures = {
    "1": [
        {
            "data": [10, 10, 10, 20, 30, 15, 11],
            "answer": 65
        },
        {
            "data": [3,2,6,8,2,3],
            "answer": 17
        },
        {
            "data": [2,1,8,0,6,4,8,6,2,4],
            "answer": 18
        },
        {
            "data": [-7,12,-7,29,-5,0,-7,0,0,29],
            "answer": 41
        },
        {
            "data": [3,3,3,2,1,4],
            "answer": 9
        }
    ],
    "2": [
        {
            "data": "ad",
            "answer": 2
        },
        {
            "data": "abc",
            "answer": 0
        },
        {
            "data": "Hello, World!",
            "answer": 3
        },
        {
            "data": "A-dA",
            "answer": 1
        },
        {
            "data": "zz",
            "answer": 0
        },
        {
            "data": "aabDd-!",
            "answer": 1
        }
    ],
    "3": [
        {
            "data": 9,
            "answer": "Jumping!!"
        },
        {
            "data": 79,
            "answer": "Not!!"
        },
        {
            "data": 23,
            "answer": "Jumping!!"
        },
        {
            "data": 556847,
            "answer": "Not!!"
        },
        {
            "data": 4343456,
            "answer": "Jumping!!"
        },
        {
            "data": 89098,
            "answer": "Not!!"
        },
        {
            "data": 32,
            "answer": "Jumping!!"
        }
    ],
    "4": [
    {
        "data": {
            "name": "my documents",
            "type": "directory",
            "meta": {},
            "children": [
                {
                    "name": "avatar.jpg",
                    "type": "file",
                    "meta": {
                        "size": 100
                    }
                },
                {
                    "name": "photo.jpg",
                    "type": "file",
                    "meta": {
                        "size": 150
                    }
                }
            ]
        },
        "answer": {
            "name": "my documents",
            "type": "directory",
            "meta": {},
            "children": [
                {
                    "name": "avatar.jpg",
                    "type": "file",
                    "meta": {
                        "size": 50
                    }
                },
                {
                    "name": "photo.jpg",
                    "type": "file",
                    "meta": {
                        "size": 75
                    }
                }
            ]
        }
    },
    
    {
        "data": {
            "name": "photo.png",
            "type": "file",
            "meta": {
                "size": 20
            }
        },
        "answer": {
            "name": "photo.png",
            "type": "file",
            "meta": {
                "size": 20
            }
        }
    },

    {
        "data": {
            "name": "username",
            "type": "directory",
            "meta": {},
            "children": [
                {
                    "name": "Desktop",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "profile_pic.png",
                            "type": "file",
                            "meta": {
                                "size": 12
                            },
                        },
                        {
                            "name": "Документ 1.docx",
                            "type": "file",
                            "meta": {
                                "size": 35
                            }
                        }
                    ]
                },
                {
                    "name": "Downloads",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "wallpaper1.webp",
                            "type": "file",
                            "meta": {
                                "size": 4000
                            },
                        },
                        {
                            "name": "Readme.md",
                            "type": "file",
                            "meta": {
                                "size": 120
                            }
                        }
                    ]
                },
                {
                    "name": "Documents",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "Finance.xlsx",
                            "type": "file",
                            "meta": {
                                "size": 600
                            },
                        },
                        {
                            "name": "passport.jpeg",
                            "type": "file",
                            "meta": {
                                "size": 450
                            }
                        }
                    ]
                },
                {
                    "name": "Pictures",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "Wallpapers",
                            "type": "directory",
                            "meta": {},
                            "children": [
                                {
                                    "name": "Безмятежность.jpeg",
                                    "type": "file",
                                    "meta": {
                                        "size": 700
                                    }
                                },
                                {
                                    "name": "Macos_Tahoe.webp",
                                    "type": "file",
                                    "meta": {
                                        "size": 1200
                                    }
                                },
                                {
                                    "name": "wallpaper1.png",
                                    "type": "file",
                                    "meta": {
                                        "size": 300
                                    }
                                },
                            ]
                        },
                        {
                            "name": "Screenshots",
                            "type": "directory",
                            "meta": {},
                            "children": [
                                {
                                    "name": "Screenshot_1.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 200
                                    }
                                },
                                {
                                    "name": "Screenshot_2.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 200
                                    }
                                },
                                {
                                    "name": "Screenshot_3.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 200
                                    }
                                },
                            ]
                        }
                    ]
                },
            ]
        },

        "answer": {
            "name": "username",
            "type": "directory",
            "meta": {},
            "children": [
                {
                    "name": "Desktop",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "profile_pic.png",
                            "type": "file",
                            "meta": {
                                "size": 12
                            },
                        },
                        {
                            "name": "Документ 1.docx",
                            "type": "file",
                            "meta": {
                                "size": 35
                            }
                        }
                    ]
                },
                {
                    "name": "Downloads",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "wallpaper1.webp",
                            "type": "file",
                            "meta": {
                                "size": 4000
                            },
                        },
                        {
                            "name": "Readme.md",
                            "type": "file",
                            "meta": {
                                "size": 120
                            }
                        }
                    ]
                },
                {
                    "name": "Documents",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "Finance.xlsx",
                            "type": "file",
                            "meta": {
                                "size": 600
                            },
                        },
                        {
                            "name": "passport.jpeg",
                            "type": "file",
                            "meta": {
                                "size": 450
                            }
                        }
                    ]
                },
                {
                    "name": "Pictures",
                    "type": "directory",
                    "meta": {},
                    "children": [
                        {
                            "name": "Wallpapers",
                            "type": "directory",
                            "meta": {},
                            "children": [
                                {
                                    "name": "Безмятежность.jpeg",
                                    "type": "file",
                                    "meta": {
                                        "size": 700
                                    }
                                },
                                {
                                    "name": "Macos_Tahoe.webp",
                                    "type": "file",
                                    "meta": {
                                        "size": 1200
                                    }
                                },
                                {
                                    "name": "wallpaper1.png",
                                    "type": "file",
                                    "meta": {
                                        "size": 300
                                    }
                                },
                            ]
                        },
                        {
                            "name": "Screenshots",
                            "type": "directory",
                            "meta": {},
                            "children": [
                                {
                                    "name": "Screenshot_1.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 100
                                    }
                                },
                                {
                                    "name": "Screenshot_2.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 100
                                    }
                                },
                                {
                                    "name": "Screenshot_3.jpg",
                                    "type": "file",
                                    "meta": {
                                        "size": 100
                                    }
                                },
                            ]
                        }
                    ]
                },
            ]
        }
    }
]
}

def check_exrsize(some_func, exersize):
    try:
        for case in fixtures[exersize]:
            result = some_func(case["data"])
            assert result == case["answer"], (
                f"\n Ожидалось: {case['answer']}"
                f"\n Вернулось: {result}" 
                f"\n Данные: {case['data']}"
                )
    except AssertionError as e:
        print(f"Ошбика в задаче {exersize}: {e}")
    else: 
        print(f"Задача {exersize} выполнено успешно")

# -----------------------------------------------------------------------------
# Задача 1
def max_three_sum(numbers: List) -> int:
    return sum(sorted(set(numbers))[-3:])


# Задача 2
def count_lonely_letters(some_string: str) -> int:
    normalize_string = ''.join([letter for letter in some_string.lower() if letter.isalpha()])
    letters_counts = {char: normalize_string.count(char) for char in normalize_string}
    unique_ascii_indexes = [ord(k) for k, v in letters_counts.items() if v == 1]

    lonely_letters_indexes = []

    for i in unique_ascii_indexes:
        prev_number = i - 1 in unique_ascii_indexes
        next_number = i + 1 in unique_ascii_indexes
        if not prev_number and not next_number:
            lonely_letters_indexes.append(i)

    return len(lonely_letters_indexes)


# Задача 3
def is_jumping_number(some_number: int) -> str:
    digits = [int(digit) for digit in str(some_number)]
    return "Jumping!!" if all(abs(digits[i] - digits[i + 1]) == 1 for i in range(len(digits) - 1)) else "Not!!"


# Задача 4
def compress_images(some_tree: Dict) -> Dict:
    copy_tree = copy.deepcopy(some_tree)

    if copy_tree["type"] == "file":
        if copy_tree["name"].endswith((".jpg")):
            copy_tree["meta"]["size"] /= 2
        return copy_tree
    
    if copy_tree["type"] == "directory":
        copy_tree["children"] = [compress_images(child) for child in copy_tree["children"]]
        return copy_tree
    
    return copy_tree

# Задача 5
class Menu:
    def __init__(self, menu=None):
        self.menu = menu or [1, 2, 3]
        self.menu = menu
        self.current = 0

    def to_the_right(self):
        self.current = (self.current + 1) % len(self.menu)

    def to_the_left(self):
        self.current = (self.current - 1) % len(self.menu)

    def display(self):
        return f"[{', '.join(
            [f"[{self.menu[i]}]" \
                if i == self.current else str(self.menu[i]) \
                for i in range(len(self.menu))]
            )}]"

# Проверки
check_exrsize(max_three_sum, "1")
check_exrsize(count_lonely_letters, "2")
check_exrsize(is_jumping_number, "3")
check_exrsize(compress_images, "4")

# Проверка задачи 5
def check_exrsize_5():
    try:
        new_menu = Menu([1, 2, 3])
        assert new_menu.display() == "[[1], 2, 3]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_right()
        assert new_menu.display() == "[1, [2], 3]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_right()
        assert new_menu.display() == "[1, 2, [3]]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_right()
        assert new_menu.display() == "[[1], 2, 3]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_left()
        assert new_menu.display() == "[1, 2, [3]]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_left()
        assert new_menu.display() == "[1, [2], 3]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_left()
        assert new_menu.display() == "[[1], 2, 3]", f"Пришло: {new_menu.display()}"
        new_menu.to_the_left()
        assert new_menu.display() == "[1, 2, [3]]", f"Пришло: {new_menu.display()}"

        some_menu = Menu(['Options', 'Settings', 'Control'])
        assert some_menu.display() == "[[Options], Settings, Control]", f"Пришло: {some_menu.display()}"
        some_menu.to_the_right()
        assert some_menu.display() == "[Options, [Settings], Control]", f"\n Пришло: {some_menu.display()}"
    except AssertionError as e:
        print(f"Ошбика в задаче 5 {e}: ")
    else: 
        print(f"Задача 5 выполнено успешно")

check_exrsize_5()



