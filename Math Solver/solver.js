function triggerUpload() {
    document.getElementById('file-input').click();
}

function showInputSection() {
    const inputSection = document.getElementById('input-section');
    const equationText = document.getElementById('equation-text');
    if (inputSection.style.display === 'flex') {
        inputSection.style.display = 'none';
        document.getElementById('result-box').innerHTML = ``;
    } else {
        inputSection.style.display = 'flex';
        equationText.focus();
    }
}

function solveEquation() {
    const equationText = document.getElementById('equation-text');
    const resultBox = document.getElementById('result-box');
    
    let equation = equationText.value.trim().replace(/(\d+)([a-zA-Z])/g, '$1*$2');
    if (equation === "") {
        alert("Please type an equation first!");
        return;
    }
    let result = "";
    try {
        if (equation.includes('=')) {
            // Nerdamer solves equations directly by calling nerdamer.solve(equation, variable)
            // It will output answers as clean fractions or arrays if multiple roots exist
            let solutions = nerdamer.solve(equation, 'x');
            result = `x = ${solutions.toString()}`;
        } 
        else {
            try {
                result = math.evaluate(equation);
            } catch {
                result = nerdamer(equation).evaluate().toString();
            }
        }
        resultBox.innerHTML = `<p style="margin-top: 15px; font-weight: bold; color: #10b981;">Result: ${result}</p>`;
    } catch (error) {
        console.error(error);
        resultBox.innerHTML = `<p style="margin-top: 15px; color: #ef4444;">Error: Nerdamer could not parse expression. Check your equation format.</p>`;
    }
}

document.getElementById('file-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const resultBox = document.getElementById('result-box');
    const equationText = document.getElementById('equation-text');
    const inputSection = document.getElementById('input-section');    
    if (file) {
        resultBox.innerHTML = `<p style="margin-top: 15px; color: #4f46e5;">Analysing image to extract question...</p>`;
        inputSection.style.display = 'flex';
        Tesseract.recognize(file, 'eng', { 
            logger: m => console.log(m) 
        }).then(({ data: { text } }) => {
            let cleanedText = text.replace(/\s+/g, ' ').trim();
            if (cleanedText === "") {
                resultBox.innerHTML = `<p style="margin-top: 15px; color: #ef4444;">Could not detect any text in the image.</p>`;
            } else {
                equationText.value = cleanedText;
                resultBox.innerHTML = `<p style="margin-top: 15px; color: #10b981;">Image processed successfully! Review the text above and click Solve.</p>`;
            }
        }).catch(error => {
            console.error(error);
            resultBox.innerHTML = `<p style="margin-top: 15px; color: #ef4444;">Error processing image.</p>`;
        });
    }
});