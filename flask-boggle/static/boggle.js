async function submitWord() {
    try {
        const word = $("#wordInput").val();
        const response = await axios.post('/submit-word', { word: word });

        // Handle the JSON response from the server
        const result = response.data.result;
        displayResultMessage(result);
    } catch (error) {
        console.error(error);
    }
}

function displayResultMessage(result) {
    // Update the UI to display the result message
    const resultContainer = $("#resultContainer");
    if (result === 'ok') {
        resultContainer.text('The word is valid and exists on the board!');
    } else if (result === 'not-on-board') {
        resultContainer.text('The word is valid but does not exist on the board.');
    } else if (result === 'not-a-word') {
        resultContainer.text('The word is not valid.');
    }
}

document.addEventListener("DOMContentLoaded", function () {
    $("#button").click(function () {
        submitWord();
    });
});

// async function submitWord(evt) {
//     evt.preventDefault();
//     const $word = $(".word", this.board);

//     let word = $word.val();
//     if (!word) return;

//     if (this.words.has(word)) {
//         this.showMessage('Already found ${word}', "err");
//         return;
//     }
    
//     // check server for validity
//     const resp = await axios.get("/submit-word", { params: { word: word }});
//     if (resp.data.result === "not-word") {
//       this.showMessage(`${word} is not a valid English word`, "err");
//     } else if (resp.data.result === "not-on-board") {
//       this.showMessage(`${word} is not a valid word on this board`, "err");
//     } else {
//       this.showWord(word);
//       this.score += word.length;
//       this.showScore();
//       this.words.add(word);
//       this.showMessage(`Added: ${word}`, "ok");
//     }

//     $word.val("").focus();
//   }