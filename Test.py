from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.google.com/search?q=Selenium+WebDriver&sca_esv=0daf534e446e5838&source=hp&ei=jbEIZ7OHHbXZ1sQPlbnQmQE&iflsig=AL9hbdgAAAAAZwi_nQQ2fH2hp7_wIakUB5eN6O0jKHeB&ved=0ahUKEwjzgfS5xoWJAxW1rJUCHZUcNBMQ4dUDCA8&uact=5&oq=Selenium+WebDriver&gs_lp=Egdnd3Mtd2l6IhJTZWxlbml1bSBXZWJEcml2ZXIyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESJnBA1DgjwFYr6sDcAl4AJABAJgBmAKgAdIcqgEGMC4yNC4zuAEDyAEA-AEBmAIkoAKuHagCCsICEBAAGAMY5QIY6gIYjAMYjwHCAhAQLhgDGOUCGOoCGIwDGI8BwgILEAAYgAQYsQMYgwHCAg4QLhiABBixAxiDARiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgILEC4YgAQY0QMYxwHCAggQLhiABBixA8ICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAhQQLhiABBixAxjRAxiDARjHARiKBcICCxAAGIAEGLEDGIoFwgIKEAAYgAQYsQMYCsICBxAAGIAEGArCAgYQABgNGB7CAgYQABgHGB7CAgoQABiABBixAxgNwgIHEAAYgAQYDcICCBAAGAcYChgemAMGkgcGOS4yNC4zoAeR1QE&sclient=gws-wiz')

# Validate the title
expected_title = 'Selenium WebDriver - Google Search'  # Change this to the expected title
actual_title = driver.title

if expected_title == actual_title:
    print('Title validation successful!')
else:
    print('Title validation failed. Expected:', expected_title, 'Actual:', actual_title)

try:
    while True:
        pass  # This will keep the program running
except KeyboardInterrupt:
    print('Closing the browser...')


# Close the browser
driver.quit()