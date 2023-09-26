import cssutils

# Create a new CSS stylesheet
stylesheet = cssutils.parseString('''
    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: blue;
    }
''')

# Modify the background color of the body element
body = stylesheet.cssRules[0].style
body.setProperty('background-color', '#ffffff')

# Output the modified CSS
print(stylesheet.cssText)
