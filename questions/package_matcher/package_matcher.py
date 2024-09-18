# cam game cam -> L: 2 cam, L: game
# Package matcher

# Description

# As the owner of an online store, you need to fulfill orders everyday.
# To optimize the packing of each order, you decide to write an algorithm to match boxes and items based on their respective sizes.
# You have access to the following two boxes:
# - A medium box (identifier: M)
# - A large box (identifier: L)
# When possible, you should try to fit multiple items in the same box but boxes can only contain one type of product.
# This is the list of items you sell along with associated boxes:
# - Camera (identifier: Cam): one can fit in a medium box, and up to two can fit in a large box
# - Gaming Console (identifier: Game): too big for a medium box, but up to two can fit in a large box
# - max of 2 g consoles can fit in 1 box
# - Bluetooth speaker (identifier: Blue): one can fit in a large box . max is 1 per large box
# Your goal is to design a function that takes a list of items and returns the box & item matches (examples below).
# Your solution should work for any number of each item greater than or equal to zero.
# Input = [], Output = []
# ## Input/Output expectations
# ["Cam"] -> [M: ["Cam"]]
# ["Cam", "Game"] -> [M: ["Cam"], L: ["Game"]]
# ["Game", "Blue"] -> [L: ["Game"], L : ["Blue"]]
# ["Game", "Game", "Blue"] -> [L: ["Game", "Game"], L : ["Blue"]]
# ["Cam", "Cam", "Game", "Game"] -> [L: ["Cam", "Cam"], L: ["Game", "Game"]]
# ["Cam", "Cam", "Cam", "Game", "Game", "Game", "Cam", "Blue"] ->
# [L: ["Cam", "Cam"], L: ["Cam", "Cam"], L: ["Game", "Game"], L: ["Game"], L: ["Blue"]]
# ["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"] -> 
# [L: ["Cam", "Cam"] , L: ["Cam", "Cam"] , M: ["Cam"] , L: ["Game", "Game"] , L: ["Blue"] , L: ["Blue"]]

import sys

class PackageMatcher:
    # hash map to hold box capacitys for each product type
    package_capacitys = {
        "M": {
            "Cam": 1,
            "Game": 0,
            "Blue": 0
        },
        "L": {
            "Cam": 2,
            "Game": 2,
            "Blue": 1
        }
    }

    # args: list of items
    # returns: list of objects containing size, and items in pkg
    def package_match(self, items):
        product_counts = {
            "Cam": 0,
            "Game": 0,
            "Blue": 0
        }

        # loop through items and get item counts
        for i in range(len(items)):
            if items[i] == "Cam":
                product_counts["Cam"] += 1
            elif items[i] == "Game":
                product_counts["Game"] += 1
            elif items[i] == "Blue":
                product_counts["Blue"] += 1
        
        packages = []

        for key in product_counts:
            items_in_large_pkg = self.package_capacitys["L"][key]
            items_in_medium_pkg = self.package_capacitys["M"][key]

            # looks at how many large boxes we can fill with the item
            packages += [{"L": [key] * items_in_large_pkg}] * (product_counts[key] // items_in_large_pkg)
            product_counts[key] -= (product_counts[key] // items_in_large_pkg) * items_in_large_pkg

            if (product_counts[key] == 0):
                continue
            # need to use a paritall filled large 
            elif items_in_large_pkg > product_counts[key] and items_in_medium_pkg < product_counts[key]:
                packages += [{"L": [key] * product_counts}]
                continue
            
            # how many med pkgs we can fill with the item
            packages += [{"M": [key] * items_in_medium_pkg}] * (product_counts[key] // items_in_medium_pkg)
            product_counts[key] -= (product_counts[key] // items_in_medium_pkg) * items_in_medium_pkg

            # need to use a partially med filled box
            if (product_counts[key] != 0):
                packages += [{"M": [key] * product_counts[key]}]
        print(packages)
        return packages

if __name__ == "__main__":
    items = sys.argv[1:]
    packager = PackageMatcher()
    packager.package_match(items)
