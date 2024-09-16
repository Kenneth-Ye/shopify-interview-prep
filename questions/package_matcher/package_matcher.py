# cam game cam -> L: 2 cam, L: game
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
