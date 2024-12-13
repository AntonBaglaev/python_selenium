import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
    x_selector1 = """//*[@id='login']/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id='login']/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

test_step1()

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))