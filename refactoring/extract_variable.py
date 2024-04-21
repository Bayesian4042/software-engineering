# Problem
## expression that is hard to understand

def renderBanner():
    if (platform.toUpperCase().indexOf("MAC") > -1) and (platform.toUpperCase().indexOf("IE") > -1) and wasInitialized() and resize > 0:
        pass


# Solution

def renderBanner():
    isMacOs = platform.toUpperCase().indexOf("MAC") > -1
    isIEBrowser = platform.toUpperCase().indexOf("IE") > -1
    wasResized = resize > 0

    if isMacOs and isIEBrowser and wasInitialized() and wasResized:
        pass