from Utilities.Common_ops import *
from Utilities.verifications import *


def test01_dynamic_id(driver):
    driver.get('http://uitestingplayground.com/dynamicid')
    btn = driver.find_element(By.XPATH, "//div[@class='container']/Button")
    verifai_txt("Button with Dynamic ID", btn.text)


def test02_class_attr(driver):
    driver.get('http://uitestingplayground.com/classattr')
    expected = "Primary button pressed"
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alr = driver.switch_to.alert
    result = alr.text
    alr.accept()
    verifai_txt(expected, result)


def test03_hidden_layers(driver):
    driver.get('http://uitestingplayground.com/hiddenlayers')
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        pytest.fail("Green Button not supposed to Be Hit Twice!")
        screenshot("Green Button not supposed to Be Hit Twice!")
    except Exception:
        print("Green Button Can not Be Hit Twice!")
        pass


def test04_load_delay(driver):
    driver.get('http://uitestingplayground.com/')
    expected = "http://uitestingplayground.com/loaddelay"
    driver.find_element(By.LINK_TEXT, "Load Delay").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    result = driver.current_url
    verifai_txt(expected, result)


def test05_AJAX_Data(driver):
    driver.get('http://uitestingplayground.com/ajax')
    expected = "Data loaded with AJAX get request."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    verifai_txt(expected, result)


def test06_client_side_delay(driver):
    driver.get('http://uitestingplayground.com/clientdelay')
    expected = "Data calculated on the client side."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    verifai_txt(expected, result)


def test07_click(driver):
    driver.get('http://uitestingplayground.com/click')
    expected = "btn btn-success"
    button = driver.find_element(By.ID, "badButton")
    action.move_to_element(button).click().perform()
    result = button.get_attribute("class")
    verifai_txt(expected, result)


def test08_text_input(driver):
    driver.get('http://uitestingplayground.com/textinput')
    expected = "Almog Noach"
    driver.find_element(By.ID, "newButtonName").send_keys(expected)
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    result = button.text
    verifai_txt(expected, result)


def test09_scrollbars(driver):
    driver.get('http://uitestingplayground.com/scrollbars')
    expected = "Hiding Button"
    hiding_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    driver.execute_script("arguments[0].scrollIntoView(true);", hiding_btn)
    result = hiding_btn.text
    verifai_txt(expected, result)


def test10_dynamic_table(driver):
    driver.get('http://uitestingplayground.com/DynamicTable')
    expected = driver.find_element(By.CLASS_NAME, "bg-warning").text.split(": ")[1]
    columns = driver.find_elements(By.XPATH, "//span[@role='columnheader']")
    cells = driver.find_elements(By.XPATH, "//span[@role='cell']")
    result, x, y = "0", 0, 0
    for colum in columns:
        if colum.text == "CPU":
            break
        else:
            x = x + 1
    for cell in cells:
        if cell.text == "Chrome":
            y = y + x
            break
        else:
            y = y + 1
    result = cells[y].text
    verifai_txt(expected, result)


def test11_verify_text(driver):
    driver.get('http://uitestingplayground.com/verifytext')
    expected = "Welcome UserName!"
    result = driver.find_element(By.XPATH, "//span[normalize-space(.)='Welcome UserName!']").text
    verifai_txt(expected, result)


def test12_progressbar(driver):
    driver.get('http://uitestingplayground.com/progressbar')
    expected = "75%"
    start_btn = driver.find_element(By.ID, "startButton")
    stop_btn = driver.find_element(By.ID, "stopButton")
    progress_bar = driver.find_element(By.ID, "progressBar")
    start_btn.click()
    now = progress_bar.text
    while now != "75%":
        now = progress_bar.text
    stop_btn.click()
    result = progress_bar.text
    verifai_txt(expected, result)


def test13_visibility(driver):
    driver.get('http://uitestingplayground.com/visibility')
    hide_btn = driver.find_element(By.ID, "hideButton")
    buttons = driver.find_elements(By.XPATH, "//button[@type=\"button\"]")

    # Create a list of buttons id names
    visible_btn_id = []
    for btn in buttons:
        visible_btn_id.append(btn.get_attribute("id"))

    # Click on Hide Button
    hide_btn.click()
    buttons = driver.find_elements(By.XPATH, "//button[@type=\"button\"]")

    # Create a new list of buttons id names after hide_btn click
    new_btn_id = []
    for btn in buttons:
        new_btn_id.append(btn.get_attribute("id"))
    hide_btn.click()

    # Checking if The Button Exist
    for btn in visible_btn_id:
        try:
            x = new_btn_id.index(btn)
            print(str(x) + ". " + btn + " fond but not visible")
        except ValueError:
            print(str(x) + ". " + btn + "  not fond")

    expected = 8
    result = len(buttons)
    verifai_txt(expected, result)


def test14_sample_app(driver):
    driver.get('http://uitestingplayground.com/SampleApp')
    # Elements
    user_name_txt = driver.find_element(By.NAME, "UserName")
    password_txt = driver.find_element(By.NAME, "Password")
    login_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    login_status = driver.find_element(By.ID, "loginstatus")

    # User Info
    user_name = "Almog81"
    password = "pwd"

    # Login Test
    expected = "Welcome, " + user_name + "!"
    user_name_txt.send_keys(user_name)
    password_txt.send_keys(password)
    login_btn.click()
    result = login_status.text
    verifai_txt(expected, result)


def test15_mouseover(driver):
    driver.get('http://uitestingplayground.com/mouseover')
    expected = "2"
    click_me = driver.find_element(By.LINK_TEXT, "Click me")
    action.move_to_element(click_me).click().click().perform()
    result = driver.find_element(By.ID, "clickCount").text
    verifai_txt(expected, result)


def test16_non_breaking_space(driver):
    driver.get('http://uitestingplayground.com/nbsp')
    expected = "My Button"
    btn = driver.find_element(By.XPATH, "//button[text()='My\u00A0Button']")
    btn.click()
    result = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").text
    verifai_txt(expected, result)


def test17_overlapped_element(driver):
    driver.get('http://uitestingplayground.com/overlapped')
    expected = "Subject"

    # Element
    id = driver.find_element(By.ID, "id")
    name = driver.find_element(By.ID, "name")
    subject = driver.find_element(By.ID, "subject")

    # Actions
    driver.execute_script("arguments[0].scrollIntoView(true);", id)
    id.send_keys("123456789")
    driver.execute_script("arguments[0].scrollIntoView(true);", name)
    name.send_keys("Almog Noach")
    driver.execute_script("arguments[0].scrollIntoView(true);", subject)
    subject.send_keys("Subject name: kuku")

    # Assert
    result = subject.accessible_name
    verifai_txt(expected, result)


def test18_shadow_dom(driver):
    driver.get('http://uitestingplayground.com/shadowdom')
    # Element
    s_dom = driver.find_element(By.XPATH, "//div[@class='container']/guid-generator")
    generate_btn = s_dom.shadow_root.find_element(By.ID, "buttonGenerate")
    copy_btn = s_dom.shadow_root.find_element(By.ID, "buttonCopy")
    edit_field = s_dom.shadow_root.find_element(By.ID, "editField")

    # Action
    generate_btn.click()
    copy_btn.click() # This button does not work on the Online Web,so we will do our own copy operation:
    pyperclip.copy(edit_field.text)
    expected = pyperclip.paste()

    # Assert
    result = edit_field.text
    verifai_txt(expected, result)