function addStyleSheets(styles) {
    const head = document.querySelector('head');

    for (let style of styles) {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = style;
        head.append(link);
    }
}

function addScripts(scripts) {
    const body = document.querySelector('head');

    for (let script of scripts) {
        const scriptEl = document.createElement('script');
        scriptEl.type = 'text/javascript';
        scriptEl.src = script
        body.append(scriptEl);
    }
}

async function sleep(s) {
    return new Promise(resolve => setTimeout(resolve, s * 1000));
}

async function startLoading(time) {
    const loadingScreen = document.createElement('div');
    loadingScreen.style.width = '100%';
    loadingScreen.style.height = '100%';
    loadingScreen.style.position = 'absolute';
    loadingScreen.style.top = '0';
    loadingScreen.style.left = '0';
    loadingScreen.style.zIndex = '1001';
    loadingScreen.style.background = 'black';

    let interval = 0.5,
        curTime = 0;

    loadingScreen.style.transition = `background ${interval}s`;

    const body = document.querySelector('body');
    body.appendChild(loadingScreen);
    body.style.overflow = 'hidden';

    while (curTime < time) {
        let h, s, l;
        h = Math.floor(Math.random() * 360);
        s = Math.floor(Math.random() * 100);
        l = Math.floor(Math.random() * 100);

        loadingScreen.style.background = `hsl(${h}, ${s}%, ${l}%)`
        await sleep(interval);

        curTime += interval;
    }
}

const scripts = [
    'https://anubhav-kaushik.github.io/tab-addons/widget-tab-type.js',
    'https://anubhav-kaushik.github.io/quiz-creator/js/action.js',
    'https://anubhav-kaushik.github.io/quiz-creator/js/quiz-creator.js',
    'https://anubhav-kaushik.github.io/marksCalc/tcs-marks-calc.js',
];

const styleSheets = [
    'https://anubhav-kaushik.github.io/tab-addons/widget-tab-type.css',
    'https://anubhav-kaushik.github.io/quiz-creator/css/quiz-style.css',
    'https://anubhav-kaushik.github.io/marksCalc/style.css',
    'https://anubhav-kaushik.github.io/create-table/css/style.css',
]

addStyleSheets(styleSheets);
addScripts(scripts);

function backlink(href) {
    const linkBlock = document.createElement('a');
    linkBlock.innerHTML = `Home`
    linkBlock.setAttribute('href', href);

    linkBlock.style.position = 'absolute';
    linkBlock.style.right = '2rem';
    linkBlock.style.top = '1rem';
    linkBlock.style.fontSize = '1rem';
    linkBlock.style.fontWeight = 'bold';
    linkBlock.style.cursor = 'pointer';
    linkBlock.style.color = 'white';
    linkBlock.style.textDecoration = 'none';

    return linkBlock;
}

function signature() {
    const signature = document.createElement('a');
    signature.innerHTML = `created by <span id="creator" class="handwritten">Anubhav Sharma</span>`
    signature.setAttribute('href', '');

    signature.style.position = 'absolute';
    signature.style.right = '45%';
    signature.style.top = '1rem';
    signature.style.fontSize = '1rem';
    signature.style.fontWeight = 'bold';
    signature.style.cursor = 'pointer';
    signature.style.color = 'white';
    signature.style.textDecoration = 'none';

    return signature;
}

async function run(tier) {
    await sleep(1.5);
    const result = main(page, '.section-cntnr', '.section-lbl', '.rw', markingScheme, tier);

    const mainBody = document.querySelector('body');
    mainBody.innerHTML = initialTabBlock().outerHTML;
    mainBody.append(backlink('/'))

    const finalData = {
        'Quiz': createQuiz(result['answerKeyDict'], `${result['candidateInfo']['Exam Date']} - ${result['candidateInfo']['Exam Time']}`)
    }

    addTabs(finalData, '.tabs-widget .tabs', '.tabs-widget .tabs-content')
    
}


