function css(element, style) {
    for (const property in style)
        element.style[property] = style[property];
}

function conditionalStyling(elementSelector, elementContain, ifTrue, ifFalse) {
    const elements = document.querySelectorAll(elementSelector);

    for (let element of elements) {
        const nodes = element.childNodes;
        let containsNode = false;

        for (let node of nodes) {
            if (node.nodeType === 1) {
                if (node.nodeName.toLowerCase() === elementContain.toLowerCase()) {
                    css(element, ifTrue);
                    containsNode = true;
                } 
            }
        }

        if (!containsNode) {
            css(element, ifFalse);
        }
    }
}

function conditionalStylingOnHover(elementSelector, elementContain, ifTrue, ifFalse, defaultStyle) {
    const elements = document.querySelectorAll(elementSelector);

    for (let element of elements) {
        const nodes = element.childNodes;
        let containsNode = false;

        for (let node of nodes) {
            if (node.nodeType === 1) {
                if (node.nodeName.toLowerCase() === elementContain.toLowerCase()) {
                    element.onmouseenter =  () => {
                        console.log('Enter')
                        css(element, ifTrue)
                    }
                    element.onmouseleave =  () => {
                        console.log('Leave')
                        css(element, defaultStyle)
                    }
                    containsNode = true;
                } 
            }
        }

        if (!containsNode) {
            element.onmouseenter =  () => {
                console.log('Enter')
                css(element, ifFalse)
            }
            element.onmouseleave =  () => {
                console.log('Leave')
                css(element, defaultStyle)
            }
        }
    }
}
