// STRICT REPLACEMENT MAP
const replacements = {
    'a': ['@'],
    'i': ['!'],
    's': ['$'],
    'o': ['*'],  
    't': ['+'],
    'c': ['('],
    'b': ['>'], 
    'd': [')'], 
    'k': ['<']  
};

// UI References
const slider = document.getElementById('lengthSlider');
const lengthDisplay = document.getElementById('lengthDisplay');

// Update display and regenerate when slider moves
slider.oninput = function() {
    lengthDisplay.innerText = this.value;
    generatePassword();
}

function generatePassword() {
    const totalLength = parseInt(slider.value);
    const wordLength = (totalLength - 2) / 2;

    const currentList = vocabulary[wordLength];
    if (!currentList) {
        console.error("No word list found for length " + wordLength);
        return;
    }

    let adj = currentList.adj[Math.floor(Math.random() * currentList.adj.length)];
    let noun = currentList.noun[Math.floor(Math.random() * currentList.noun.length)];

    // Calculate ALL valid replacement "moves"
    let validMoves = [];

    // Scan Adj
    for (let i = 0; i < adj.length; i++) {
        if (replacements[adj[i]]) {
            validMoves.push({ word: 'adj', index: i, charToReplace: adj[i] });
        }
    }

    // Scan Noun (Skip index 0 for Capitalization safety)
    for (let i = 1; i < noun.length; i++) {
        if (replacements[noun[i]]) {
            validMoves.push({ word: 'noun', index: i, charToReplace: noun[i] });
        }
    }

    // If absolutely no valid moves exist, retry.
    if (validMoves.length === 0) {
        return generatePassword();
    }

    // Pick random move
    let selectedMove = validMoves[Math.floor(Math.random() * validMoves.length)];
    
    // Determine replacement char
    let possibleNewChars = replacements[selectedMove.charToReplace];
    let finalNewChar = possibleNewChars[Math.floor(Math.random() * possibleNewChars.length)];

    // Apply move
    if (selectedMove.word === 'adj') {
        adj = adj.substring(0, selectedMove.index) + finalNewChar + adj.substring(selectedMove.index + 1);
    } else {
        noun = noun.substring(0, selectedMove.index) + finalNewChar + noun.substring(selectedMove.index + 1);
    }

    // Capitalize Noun
    noun = noun.charAt(0).toUpperCase() + noun.slice(1);

    // Generate Numbers (No doubles)
    let n1 = Math.floor(Math.random() * 10);
    let n2 = Math.floor(Math.random() * 10);
    while (n1 === n2) {
        n2 = Math.floor(Math.random() * 10);
    }
    let numStr = n1.toString() + n2.toString();

    let finalPassword = adj + noun + numStr;
    document.getElementById("passwordOutput").innerText = finalPassword;
}

function copyPassword() {
    const text = document.getElementById("passwordOutput").innerText;
    if(!text) return;
    
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalText = btn.innerText;
        btn.innerText = "Copied to clipboard!";
        btn.style.color = "var(--italian-red)";
        setTimeout(() => {
            btn.innerText = originalText;
            btn.style.color = "";
        }, 2000);
    });
}

// Init
generatePassword();