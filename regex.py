import re

raw_text = """
<div>
<span class="actionBar__text"> Showing 18 of 101
products.
</span>
</div>
"""


def find_total(raw_text):
    result = -1
    regex = "Showing\s+\d+\s+of\s+(?P<total>\d+)\s+products?"
    match = re.search(regex,raw_text)

    if match:
        result = int(match.group("total"))
        # print(f"Total number of products is {result}")
    # else:
    #     print("Total number of products not found.")

    return result
    


total = find_total(raw_text)
print(total)


def test_regex():
    raw_text1 = """<div><span class="actionBar__text"> Showing  of  products.</span></div>"""
    raw_text2 = """<div><span class="actionBar__text"> Showing 20 of 200 products.</span></div>"""
    raw_text3 = """<div><span class="actionBar__text"> Showing 1 of 1 product.</span></div>"""
    
    print(find_total(raw_text1) == -1)
    print(find_total(raw_text2) == 200)
    print(find_total(raw_text3) == 1)

test_regex()