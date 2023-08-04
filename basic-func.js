async function sleep(s) {
    return new Promise(resolve => setTimeout(resolve, s * 1000));
}

function reachIntoView(elementSelector) {
    const element = document.querySelector(elementSelector);

    options = {
        behaviour: 'smooth',
        block: 'center',
        inline: 'center'
    }

    element.scrollIntoView(options)
}

function hyperlinkTo(href, newWindow=false) {
    let baseUrl = window.location.href;
    
    if (baseUrl.endsWith('index.html')) {
        baseUrl = baseUrl.replace('index.html', '');
    }
    const url = baseUrl + href;

    if (newWindow) {
        return window.open(url, '_blank');
    } else {
        return window.open(url, '_self');
    }
}

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.substring(1);
}

function isIn(key, array) {
    for (let element of array) {
        if (key == element) {
            return true;
        }
    }

    return false;
}